import tweepy, sys, time
import urllib3.contrib.pyopenssl
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

api = tweepy.API(auth)
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print tweet.text

# Tweet every X min ...

#user = api.get_user('twitter')
#trend = api.trends_available()

#print user.screen_name
#print user.followers_count
#for friend in user.friends():
#       print friend.screen_name

'''api1 = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
count = 0
skip = 0
r = api1.request('statuses/filter', {'track':'giraffe'})
for item in r:
    if 'text' in item:
        count += 1
    elif 'limit' in item:
        skip = item['limit'].get('track')
        print('*** SKIPPED %d TWEETS' % skip)
    elif 'disconnect' in item:
        print('[disconnect] %s' % item['disconnect'].get('reason'))
        break
    print(count+skip);
'''
