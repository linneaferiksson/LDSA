#!/usr/bin/env python
"""mapper.py"""

import sys
import json
import re

# the input comes from the standard input (STDIN)
for tweet in sys.stdin:
    tweet = tweet.strip()
    retweets = re.search(".retweeted_status.", tweet)
    if tweet and not retweets:
        tweetDict = json.loads(tweet)
        words = tweetDict["text"].split()
        print('%s\t%s' % ("uniquetweet", 1))
        for word in words:
            word = word.lower()
            if word in ["han", "hon", "hen", "den", "det", "denne", "denna"]:
                print ('%s\t%s' % (word, 1))