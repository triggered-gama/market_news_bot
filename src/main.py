# src/main.py

from fetch_news import fetch_from_rss
from deduplicate import deduplicate_articles


def main():
    articles = fetch_from_rss()
    print(f"\nFetched {len(articles)} articles")

    deduped_articles = deduplicate_articles(articles)
    print(f"After deduplication: {len(deduped_articles)} articles\n")

    # Sort by published time (latest first)
    deduped_articles.sort(
        key=lambda x: x["published_at"],
        reverse=True
    )

    for idx, article in enumerate(deduped_articles[:5], start=1):
        print(f"{idx}. {article['title']}")
        print(f"   Source: {article['source']}")
        print(f"   Published: {article['published_at']}")
        print(f"   Link: {article['url']}\n")


if __name__ == "__main__":
    main()
