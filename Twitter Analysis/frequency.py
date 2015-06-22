from __future__ import division
import sys
import json

def main():
    tweet_file = open("tweets_from_trends.txt")

    scores = {}
    freq = {} #For non sentiment words

    for line in tweet_file:
	x = json.loads(line)
	if len(x.keys()) != 1:
		y = x[u'text']
		encoded = y.encode('utf-8')

		spl = encoded.split()
		#spl is the non senti array and scores is senti dict

		for itr in range(len(spl)):
			if spl[itr] not in freq.keys():
				freq[spl[itr]] = 1;
			else:
				freq[spl[itr]] += 1
							
    total = 0.0
    for item in freq.keys():
	    total += float(freq[item])

    for item in freq.keys():
	    print item + ' ' + str(freq[item]/total)

if __name__ == '__main__':
    main()
