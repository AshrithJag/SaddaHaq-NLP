import sys
import re
import json

#def hw():
#    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}
    for line in sent_file:
  	term, score  = line.split("\t")
  	scores[term] = int(score)

    for line in tweet_file:
	x = json.loads(line)
	score = 0
	if len(x.keys()) != 1:
		y = x[u'text']
		encoded = y.encode('utf-8')
#		print encoded
		for item in scores:
			if re.search(item,encoded,re.IGNORECASE):
				score += scores[item]
		print score
	
	else:
		print 0
		
#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()
