# src/main.py

from src.fetch_news import fetch_from_rss
from src.deduplicate import deduplicate_articles
from src.summarize import summarize_articles
from src.generate_html import generate_html_dashboard


def main():
    # 1. Fetch news
    articles = fetch_from_rss()

    # 2. Deduplicate
    deduped_articles = deduplicate_articles(articles)

    # 3. Sort newest first
    deduped_articles.sort(
        key=lambda x: x["published_at"],
        reverse=True
    )

    # 4. Summarize ALL articles
    summarized_articles = summarize_articles(deduped_articles)

    # 5. Generate HTML dashboard
    dashboard_path = generate_html_dashboard(summarized_articles)

    # 6. Logs
    print("\nDashboard refreshed successfully")
    print(f"HTML dashboard generated at: {dashboard_path}")
    print(f"Total articles on dashboard: {len(summarized_articles)}")


if __name__ == "__main__":
    main()



# import os

# from src.fetch_news import fetch_from_rss
# from src.deduplicate import deduplicate_articles

# from src.summarize import summarize_articles
# from src.generate_html import generate_html_dashboard
# from src.email_digest import send_email_digest

# def main():
#     articles = fetch_from_rss()
#     deduped_articles = deduplicate_articles(articles)

#     deduped_articles.sort(
#         key=lambda x: x["published_at"],
#         reverse=True
#     )

#     # Summarize ALL (we’ll optimize later if needed)
#     summarized_articles = summarize_articles(deduped_articles)

#     dashboard_path = generate_html_dashboard(summarized_articles)

#     print(f"\nHTML dashboard generated at: {dashboard_path}")
#     print(f"Total articles on dashboard: {len(summarized_articles)}")


#     TOP_10 = sorted(
#         deduped_articles,
#         key=lambda x: x["published_at"],
#         reverse=True
#     )

#     sender_email = os.getenv("SENDER_EMAIL")
#     receiver_email = os.getenv("RECEIVER_EMAIL")
#     app_password = os.getenv("EMAIL_APP_PASSWORD")

#     if not all([sender_email, receiver_email, app_password]):
#         print("Email credentials not set. Skipping email.")
#     else:
#         send_email_digest(
#             articles=TOP_10,
#             # dashboard_url="http://localhost:8000", ## for testing it locally
#             dashboard_url="https://<username>.github.io/market_news_bot/", ## when pushing it to GitHub Pages
#             sender_email=sender_email,
#             receiver_email=receiver_email,
#             app_password=app_password,
#         )

# if __name__ == "__main__":
#     main()


