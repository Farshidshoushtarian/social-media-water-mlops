# twitter_scraper.py (Fixed to DC Water + Keywords)

import os
import json
from datetime import datetime
from dotenv import load_dotenv
import tweepy

# Load credentials
load_dotenv()
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

# Authenticate with Twitter API v2
client = tweepy.Client(bearer_token=bearer_token)

# Fixed utility and keywords
utility_name = "DC Water"
x_handle = "@dcwater"
keywords = [
    "water outage",
    "no water",
    "low water pressure",
    "burst pipe",
    "dirty water",
    "brown water",
    "boil water notice",
    "discolored water",
    "water contamination",
    "high water bill"
]

# Build the query: (@dcwater OR keyword1 OR keyword2 ...) -is:retweet
query = f"{x_handle} AND ({' OR '.join(keywords)}) -is:retweet"

# Twitter search params
max_results = 100
response = client.search_recent_tweets(
    query=query,
    max_results=max_results,
    tweet_fields=["created_at", "text", "author_id", "lang", "public_metrics"],
)

# Save tweets
output_dir = "data_ingestion/raw_data"
os.makedirs(output_dir, exist_ok=True)
filename = f"{output_dir}/dc_water_tweets_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

with open(filename, "w", encoding="utf-8") as f:
    for tweet in response.data or []:
        json.dump(tweet.data, f)
        f.write("\n")

print(f"✅ Saved {len(response.data or [])} tweets for {utility_name} to {filename}")
