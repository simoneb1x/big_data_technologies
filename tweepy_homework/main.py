import tweepy
import config

client = tweepy.Client(bearer_token=config.bearer_token, 
              consumer_key=config.consumer_key, 
              consumer_secret=config.consumer_secret, 
              access_token=config.access_token, 
              access_token_secret=config.access_token_secret
              )

recent_tweets_about_oscar = client.search_recent_tweets("#Oscar", max_results=10)
tweet_number = 1

for elem in recent_tweets_about_oscar.data:
    temp = elem.data
    print("+++++++++++++++++++++++++")
    print("Tweet n.%d" % (tweet_number))
    print("ID: " + elem.data["id"])
    print("Text: " + elem.data["text"])
    print("+++++++++++++++++++++++++")
    print(" ")
    tweet_number += 1