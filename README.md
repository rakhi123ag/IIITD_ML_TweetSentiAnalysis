I developed this project to do sentiment analysis on twitter dataset and news dataset of same entity(Name,location).
I used python for doing data fetch,pre-processing and sentiment analsysis.

In this project following python packages are used;
 tweepy
 
 json
 
 pymongo
 
 newsapi_python
 
 re
 
 textblob
 
 
 
STEP 1: First I created a script that fetch random tweets from twitter. 

STEP 2: Object that is recevied from twitter stream is a JSON, and contain tweet related to create,delete etc. I only require created tweets,so I writes an another 
scrip that will fetech tweet text from json from only created type tweets.I only fetech 10K tweets.

STEP 3: I used mongodb to store tweets(Original db size is more than 100MB so I truncate records so can push on git hub).

STEP 4: I assume that the most frequest name entity is donald trump, with this assumption I fetech related news from other sources and store them in text file.

STEP 5: Finally I use textblob python package to do sentiment analysis.    

