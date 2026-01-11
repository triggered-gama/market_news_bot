# src/summarize.py

from typing import List, Dict
from transformers import pipeline

# Load once (important for performance)
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    device=-1  # CPU
)


def summarize_articles(
    articles: List[Dict],
    max_length: int = 120,
    min_length: int = 40
) -> List[Dict]:
    """
    Add summary field to each article.
    """

    summarized_articles = []

    for article in articles:
        text = article["content"]

        # Guardrail: very short articles
        if len(text.split()) < 50:
            article["summary"] = text
            summarized_articles.append(article)
            continue

        try:
            summary = summarizer(
                text,
                max_length=max_length,
                min_length=min_length,
                do_sample=False
            )[0]["summary_text"]
        except Exception as e:
            # Fail-safe: fallback to description
            summary = article.get("description", "")

        article["summary"] = summary
        summarized_articles.append(article)

    return summarized_articles
