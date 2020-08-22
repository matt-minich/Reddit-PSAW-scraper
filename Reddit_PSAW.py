from psaw import PushshiftAPI
import csv
import datetime as dt


api = PushshiftAPI()

start_epoch=int(dt.datetime(2018, 1,1).timestamp())
end_epoch=int(dt.datetime(2019,1,1).timestamp())

subreddit = input('Which subreddit would you like to scrape? ')


with open('D:/CAMER/%s.csv' % subreddit, 'w', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'title', 'author', 'original content', 'selfpost', 'stickied', 'selftext',
                  'time created', 'locked', 'number of comments', 'NSFW', 'permalink', 'score',
                  'url']
    filewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    filewriter.writeheader()

    for i in api.search_submissions(after=start_epoch,
                                    before=end_epoch,
                                    subreddit=subreddit,
                                    limit=None):

        if hasattr('i', 'selftext')== True:
            selftext = i.selftext
        else:
            selftext = 'NaN'
        if hasattr('i','is_original_content') == True:
            isic = i.is_original_content
        else:
            isic = 'NaN'

        filewriter.writerow({'id': i.id,
                             'title': i.title,
                            'author': i.author,
                            'original content': isic,
                            'selfpost': i.is_self,
                            'time created': i.created_utc,
                            'stickied': i.stickied,
                            'locked': i.locked,
                            'NSFW': i.over_18,
                            'selftext': selftext,
                            'number of comments': i.num_comments,
                            'score': i.score,
                            'permalink': i.permalink,
                            'url': i.url})

print ('We did it!')
