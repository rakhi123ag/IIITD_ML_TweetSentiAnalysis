import json
from pprint import pprint

tweets = []
i=1
count=0
sourceFile=open('textpartoftweet.txt', 'w')
for line in open('tweets.json', 'r'):
	#print(line)
	if i%2==1 and 'created_at' in json.loads(line):
		#print(json.loads(line)['text'])
		tweets.append(json.loads(line)['text'])
		count+=1
	i=i+1
	if count>=10000:
		break
#sourceFile.write("\n".join(tweets))
for item in tweets:
  sourceFile.write("%s\n" % item.encode("utf-8"))