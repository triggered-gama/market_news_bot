# src/fetch_news.py

import feedparser
from dateutil import parser as date_parser
from typing import List, Dict

RSS_FEEDS = {
    "reuters": "https://feeds.reuters.com/reuters/businessNews",
    "yahoo_finance": "https://finance.yahoo.com/rss/topstories",
    "cnbc": "https://www.cnbc.com/id/100003114/device/rss/rss.html",
}

def fetch_from_rss() -> List[Dict]:
    articles = []

    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)

        for entry in feed.entries:
            try:
                published_at = date_parser.parse(entry.published)
            except Exception:
                continue

            articles.append({
                "title": entry.get("title", ""),
                "description": entry.get("summary", ""),
                "content": entry.get("summary", ""),
                "url": entry.get("link", ""),
                "source": source,
                "published_at": published_at,
            })

    return articles
