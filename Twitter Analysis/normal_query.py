import tweepy, sys, time
import urllib3
import urllib3.contrib.pyopenssl
import requests
from requests_oauthlib import OAuth1
urllib3.contrib.pyopenssl.inject_into_urllib3()
from TwitterAPI import TwitterAPI
                
# Substitute your API and ACCESS credentials.

#Keys and Tokens
consumer_key = 'JC6TDHynInJgaoDeKeoYTxzPg'
consumer_secret = 'VKfpn3guTJ90ake3d0lJLlh7GEOpHN2krvdy2FhQm5OJc5e5tN'
access_token = '1420838546-cpXpL7fd7SiP4IZqkklXQDTEpCN4eSNSgqWT17F'
access_token_secret = 'YmfLEDbRjaiOg8lgQ6thyKZPQQxR4lQDXv6dolvqDX7gV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

def get_oauth():
    oauth = OAuth1('JC6TDHynInJgaoDeKeoYTxzPg', client_secret= 'VKfpn3guTJ90ake3d0lJLlh7GEOpHN2krvdy2FhQm5OJc5e5tN',
 resource_owner_key= '1420838546-cpXpL7fd7SiP4IZqkklXQDTEpCN4eSNSgqWT17F'
, resource_owner_secret= 'YmfLEDbRjaiOg8lgQ6thyKZPQQxR4lQDXv6dolvqDX7gV' )

    return oauth

api = tweepy.API(auth)

oauth = get_oauth()
# Tweet every X min ...
r = requests.get(url="https://api.twitter.com/1.1/users/lookup.json?screen_name=katyperry", auth=oauth)
print r.json()
