#!usr/bin/src python3
from rnd import api_call
from scrape import find_all
from twitter import * 
import base64
import hashlib
import os
import re
import requests
import tweepy

from requests_oauthlib import OAuth2Session

# setting the api connection stuff
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_ID")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")
API_KEY  = os.environ.get("TWITTER_API_KEY")
API_SECRET = os.environ.get("TWITTER_API_KEY_SECRET")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
auth_url = "https://twitter.com/i/oauth2/authorize"
token_url = "https://api.twitter.com/2/oauth2/token"
end_url = "https://api.twitter.com/2/tweets"

scopes = ["tweet.read", "users.read", "tweet.write"]

def prep_time(word):
    print("Setting up authentication...")
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET, bearer_token=BEARER_TOKEN)

    print("Getting the word and definition...")
    tweet = api_call(word)
    
    print(f"Tweeting about {i}...")
    client.create_tweet(text=tweet)
    print("Success!")

with open("words.txt", "r") as f:
    dictionary = f.read().splitlines()

# finding all the links
with open("links.txt", "r") as f:
    links = f.read().split("\n")[:-1]
    words = find_all(links)
    words = [i for i in words if i not in dictionary]

with open("words.txt", "a") as f:
    for i in words:
        f.write(i)

for i in words:
    prep_time(i)
