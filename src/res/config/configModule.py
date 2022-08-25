# tweepy-bots/bots/config.py
import tweepy
import logging
import os

logger = logging.getLogger()


def create_api():
    print("creating API...")
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api


class AuthPackage:

    # protected data members
    def __init__(self, CONSUMER_KEY=None, CONSUMER_SECRET=None, ACCESS_TOKEN=None, ACCESS_TOKEN_SECRET=None):
        self.__CONSUMER_KEY = os.getenv("CONSUMER_KEY")
        self.__CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
        self.__ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
        self.__ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
        pass

        # Authenticate to Twitter
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
