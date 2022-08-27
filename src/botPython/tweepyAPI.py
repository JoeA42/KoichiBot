import os

import tweepy
from tweepy import API

from src.res.config import create_api

print("TEST for tweepyAPI.py")


def create_tweet(message):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))

    # Create API object
    api = tweepy.API(auth)

    # Create a tweet
    api.update_status(message)
    print(f"tweet posted with the message: {message}")


def create_direct_message():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
    auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

    # Create API object
    api = tweepy.API(auth)

    api.send_direct_message()


def get_moots():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
    auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

    # Create API object
    api = tweepy.API(auth)
    API.get_friend_ids()


create_tweet("Test for automated tweets")
