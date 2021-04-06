# import the modules
import praw
import pandas as pd
from authenticate import redditAuthenticate
from get_all_tickers import get_tickers as gt
  
# creating an authorized reddit instance 
reddit = redditAuthenticate()

#get tickers and remove duplicates (listed on multiple exchanges?)
tickers = list(dict.fromkeys(gt.get_tickers()))

#WSB lingo
lingo = ['I', 'A', 'DD', 'WSB', 'LOL', 'IV', 'IP', 'YOLO', 'TIL', 'EDIT', 'OTM', 'GOT', 'IPO', 'WTF', 'ATH']

#ignore WSB lingo
filteredTickers = [ele for ele in tickers if ele not in lingo]

#fetch daily discussion thread
submission = next(reddit.subreddit("wallstreetbets").search("title:Daily Discussion Thread for AND flair:Daily Discussion", time_filter='day'))
print (submission.title)

#add limit=X to scrap first X pages only
submission.comments.replace_more()

#output array
countsum=[0]*len(filteredTickers)

#compare comment text with ticker list and count
comments = submission.comments.list()
for comment in comments:
    #ignore downvoted posts
    if comment.score > -1:
        #print(comment.body)
        for i, ticker in enumerate(filteredTickers):
            #match tickers with whole words only (in case that body contains "ASO" don't match "A" but match "ASO")
            if ticker in (comment.body).split():
                countsum[i]=countsum[i]+1

output=pd.DataFrame(data={'Ticker': filteredTickers, 'Count': countsum})

print(output[output['Count']>10].sort_values(by='Count', ascending=False))







