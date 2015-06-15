import sys
import re
import json
import ast


def main():
    sent_file = open("AFINN-111.txt")
    tweet_file = open("tweets_from_trends.txt")

    scores = {}

    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)

    fp = open("scores.txt", "w+")
    for line in tweet_file:
#        x = line
        x = ast.literal_eval(line)
#        print x
        score = 0
        if len(x.keys()) != 1:
            y = x[u'text']
            encoded = y.encode('utf-8')
#            print encoded
            for item in scores:
                if re.search(item,encoded,re.IGNORECASE):
                    score += scores[item]
#            print 'TWEEEEEEET------------' + x[u'text'] + '-----------||||' + str(score) + '||||--------' + x[u'created_at']
            fp.write(str(score) + '\n')

        else:
            fp.write('0\n')

    fp.close()

if __name__ == '__main__':
    main()