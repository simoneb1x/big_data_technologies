import tweepy
import config

client = tweepy.Client(bearer_token=config.bearer_token, 
              consumer_key=config.consumer_key, 
              consumer_secret=config.consumer_secret, 
              access_token=config.access_token, 
              access_token_secret=config.access_token_secret
              )

recent_tweets_about_oscar = client.search_recent_tweets(
                                "#Oscar",
                                max_results=10
                            )

tweets_array = []

for elem in recent_tweets_about_oscar:
    tweets_array.append(elem)

for tweet in recent_tweets_about_oscar[0]:
    print(tweet.data)
    print(" ")

print(tweets_array)