import os

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

    def on_tweet(self, tweet):
        print(tweet.text)
        try:
            client.retweet(tweet.id)
            client.like(tweet.id)
        except Exception as error:
            print(error)


def get_tweets_by():
    auth.set_access_token(key, secret)
    tweets = api.mentions_timeline()
    print(tweets[0].text)


# get_tweets_by()
# stream = TweetStream(bearer_token=bearer_token)
# stream.delete_rules()
# rule = tweepy.StreamRule(" from:GeorgeTakei ")
# print(stream.get_rules())
# stream.disconnect()
# stream.add_rules(rule)
# stream.filter()


# def retweet_latest
create_tweet("KoichiBot off (I'm tweeting "
             "programmatically!)")
# print(get_moots())
