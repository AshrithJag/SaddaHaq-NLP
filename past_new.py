import oauth2 as oauth
import urllib2 as urllib
import urllib as urllib_pre
import sys
import io
import json

# See assignment1.html instructions or README for how to get these credentials

api_key = 'JC6TDHynInJgaoDeKeoYTxzPg'
api_secret = 'VKfpn3guTJ90ake3d0lJLlh7GEOpHN2krvdy2FhQm5OJc5e5tN'
access_token_key = '1420838546-cpXpL7fd7SiP4IZqkklXQDTEpCN4eSNSgqWT17F'
access_token_secret = 'YmfLEDbRjaiOg8lgQ6thyKZPQQxR4lQDXv6dolvqDX7gV'

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response



def fetchsamples(url):

#  url = "https://stream.twitter.com/1.1/statuses/filter.json?track=@katyperry"
# katyperry id = 21447363
# verified id present in the tweet  
  parameters = []
  response = twitterreq(url, "GET", parameters)
#  print response
  f = open("tweets_trying.txt",'w+')
#  count = 0
#  limit = sys.argv[1]
  for line in response:
    x = line.strip() + '\n'
    x = json.loads(x)
    y = x[u'statuses']
    for ele in y:
        print ele
#    count += 1
#    if count >= int(limit):
#        break
  f.close()


if __name__ == '__main__':
#    f = io.open('trends.txt','r',encoding='utf-8')
#    f = f.readlines()

#   Cleaning the Values from the trends returned.
#   for i in range(len(f)):
#        if f[i][0] == '#':
#            f[i] = f[i][1:]
#        if f[i][len(f[i])-1] == '\n':
#            f[i] = f[i][:len(f[i])-1]

#    param = ''
#    for i in f:
#        param = param+i+','
#    param = ",".join(f)
#    print param
#    param = param[:len(param)-1]

    param = str(sys.argv[1])
    f = open("trends.txt")
    f = f.readlines()
    param = f[int(param)]

    if param:
        if param[0] == '#':
            param = param[1:]
        if param[len(param)-1] == '\n':
            param = param[:len(param)-1]
        
#    param = "https://api.twitter.com/1.1/search/tweets.json?q=chrome&since_id=24012619984051000&result_type=popular&count=1000"
    param = urllib_pre.quote_plus(param)
    param = "https://api.twitter.com/1.1/search/tweets.json?q=" + str(param) + "&result_type=popular"
#    print param
#    param = "https://api.twitter.com/1.1/search/tweets.json?q=from%3ACmdr_Hadfield%20%23nasa&result_type=popular"
    param = param.decode('ascii','ignore')
    fetchsamples(param)
