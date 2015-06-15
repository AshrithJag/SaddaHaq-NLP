import sys
import re
import json


def main():
    tweet_file = open("tweets_from_trends.txt")

    scores = {}

    f = open('final_tweet_from_trends.txt','w+')
    for line in tweet_file:
        x = json.loads(line)
        score = 0
        if len(x.keys()) != 1:
            y = x[u'text']
            encoded = y.encode('utf-8')
            f.write("TWEET ------"+encoded+'\n')
#            for item in scores:
#                if re.search(item,encoded,re.IGNORECASE):
#                    score += scores[item]
#            print score

        else:
            f.write(0+'\n')
    f.close()


if __name__ == '__main__':
    main()
