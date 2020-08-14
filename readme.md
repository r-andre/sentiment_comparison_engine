# TWEET SENTIMENT COMPARISON ENGINE V0.1

## Description

This script collects two sets of Tweets using the Twitter API based on two selected keywords, and scores the average sentiment of both sets of tweets, in order to evaluate which of the two topics/names/words the (Twitter) world prefers.

## How it works

First, the script asks for two keywords to collect two sets of Tweets using Tweepy with the personal Twitter API consumer key and secret. Then the Tweet messages are cleaned using Preprocessor and their sentiment is scored using TextBlob. Lastly, the average sentiment score of the two sets of Tweets are compared.

## Dependencies

  * `tweepy`
  * `textblob`
  * `preprocessor`

The script also requires a seperate `keys.py` module (in the same folder) that contains the Twitter API consumer key and secret as variables (string type) `consumer_key` and `consumer_secret`.