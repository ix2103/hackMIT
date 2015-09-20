# -*- coding: utf-8 -*-
import indicoio
from TwitterSearch import *
import json

LANGUAGE = 'en'
MAXTERM = 20

indicoio.config.api_key = '386f1e0430ab901fca510dc0084be94a'

def search(searchTerm,lang='en'):
    try:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords([searchTerm]) # let's define all words we would like to have a look for
        tso.set_language(lang) # we want to see German tweets only
        tso.set_include_entities(True) 
    
        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
        consumer_key = 'IG4yEQ3u1Oe8EJyNfU7U1p1W0',
        consumer_secret = 'dLVSRDi1ctXBlFFMQxOmqm3qIT5cxiQfULJghz2tpU0Cpl2yPz',
        access_token = '2573923417-3K4BPzgJutAflbwQ8fGR3ePQFwQbhXUKEKhmyQ4',
        access_token_secret = 'wQt2i4ViwO0GzWDde7x5CNRQpiAun8w6Iua4ZYVqwg7wJ'
        )
    
        return ts.search_tweets_iterable(tso)
    
    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print e
        return -1
    
    
def toDict(tweets, maxNum='20'):
    i = 0
    myDict={}
    for tweet in tweets:
        if i<maxNum:
            if tweet['text'] in myDict:
                entry = myDict[tweet['text']]
                if 'coordinates' in tweet and tweet['coordinates']!=None:
                    entry['location'].append(tweet['coordinates'])
                    i+=1
                elif tweet['user']['location']!='':
                    entry['location'].append(tweet['user']['location'])
                    i+=1
            else: #create new entry w/ sentiment + location
                if 'coordinates' in tweet and tweet['coordinates']!=None:
                    myDict[tweet['text']]={'sentiment':indicoio.sentiment(tweet['text']),'location':[tweet['coordinates']]}
                    i+=1
                elif tweet['user']['location']!='':
                    myDict[tweet['text']]={'sentiment':indicoio.sentiment(tweet['text']),'location':[tweet['user']['location']]}
                    i+=1
        else:
            break
    return myDict


def getJSON(searchterm,language='en',maxterms='20'):  
    return json.dumps(toDict(search(searchterm,language),maxterms))
