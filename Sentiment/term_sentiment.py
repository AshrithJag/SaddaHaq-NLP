import sys
import re
import json


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}
    nsenti = {} #For non sentiment words

    for line in sent_file:
  	term, score  = line.split("\t")
  	scores[term] = int(score)

#    f = open('text.txt','r')
#    for line in f:
#    	sc.append(line)
#    f.close()
#    print sc

    for line in tweet_file:
	x = json.loads(line)
	if len(x.keys()) != 1:
		y = x[u'text']
		encoded = y.encode('utf-8')

		spl = encoded.split()
		#spl is the non senti array and scores is senti dict

		score = 0.0
		sc = {}
		for itr in range(len(spl)):
			if spl[itr] in scores.keys():
				sc[itr] = scores[spl[itr]]

#		print sc
		for itr in range(len(spl)):
			if itr in sc.keys():
				z = 1
			elif spl[itr] not in nsenti.keys():
				for itm in sc.keys():
					score += float(abs(itr - itm)*sc[itm])
				nsenti[spl[itr]] = score
			elif spl[itr] in nsenti.keys():
				#calculate score
				for itm in sc.keys():
					score += float(abs(itr - itm)*sc[itm])
				nsenti[spl[itr]] += float(score)
							
    for item in nsenti.keys():
	    print str(item) + ' ' + str(nsenti[item])


if __name__ == '__main__':
    main()
