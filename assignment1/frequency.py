

import sys
import json

def main():
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    #term_score(sent_file,tweet_file)
    term_frequency(tweet_file)
    
    
#I can divide the task into two parts
'''
1: Calculate the frequency of all terms, basically everything
2: Use a dictionary to keep track of the value of each
3: Last, use the formula and modify the dictionary value and output to stdout
'''

def term_frequency(tweet):
    terms = dict()
    count = float(0)
    #print "Function is running"
    for line in tweet:
        tweets = json.loads(line)
        if 'text' in tweets:
            tweet_text = tweets['text'].lower().strip()
            words = tweet_text.split()
            for word in words:
                #It means the dictionary has the term, increment
                if terms.has_key(word):
                    terms[word] +=1
                    count = count + 1
                else:
                    terms[word] = 1
                    count = count + 1
                    
    for i in terms:
        terms[i] = terms[i]/(count)
        print i, terms[i]
        
main()