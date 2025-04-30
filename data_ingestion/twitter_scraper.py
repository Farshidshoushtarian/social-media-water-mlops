# twitter_scraper.py (Twitter API v2)

import os
import json
from datetime import datetime
from dotenv import load_dotenv
import tweepy

# Load credentials
load_dotenv()
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

# Authenticate
client = tweepy.Client(bearer_token=bearer_token)

# Query setup
query = "water outage OR pipe burst OR low pressure -is:retweet"
max_results = 50

# Search tweets from the last 7 days
response = client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=["created_at", "text", "author_id", "lang"])

# Output directory
output_dir = "data_ingestion/raw_data"
os.makedirs(output_dir, exist_ok=True)
filename = f"{output_dir}/tweets_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

# Save results
with open(filename, "w", encoding="utf-8") as f:
    for tweet in response.data:
        json.dump(tweet.data, f)
        f.write("\n")

print(f"✅ Saved {len(response.data)} tweets to {filename}")
