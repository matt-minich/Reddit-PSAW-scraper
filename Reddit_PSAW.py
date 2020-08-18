from psaw import PushshiftAPI
import csv
import datetime as dt

api = PushshiftAPI()

start_epoch=int(dt.datetime(2012, 11,9).timestamp())

corpus = list(api.search_submissions(after = start_epoch,
                                    subreddit = 'trees',
                                     limit = None))

with open('D:/CAMER/newtrees.csv','w', encoding = 'utf-8') as csvfile:
    fieldnames = ['id','title','author','original content','selfpost','stickied','selftext','comment forest','time created','locked','number of comments','NSFW','permalink','score','upvote ratio','url']
    filewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
    filewriter.writeheader()

    for i in corpus:
        filewriter.writerow({'id': i.id,
                             'title': i.title,
                            'author': i.author,
                            'original content': i.is_original_content,
                            'selfpost': i.is_self,
                            'time created': i.created_utc,
                            'stickied': i.stickied,
                            'locked': i.locked,
                            'NSFW': i.over_18,
                            'selftext': i.selftext,
                            #'comment forest': cache,
                            'number of comments': i.num_comments,
                            'score': i.score,
                            'upvote ratio': i.upvote_ratio,
                            'permalink': i.permalink,
                            'url': i.url})

print ('We did it!')
