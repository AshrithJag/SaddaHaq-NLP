from TwitterAPI import TwitterAPI, TwitterRestPager
import re
import sys


#WORDS_TO_COUNT = ['chrome']


API_KEY = 'JC6TDHynInJgaoDeKeoYTxzPg'
API_SECRET = 'VKfpn3guTJ90ake3d0lJLlh7GEOpHN2krvdy2FhQm5OJc5e5tN'
ACCESS_TOKEN = '1420838546-cpXpL7fd7SiP4IZqkklXQDTEpCN4eSNSgqWT17F'
ACCESS_TOKEN_SECRET = 'YmfLEDbRjaiOg8lgQ6thyKZPQQxR4lQDXv6dolvqDX7gV'


api = TwitterAPI(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#counts = dict((word,0) for word in WORDS_TO_COUNT)


#def process_tweet(text):
#	text = text.lower()
#	for word in WORDS_TO_COUNT:
#		if word in text:
#			counts[word] += 1
#	print(counts)



param = str(sys.argv[1])

f = open("trends.txt")
f = f.readlines()
param = f[int(param)]

if param:
    if param[0] == '#':
        param = param[1:]
    if param[len(param)-1] == '\n':
        param = param[:len(param)-1]

WORDS_TO_COUNT = param.split()
words = ' AND '.join(WORDS_TO_COUNT)

r = TwitterRestPager(api, 'search/tweets', {'q':words, 'count':100})

fp = open('alltweets_from_trends.txt','w+')
count = 0
for item in r.get_iterator(wait=1):
	if 'text' in item:
            if 'retweeted_status' not in item: 
#            if 'retweeted_status' in item and item[u'retweeted_status'] == False: 
	        fp.write(str(item)+'\n')
                count += 1
                print count
                if count == 1000:
                    break
	elif 'message' in item and item['code'] == 88:
		print('\n*** SUSPEND, RATE LIMIT EXCEEDED: %s\n' % item['message'])
		break

fp.close()
