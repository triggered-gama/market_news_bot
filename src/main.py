# src/main.py

from fetch_news import fetch_from_rss

def main():
    articles = fetch_from_rss()
    print(f"Fetched {len(articles)} articles")

    for a in articles[:5]:
        print(a["title"], a["published_at"])

if __name__ == "__main__":
    main()
