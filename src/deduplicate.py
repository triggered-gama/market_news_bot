# src/deduplicate.py

import re
from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def normalize_text(text: str) -> str:
    """
    Normalize text for comparison:
    - lowercase
    - remove punctuation
    - collapse spaces
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def deduplicate_articles(
    articles: List[Dict],
    similarity_threshold: float = 0.85
) -> List[Dict]:
    """
    Deduplicate news articles using URL, title hash,
    and TF-IDF cosine similarity.
    """

    if not articles:
        return []

    # 1️⃣ URL-level dedup
    seen_urls = set()
    url_deduped = []

    for article in articles:
        if article["url"] in seen_urls:
            continue
        seen_urls.add(article["url"])
        url_deduped.append(article)

    # 2️⃣ Title normalization dedup
    seen_titles = set()
    title_deduped = []

    for article in url_deduped:
        normalized_title = normalize_text(article["title"])
        if normalized_title in seen_titles:
            continue
        seen_titles.add(normalized_title)
        title_deduped.append(article)

    # 3️⃣ Content similarity dedup (TF-IDF)
    texts = [
        normalize_text(a["title"] + " " + a["content"])
        for a in title_deduped
    ]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(texts)
    similarity_matrix = cosine_similarity(tfidf_matrix)

    unique_indices = []
    visited = set()

    for i in range(len(title_deduped)):
        if i in visited:
            continue

        unique_indices.append(i)

        for j in range(i + 1, len(title_deduped)):
            if similarity_matrix[i, j] >= similarity_threshold:
                visited.add(j)

    return [title_deduped[i] for i in unique_indices]
