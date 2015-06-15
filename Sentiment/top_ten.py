import sys
import operator
import json
from collections import OrderedDict

def main():
    tweet_file = open(sys.argv[1])

    scores = {}
    freq = {} #For hashtags

    for line in tweet_file:
	x = json.loads(line)
	if len(x.keys()) != 1:
		y = x[u'text']
		y = y.encode('utf-8')
		z = x[u'entities'][u'hashtags']
		for item in z:
			temp = item[u'text']
			if temp in freq.keys():
				freq[temp] += 1
			else:
			 	freq[temp] = 1
#    sorted_x = sorted(freq.iteritems(), key=operator.itemgetter(1))
#    desc = OrderedDict(sorted(freq.items(),key=lambda kv: freq[kv], reverse=True))
    desc = sorted(freq.iteritems(), key=operator.itemgetter(1) , reverse=True)
    ind = 0
    for item in desc:
#	print item + ' '+ str(freq[item])
    	print item[0] + ' ' + str(item[1])
	ind += 1
	if ind == 10:
		break


#    for item in freq.keys():
#	    print item + ' ' + str(freq[item]/total)

if __name__ == '__main__':
    main()
