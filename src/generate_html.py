# src/generate_html.py

from typing import List, Dict
from datetime import datetime
from pathlib import Path
import pytz


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Indian Market News – {date}</title>

    <!-- Auto refresh every 5 minutes -->
    <meta http-equiv="refresh" content="300">

    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f7f7f7;
        }}
        h1 {{
            color: #222;
        }}
        .refresh-info {{
            background: #e9f2ff;
            padding: 10px 14px;
            border-left: 4px solid #0b5ed7;
            margin-bottom: 20px;
            font-size: 14px;
        }}
        .article {{
            background: #ffffff;
            padding: 16px;
            margin-bottom: 16px;
            border-radius: 6px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        .meta {{
            font-size: 12px;
            color: #666;
            margin-bottom: 6px;
        }}
        .title a {{
            font-size: 18px;
            font-weight: bold;
            color: #0b5ed7;
            text-decoration: none;
        }}
        .title a:hover {{
            text-decoration: underline;
        }}
        .summary {{
            margin-top: 8px;
            font-size: 14px;
            color: #333;
        }}
        .footer {{
            margin-top: 40px;
            font-size: 12px;
            color: #888;
            text-align: center;
        }}
    </style>
</head>
<body>

<h1>📊 Indian Stock Market News – {date}</h1>

<div class="refresh-info">
    <strong>Last refreshed:</strong> {generated_at} IST  
    &nbsp;•&nbsp; Auto-refreshes every 5 minutes
</div>

{articles}

<div class="footer">
    Generated automatically by <strong>market_news_bot</strong>
</div>

</body>
</html>
"""


def generate_article_block(article: Dict) -> str:
    published = article["published_at"].astimezone(
        pytz.timezone("Asia/Kolkata")
    ).strftime("%d %b %Y, %H:%M")

    source = article["source"].replace("_", " ").title()

    return f"""
    <div class="article">
        <div class="meta">{published} IST | {source}</div>
        <div class="title">
            <a href="{article['url']}" target="_blank" rel="noopener noreferrer">
                {article['title']}
            </a>
        </div>
        <div class="summary">{article['summary']}</div>
    </div>
    """


def generate_html_dashboard(articles: List[Dict], output_dir: str = "output") -> str:
    """
    Generates HTML dashboard and returns the index file path.
    """

    Path(output_dir).mkdir(exist_ok=True)

    ist = pytz.timezone("Asia/Kolkata")
    now_ist = datetime.now(ist)

    today = now_ist.strftime("%Y-%m-%d")
    generated_at = now_ist.strftime("%d %b %Y, %H:%M")

    article_blocks = "\n".join(
        generate_article_block(article) for article in articles
    )

    html_content = HTML_TEMPLATE.format(
        date=today,
        generated_at=generated_at,
        articles=article_blocks
    )

    index_file = Path(output_dir) / "index.html"
    index_file.write_text(html_content, encoding="utf-8")

    return str(index_file)
