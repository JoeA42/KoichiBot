import tweepy
from src.res import configModule



class AuthPackage(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):

    # protected data members
    def __init__(self):
        self.__CONSUMER_KEY = CONSUMER_KEY
        self.__CONSUMER_SECRET = CONSUMER_SECRET
        self.__ACCESS_TOKEN = ACCESS_TOKEN
        self.__ACCESS_TOKEN_SECRET = ACCESS_TOKEN_SECRET
        pass

        # Authenticate to Twitter
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


configModule

AuthPackage().__init__()

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Tweepy")
