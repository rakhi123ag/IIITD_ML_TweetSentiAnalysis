from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['tweetsample']
posts = db.tweets

for line in open('../1.FetchTweetsFromTwitterStream/textpartoftweet.txt', 'r'):
	post_data = {'tweet': line}
	result = posts.insert_one(post_data)