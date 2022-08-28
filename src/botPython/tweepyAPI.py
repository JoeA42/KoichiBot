import os
import time

import tweepy
from dotenv import load_dotenv
from tweepy import API

print("TEST for tweepyAPI.py")
load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
key = os.getenv("ACCESS_TOKEN")
secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
client = tweepy.Client(bearer_token, consumer_key, consumer_secret, key, secret)


def create_tweet(message):
    # Authenticate to Twitter
    auth.set_access_token(key, secret)

    # Create a tweet
    api.update_status(message)
    print(f"tweet posted with the message: {message}")


def create_direct_message():
    # Authenticate to Twitter
    auth.set_access_token(key, secret)

    api.send_direct_message()


def get_moots():
    # Authenticate to Twitter
    auth.set_access_token(key, secret)

    # Create API object
    return API.get_friend_ids(api)


class TweetStream(tweepy.StreamingClient):

    def on_connect(self):
        print("Connected")

    def on_tweet(self, tweet):
        print(tweet.text)
        time.sleep(0.2)
        # try:
        #     client.like(tweet.id)
        #     client.retweet(tweet.id)
        # except Exception as error:
        #     print(error)


def get_tweets_by():
    auth.set_access_token(key, secret)
    tweets = api.home_timeline()
    for tweet in tweets:
        print(tweet.text)
        client.like(tweet)


# get_tweets_by()
# stream = TweetStream(bearer_token=bearer_token)
# stream.delete_rules(1563725008375091200)
# rule = tweepy.StreamRule(" from:AlvarezKoichi #KoichiExplains ")
# stream.add_rules(rule)
# print(stream.get_rules())
# stream.disconnect()
# stream.filter(tweet_fields=["referenced_tweets"])

# def retweet_latest
create_tweet("KoichiBot off 🐱💤🛌🏾")
# create_tweet("KoichiBot on 💻 dev mode (I'm tweeting programmatically!)")
# create_tweet("KoichiBot on 📋 test mode (I'm tweeting "
#              "programmatically!)")
# create_tweet("KoichiBot on 🐱⏰🍵 (I'm tweeting "
#              "programmatically!)")
# print(get_moots())
