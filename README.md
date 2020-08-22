# Reddit-PSAW-scraper
A simple script that scrapes the Pushshift.io API using PSAW

This script is an adaptation of the <a href: 'https://github.com/matt-minich/Reddit-PRAW-API'>PRAW scraper </a> that can be found in another of my repositories. 
I also relied on the <a href: 'https://pypi.org/project/psaw/'>official PSAW documentation</a> and guidance from the good people at <a href: 'https://www.reddit.com/r/pushshift/'> r/pushshift.</a>

This script allows users to scrape data from an unlimited number of Reddit posts from the pushshift API. Details about Pushshift can be found <a href: 'https://www.aaai.org/ojs/index.php/ICWSM/article/view/7347'>here.</a>
The user will first need to ented a start date and end date for their search on lines 8 and 9(those dates should be between June of 2005 and April of 2019).

Once run, the script will give prompts asking for a subreddit and a number of posts. The subreddit should be entered without special characters (i.e. 'trees', not 'r/trees').
This script is designed to scrape the "hot" posts from the given subreddit (the most upvoted posts recently).

The script will output a .csv file with the name of the requested subreddt (e.g. 'trees.csv'). Each row in the .csv will contain this data for each post: 

id: a numerical ID unique to the post 

title: the title of the post

author: the username of the poster

original content: whether the post has been marked as original content (boolean)

selfpost: whether the post has been marked as a selfpost (boolean)

time created: the time (in epoch) the post was posted 

stickied: whether the post is "stickied" to the top of the subreddit (boolean)

locked: whether the post has been locked by moderators (boolean)

NSFW: whether the post has been marked as containing adult content (boolean)

selftext: the body text of the post (if the post is a selfpost) 

number of comments: the number of comments on the post

score: the post's score (upvotes - downvotes) at the time of scraping

permalink: a direct link to the post

url: the link included in the post or a link to the post itself (if selfpost)
