from textblob import TextBlob
import re



sentiments=['neutral','positive','negative']

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

	
def analize_sentiment(tweet):
    '''
    Utility function to classify the polarity of a tweet
    using textblob.
    '''
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1
		
		

if __name__=='__main__':
	print('--'*25,'Sentiment analysis of news','--'*25) 
	for line in open('news.txt', 'r'):
		sentiment=analize_sentiment(line)
		print(line + '' +'-->'+ '' +sentiments[sentiment]) 
		
		print('--'*25,'Sentiment analysis of tweets','--'*25) 
	for line in open('tweets.txt', 'r'):
		sentiment=analize_sentiment(line)
		print(line + '' +'-->'+ '' +sentiments[sentiment]) 	