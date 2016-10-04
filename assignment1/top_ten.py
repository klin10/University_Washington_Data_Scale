import sys
import json
import operator

def main():
    tweet_file = open(sys.argv[1])
    top_ten(tweet_file)
    
def top_ten(tweet_file):
    hashtag_dictionary = dict()
    #print "top ten"
    for line in tweet_file:
        #print line
        tweets=json.loads(line)
        #Entities holds the hashtag
        if 'entities' in tweets.keys():
            entities = tweets['entities']
            #Tags it is a property under entities
            tags = entities['hashtags']
            for tag in tags:
                #Extract the text of the hashtag and put it in dictionary
                text = tag['text']
                #print text
                if text in hashtag_dictionary.keys():
                    hashtag_dictionary[text] = hashtag_dictionary[text] + 1
                else:
                    hashtag_dictionary[text] = 1
    #len(hash)
    #After tags are being extracted, print the top ten
    hashtags = sorted(hashtag_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    #print hashtags 
    for hashtag in hashtags[:10]:
        #Print the current hashtag and the value stored in the dictionary
        print hashtag[0].encode('utf-8')  + " " + str(hashtag[1])
        #print (i.encode('utf-8').replace(",","-"))
        #print (i)
        
main()