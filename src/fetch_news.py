# src/fetch_news.py

import feedparser
from dateutil import parser as date_parser
from typing import List, Dict
from datetime import datetime

from utils.market_relevance import is_market_relevant
from utils.time_filters import is_within_intraday_window


RSS_FEEDS = {
    "moneycontrol_latest": "https://www.moneycontrol.com/rss/latestnews.xml",
    "moneycontrol_markets": "https://www.moneycontrol.com/rss/marketreports.xml",
    "economic_times_markets": "https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms",
    "business_standard_markets": "https://www.business-standard.com/rss/markets-106.rss",
    "livemint_markets": "https://www.livemint.com/rss/market",
    "cnbc_tv18": "https://www.cnbctv18.com/rss/market.xml",
}


def fetch_from_rss() -> List[Dict]:
    """
    Fetch Indian market-related news from free RSS feeds,
    filter for intraday relevance, and normalize schema.
    """
    articles = []

    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)

        for entry in feed.entries:
            try:
                published_at = date_parser.parse(entry.published)
            except Exception:
                continue

            # 🔒 Hard safety check against very old content
            if published_at.year < 2024:
                continue

            # ⏱ Intraday filter (IST aware)
            if not is_within_intraday_window(published_at):
                continue

            title = entry.get("title", "").strip()
            summary = entry.get("summary", "").strip()
            combined_text = f"{title} {summary}"

            # 📈 Market relevance filter
            if not is_market_relevant(combined_text):
                continue

            articles.append({
                "title": title,
                "description": summary,
                "content": summary,
                "url": entry.get("link", ""),
                "source": source,
                "published_at": published_at,
                "fetched_at": datetime.utcnow(),
            })

    return articles
