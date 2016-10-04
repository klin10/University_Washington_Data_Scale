import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw() avoid std mismatch
    #dictionary(sys.argv[1])
    #importjson(sys.argv[2])
    #lines(sent_file)
    #lines(tweet_file)
    get_score(sent_file, tweet_file)

def get_score(sentiment, tweet):
    #create dictionary to hold all score
    scores = dict()
    #Extract score
    for line in sentiment:
        term,score = line.split("\t")
        scores[term] = int(score)
    #Extract tweets and analyze the sentiment of each
    for line in tweet:
        tweets = json.loads(line)
        current_sentiment = 0
        if 'text' in tweets:
            tweet_text = tweets['text'].lower().strip()
            words = tweet_text.split()
            for word in words:
                if scores.has_key(word):
                    current_sentiment = current_sentiment + scores[word]
                else:
                    current_sentiment += 0
        print current_sentiment
    
    
def importjson(file):

    data = []
    with open(file) as f:
        for line in f:
            data = json.loads(line);
        print data[u'text']
    
def dictionary(file):
        afinnfile = open(file)
        scores = {} #dictionary
        for line in afinnfile:
            terms, score = line.split ("\t")
            scores[terms] = int(score)
        #print scores.items()

if __name__ == '__main__':
    main()
