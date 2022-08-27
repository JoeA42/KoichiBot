# tweepy-bots/bots/config.py
import logging
import os

import tweepy

logger = logging.getLogger()


def create_api():
    print("creating API... and AuthPackage")
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    print(consumer_key, consumer_secret, access_token, access_token_secret)

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

# class AuthPackage:
#
#     # protected data members
#     def __init__(self):
#         consumer_key = os.getenv("CONSUMER_KEY")
#         consumer_secret = os.getenv("CONSUMER_SECRET")
#         access_token = os.getenv("ACCESS_TOKEN")
#         access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
#         pass
#
#         # Authenticate to Twitter
#         auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#         auth.set_access_token(access_token, access_token_secret)
#
#         create_api()
