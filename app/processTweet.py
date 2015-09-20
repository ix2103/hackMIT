#!flask/bin/python3
# -*- coding: utf-8 -*-
import indicoio
from TwitterSearch import *
import json

LANGUAGE = 'en'
MAXTERM = 20
INDICO_KEY='386f1e0430ab901fca510dc0084be94a'
TWIT_CONSUMER_KEY='IG4yEQ3u1Oe8EJyNfU7U1p1W0'
TWIT_CONSUMER_SECRET='dLVSRDi1ctXBlFFMQxOmqm3qIT5cxiQfULJghz2tpU0Cpl2yPz'
TWIT_ACCESS_TOKEN='2573923417-3K4BPzgJutAflbwQ8fGR3ePQFwQbhXUKEKhmyQ4'
TWIT_ACCESS_SECRET='wQt2i4ViwO0GzWDde7x5CNRQpiAun8w6Iua4ZYVqwg7wJ'


indicoio.config.api_key = INDICO_KEY

"""
THE ONLY METHOD YOU SHOULD BE CALLING
This returns a JSON with the tweet, sentiment, and location(s) of the tweets.
"""
def getJSON(searchterm,language=LANGUAGE,maxterms=MAXTERM):  
    return json.dumps(toDict(search(searchterm,language),maxterms))

#all helper methods below

"""
Takes a search term and returns an iterable with tweets related to the search term
"""
def search(searchTerm,lang=LANGUAGE):
    try:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords([searchTerm]) # let's define all words we would like to have a look for
        tso.set_language(lang) # we want to see German tweets only
        tso.set_include_entities(True) 
    
        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
        consumer_key = TWIT_CONSUMER_KEY,
        consumer_secret = TWIT_CONSUMER_SECRET,
        access_token = TWIT_ACCESS_TOKEN,
        access_token_secret = TWIT_ACCESS_SECRET
        )
    
        return ts.search_tweets_iterable(tso)
    
    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print (e)
        return -1
    

"""
Takes a tweet iterable and processes maxNum of the tweets into format we want
"""
def toDict(tweets, maxNum=MAXTERM):
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
