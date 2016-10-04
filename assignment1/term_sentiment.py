# Problem 3: Derive the sentiment of new terms
# In this part you will be creating a script that computes the sentiment
# for the terms that do not appear in the file AFINN-111.txt.

# Here's how you might think about the problem: We know we can use the
# sentiment-carrying words in AFINN-111.txt to deduce the overall sentiment of a tweet.
# Once you deduce the sentiment of a tweet, you can work backwards to deduce
# the sentiment of the non-sentiment carrying words that do not appear in AFINN-111.txt.
# For example, if the word soccer always appears in proximity with positive words
# like great and fun, then we can deduce that the term soccer itself carries a positive sentiment.

#Approach to the problem
'''
(1): Compute the sentiment of the whole tweet by using the same logic as tweet_sentiment
(2): In order to save computing power, we will iterate through all words/tweet/line and then
evaluate the sentiment by lookup on the AFN-111 dictionary again, but this time we will 
add the words that are not on the list to unscored_words
Before returning the sentiment of the whole line, we will iterate through the un_scored_words and 
add the sentiment score into the unscored_word dictionary
(3)We will repeat this process for all lines of the tweet file and as we encounter the same word 
in another line, we will not add it to the dictionary again and remember to check the key first
'''


import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    term_score(sent_file,tweet_file)
    
def term_score(sentiment,tweet):
    scores = dict()
    unscored_words = dict()
    current_sentiment = 0
    #Extract score
    for line in sentiment:
        term,score = line.split("\t")
        scores[term] = int(score)
      
    for line in tweet:
        tweets = json.loads(line)
        current_sentiment = 0
        if 'text' in tweets:
            tweet_text = tweets['text'].lower().strip()
            words = tweet_text.split()
            for word in words:
                #print word
                if scores.has_key(word):
                    current_sentiment = current_sentiment + scores[word]
                else:
                    current_sentiment +=0
                    if unscored_words.has_key(word):
                        pass
                    else:
                        #print "Added key", word
                        unscored_words[word] = 0
            for word in words:
                if unscored_words.has_key(word):
                    #print word, "current_sentiment", current_sentiment
                    unscored_words[word] += float(current_sentiment)
    #print len(unscored_words), "size"
    for word in unscored_words:
        print (word.encode('utf-8').replace(",","-")), unscored_words[word]
    #print unscored_words

    return     

if __name__ == '__main__':
    main()
