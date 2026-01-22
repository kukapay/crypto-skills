#!/usr/bin/env python3
"""
Crypto Market Sentiment Analyzer
Fetches RSS feeds from popular crypto sources, analyzes sentiment, and calculates a market score.
"""

import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

# Positive and negative keywords for sentiment analysis
POSITIVE_KEYWORDS = [
    "adoption",
    "launch",
    "partnership",
    "etf",
    "rally",
    "breakthrough",
    "growth",
    "approval",
    "bullish",
    "surge",
    "adopts",
]

NEGATIVE_KEYWORDS = [
    "crash",
    "exploit",
    "hack",
    "delay",
    "liquidation",
    "depeg",
    "bearish",
    "decline",
    "setback",
    "breach",
    "drop",
]

# RSS Feed URLs
RSS_FEEDS = [
    "https://www.coindesk.com/arc/outboundfeeds/rss/?outputType=xml",
    "https://cointelegraph.com/rss",
    "https://cryptopotato.com/feed/",
    "https://cryptoslate.com/feed/",
]


def fetch_rss_feed(url):
    """Fetch and parse RSS feed."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return ET.fromstring(response.content)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None


def extract_items(root):
    """Extract title, description, and pubDate from RSS items."""
    items = []
    for item in root.findall(".//item"):
        title = item.find("title")
        description = item.find("description")
        pubdate = item.find("pubDate")

        if title is not None and description is not None:
            # Filter recent items (last 7 days)
            if pubdate is not None:
                try:
                    # Parse pubDate (e.g., "Thu, 22 Jan 2026 06:12:18 +0000")
                    dt = datetime.strptime(pubdate.text[:25], "%a, %d %b %Y %H:%M:%S")
                    if datetime.now() - dt > timedelta(days=7):
                        continue
                except:
                    pass

            items.append(
                {"title": title.text or "", "description": description.text or ""}
            )
    return items


def classify_sentiment(text):
    """Classify sentiment as +1, -1, or 0 based on keywords."""
    text_lower = text.lower()
    pos_count = sum(1 for word in POSITIVE_KEYWORDS if word in text_lower)
    neg_count = sum(1 for word in NEGATIVE_KEYWORDS if word in text_lower)

    if pos_count > neg_count:
        return 1
    elif neg_count > pos_count:
        return -1
    else:
        return 0


def analyze_sentiment(items):
    """Analyze sentiment of items and calculate overall score."""
    sentiments = []
    evidence = {"positive": [], "negative": [], "neutral": []}

    for item in items:
        text = item["title"] + " " + item["description"]
        sentiment = classify_sentiment(text)
        sentiments.append(sentiment)

        if sentiment == 1:
            evidence["positive"].append(item["title"])
        elif sentiment == -1:
            evidence["negative"].append(item["title"])
        else:
            evidence["neutral"].append(item["title"])

    if sentiments:
        score = sum(sentiments) / len(sentiments)
    else:
        score = 0

    return score, evidence


def main():
    all_items = []

    for url in RSS_FEEDS:
        root = fetch_rss_feed(url)
        if root is not None:
            items = extract_items(root)
            all_items.extend(items)

    score, evidence = analyze_sentiment(all_items)

    print(f"Market Sentiment Score: {score:.2f}")
    print("\nExplanation:")
    print(f"- Analyzed {len(all_items)} recent articles from {len(RSS_FEEDS)} feeds.")
    print(
        f"- Positive articles ({len(evidence['positive'])}): {', '.join(evidence['positive'][:5])}"
    )
    print(
        f"- Negative articles ({len(evidence['negative'])}): {', '.join(evidence['negative'][:5])}"
    )
    print(
        f"- Neutral articles ({len(evidence['neutral'])}): {len(evidence['neutral'])} total"
    )

    if score > 0.1:
        print(
            "Overall: Bullish market sentiment with positive drivers outweighing negatives."
        )
    elif score < -0.1:
        print("Overall: Bearish market sentiment with negative factors dominating.")
    else:
        print(
            "Overall: Neutral market sentiment with balanced positive and negative news."
        )


if __name__ == "__main__":
    main()
