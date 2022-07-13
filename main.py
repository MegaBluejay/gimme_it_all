#!/usr/bin/env python

import csv
import sys

from more_itertools import peekable
from praw import Reddit
from psaw import PushshiftAPI
from tqdm import tqdm

api = PushshiftAPI(Reddit())

posts = peekable(api.search_submissions(subreddit=sys.argv[1]))
posts.peek()
total = api.metadata_["total_results"]
upvoted = (post for post in tqdm(posts, total=total) if post.likes)

writer = csv.writer(sys.stdout, lineterminator="\n")
for post in tqdm(upvoted, bar_format="{n_fmt} found"):
    writer.writerow([post.title, post.url])
