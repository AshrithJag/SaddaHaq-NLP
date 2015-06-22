import sys
import re
from textblob import TextBlob
import nltk.data


def main():

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    fil = str(sys.argv[1])
    f = open(fil, 'r')
    inp = f.readlines()
    f.close()


    
    data = []
    for line in inp:
#        data.extend(tokenizer.tokenize(str(line)))
        data.extend(re.compile("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s").split(line)) 
#        data.extend(TextBlob(line).sentences)
    
#    inp = inp.encode('utf-8')
    x = []
    for line in data:
        x.append(line.strip('\n'))

    x = filter(None, x) # fastest

#    print x
    facts = []
    opinions = []
    for line in x:
        temp = TextBlob(str(line))
        if temp.sentiment.subjectivity <= 0.25:
            facts.append(temp)
        elif temp.sentiment.subjectivity >= 0.50:
            opinions.append(temp)
        print temp + '------------' + str(temp.sentiment.subjectivity)

    print facts
    print opinions

if __name__ == '__main__':
    main()
