#!/usr/bin/env python
# -*- coding: utf-8 -*-

###########################################
# TWEETS SENTIMENT COMPARISON ENGINE V0.1 #
###########################################

import tweepy
from textblob import TextBlob
import preprocessor
import statistics
from typing import List

# The key module only contains the personal consumer key and secret (both
# strings) to access the Twitter api with tweepy:
from keys import consumer_key, consumer_secret

# Authenticating Twitter access:
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

# Function to collect Tweets based on keyword:
def get_tweets(keyword: str) -> List[str]:
    '''Collects a set number of Tweets containing the specified keyword and
    stores messages and authors in a list.'''
    all_tweets = []
    twitter = tweepy.Cursor(api.search, q=keyword, tweet_mode='extended',
                            lang='en').items(10)
    for tweet in twitter:
        all_tweets.append(tweet.full_text)
    return all_tweets

# Function to clean text of Tweets:
def clean_tweets(all_tweets: List[str]) -> List[str]:
    '''Cleans the text of all input Tweets (e.g. removing author names,
    hyperlinks, etc.) and returns a list of clean Tweet messages'''
    tweets_clean = []
    for tweet in all_tweets:
        tweets_clean.append(preprocessor.clean(tweet))
    return tweets_clean

# Function to score the sentiment of Tweets:
def get_sentiment(all_tweets: List[str]) -> List[float]:
    '''Generates sentiment scores for a list of clean Tweet messages.'''
    sentiment_scores = []
    for tweet in all_tweets:
        blob = TextBlob(tweet)
        sentiment_scores.append(blob.sentiment.polarity)
    return sentiment_scores

# Function to run the engine and calculate the sentiment average of Tweets:
def generate_average_sentiment_score(keyword: str) -> int:
    '''Calculates and returns the average sentiment score of multiple Tweets
    containing a specified keyword.'''
    tweets = get_tweets(keyword)
    tweets_clean = clean_tweets(tweets)
    sentiment_scores = get_sentiment(tweets_clean)
    average_score = statistics.mean(sentiment_scores)
    return average_score

# Starting the Tweets sentiment comparison engine:
if __name__ == '__main__':
    # Acquiring the first keyword:
    print("What does the world prefer? (Please enter a word:)")
    first_thing = input()
    # Acquiring the second keyword:
    print("\n...or... (please enter another word:)")
    second_thing = input()
    print("")
    # Trying to collect Tweets:
    try:
        # Generating the average sentiment score for the first keyword:
        first_score = generate_average_sentiment_score(first_thing)
        # Generating the average sentiment score for the second keyword:
        second_score = generate_average_sentiment_score(second_thing)
        # Comparing both sentiment scores and printing the result:
        if (first_score > second_score):
            print("The world prefers " + first_thing + " over "
                  + second_thing + ".")
        elif (first_score < second_score):
            print("The world prefers " + second_thing + " over "
                  + first_thing + ".")
        else:
            print("The world has no preference between " + first_thing
                   + " and " + second_thing + ".")
    # Returing an error if no Tweets were collected:
    except:
        print("Error, no Tweets were found!")
