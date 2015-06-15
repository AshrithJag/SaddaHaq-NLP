import sys
import re
import json
import ast
import operator
from textblob import TextBlob


def main():
    sent_file = open("AFINN-111.txt")
    tweet_file = open("alltweets_from_trends.txt")

    scores = {}
    sentiment = {}
    hashtags = {}
    mentions = {}

    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)

    count = 1
    for line in tweet_file:
#        x = line
        x = ast.literal_eval(line)
#        print x
        score = 0
        if len(x.keys()) != 1:
            y = x[u'text']

            temp_tag = x[u'entities'][u'hashtags']
            for counting in temp_tag:
                if counting[u'text'] not in hashtags:
                    hashtags[counting[u'text']] = [1, str(count-1)]
                else:
                   hashtags[counting[u'text']][0] += 1
                   hashtags[counting[u'text']][1] += '-'+str(count-1)

            temp_mention = x[u'entities'][u'user_mentions']
            for counting in temp_mention:
                if counting[u'screen_name'] not in mentions:
                    mentions[counting[u'screen_name']] = [1, str(count-1)]
                else:
                    mentions[counting[u'screen_name']][0] += 1
                    mentions[counting[u'screen_name']][1] += '-'+str(count-1)

            encoded = TextBlob(y)
            score = encoded.sentiment.polarity

            sentiment[count-1] = score
            
#            encoded = y.encode('utf-8')
#            print encoded
#            for item in scores:
#                if re.search(item,encoded,re.IGNORECASE):
#                    score += scores[item]
#            print 'TWEEEEEEET------------' + x[u'text'] + '-----------||||' + str(score) + '||||--------' + x[u'created_at']
#            print score

        else:
            sentiment[count-1] = 0

        count += 1

#   Dumping top hastags, top mentions
    final_senti = sorted(sentiment.items(), key=operator.itemgetter(1))
    final_hash = sorted(hashtags.items(), key=operator.itemgetter(1))
    final_mention = sorted(mentions.items(), key=operator.itemgetter(1))

    final_hash = reversed(final_hash)
    final_mention = reversed(final_mention)
    final_senti = reversed(final_senti)

    fp = open('hashtags.txt', 'w+')
    for ele in final_hash:
        fp.write(str(ele[0].encode('utf-8')) + ' : ' + str(ele[1]) + '\n')
    fp.close()

    fp = open('mentions.txt', 'w+')
    for ele in final_mention:
        fp.write(str(ele[0].encode('utf-8')) + ' : ' + str(ele[1]) + '\n')
    fp.close()

    fp = open('allscores.txt', 'w+')
    for ele in final_senti:
        fp.write(str(ele[0]) + ' : ' + str(ele[1]) + '\n')
    fp.close()

    print "Completed :D :D"

if __name__ == '__main__':
    main()
