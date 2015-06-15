$Author : Ashrith Jalagam


Steps to be followed to Run the Code(s) : 

1) First, Using the Live TwitterStream, an output file called "output.txt" was captured after running the code "twitterstream.py" for a few seconds.
Command : "python twitterstream.py > output.txt"

2) Next, the sentiment of each tweet was derived based on the scores of the terms in the tweet. The file AFINN-111.txt contains a list of pre-computed sentiment scores.
Each line in the file contains a word or phrase followed by a sentiment score.
Each word or phrase that is found in a tweet but not found in AFINN-111.txt was given a sentiment score of 0.
Command : "python tweet_sentiment.py AFINN-111.txt output.txt"
Output : Sentiment of each tweet in the file, one numeric sentiment per line.
Order is on the basis of the tweet location in the "output.txt" file i.e the nth line has sentiment corresponding to the nth tweet in the "output.txt" file.

3) Now, for finding the sentiment of the terms which do not appear in AFINN-111.txt, we use the Closeness measure of the word alongside words whose sentiment is already known.
Command : "python term_sentiment.py AFINN-111.txt output.txt"
Output : A term followed by a space, then its sentiment score in each line.

4) Then, We compute the term frequeny histogram for the data in "output.txt".
Command : "python frequency.py output.txt"
Output : A term followed by a space, then its new sentiment score in each line.

5) Now, I Found out the happiest state in terms of the tweets generated in "output.txt".
This was done using the location attribute of a tweet and its correspoding score.
Command :  "python happiest_state.py AFINN-111 output.txt"
Output : The State Abbreviation which is the happpiest.

6) Finally, the top ten hash tags which occured most frequently in the given file.
Command : "python top_ten.py output.txt"
Output : The hashtag followed by a space, then their frequency in the descending order in each line.



NOTE : Not all are tweets in the "output.txt" file.
