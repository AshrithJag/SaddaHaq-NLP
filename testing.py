import tweepy
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()


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

user = api.get_user('twitter')
trend = api.trends_available()

#print user.screen_name
#print user.followers_count
#for friend in user.friends():
#       print friend.screen_name

