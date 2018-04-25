from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='c3c2e7d96c7941f79aa42422faf82baa')
sourceFile=open('news.txt', 'w')
# /v2/top-headlines
sources=['the-hindu','the-times-of-india','google-news-in','bbc-news']
titles=[]
for src in sources:
	news = newsapi.get_everything(q='trump',
                                          sources=src,
                                          #category='business',
                                          #language='en',
                                          #country='us'
										  )

										  
	for arti in news['articles']:
		titles.append(arti['title'])
												
for t in titles:
	sourceFile.write("%s\n" % t)


										 
