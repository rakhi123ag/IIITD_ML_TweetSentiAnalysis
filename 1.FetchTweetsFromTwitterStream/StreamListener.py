from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('tweets.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
consumer_key = 'gEZVXTHDof9ejaN8rRsONBJ1c'
consumer_secret = '2iSDwyuZH3wGjRCdmaHi3fC5JMd3fMKkXfd2r5hWjYg88TBQxn'
access_token = '955420251860037632-UHx8pw00UUV8hoEPgI1BLdrFJpeYxGv'
access_secret = '6rOMO8A5R8VlWpjnEENAmkOlNgLnkjGJhLqkTdvL8HltI'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.sample()