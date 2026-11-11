import csv
import sys
import os

def load_raw_data(filename):
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    raw_tweets = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_tweets.append(row)
            
    return raw_tweets

def clean_data(tweets):
    cleaned = []
    fixed_or_removed = 0

    for tweet in tweets:
        text = tweet.get('Text', '').strip()
        if not text:
            fixed_or_removed += 1
            continue

        raw_likes = str(tweet.get('Likes', '')).strip()
        if not raw_likes or not raw_likes.isdigit():
            likes = 0
            fixed_or_removed += 1
        else:
            likes = int(raw_likes)

        raw_retweets = str(tweet.get('Retweets', '')).strip()
        if not raw_retweets or not raw_retweets.isdigit():
            retweets = 0
            fixed_or_removed += 1
        else:
            retweets = int(raw_retweets)

        tweet_copy = tweet.copy()
        tweet_copy['Text'] = text
        tweet_copy['Likes'] = likes
        tweet_copy['Retweets'] = retweets
        cleaned.append(tweet_copy)

    print(f"--- QUEST 1: DATA CLEANING ---")
    print(f"Fixed or removed {fixed_or_removed} bad rows/fields.\n")
    return cleaned

def find_viral_tweet(tweets):
    if not tweets:
        print("No tweets available.")
        return None

    viral = tweets[0]
    for tweet in tweets[1:]:
        if tweet['Likes'] > viral['Likes']:
            viral = tweet

    print("--- QUEST 2: VIRAL TWEET ---")
    print(f"Username: @{viral.get('Username', 'N/A')}")
    print(f"Likes:    {viral['Likes']}")
    print(f"Text:     {viral['Text']}\n")
    return viral

def custom_sort_by_likes(tweets):
    sorted_list = tweets.copy()
    n = len(sorted_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j]['Likes'] < sorted_list[j + 1]['Likes']:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]

    print("--- QUEST 3: TOP 10 MOST LIKED TWEETS ---")
    for idx, tweet in enumerate(sorted_list[:10], start=1):
        print(f"{idx}. @{tweet.get('Username', 'N/A')} ({tweet['Likes']} Likes) - {tweet['Text'][:50]}...")
    print()
    return sorted_list

def search_tweets(tweets, keyword):
    matching = []
    kw_lower = keyword.lower()

    for tweet in tweets:
        if kw_lower in tweet['Text'].lower():
            matching.append(tweet)

    print(f"--- QUEST 4: SEARCH RESULTS FOR '{keyword}' ---")
    print(f"Total matching tweets found: {len(matching)}\n")
    for t in matching[:5]:
        print(f"@{t.get('Username', 'N/A')}: {t['Text']}")
    return matching

if __name__ == "__main__":
    dataset = load_raw_data("twitter_dataset.csv")
    print(f"Loaded {len(dataset)} raw tweets.\n")
    
    clean_tweets = clean_data(dataset)
    find_viral_tweet(clean_tweets)
    custom_sort_by_likes(clean_tweets)
    
    search_keyword = input("Enter a keyword to search (e.g. Python): ")
    search_tweets(clean_tweets, search_keyword)
