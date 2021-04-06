# wsbscraper
Scraps daily discussion thread of r/wallstreetbets and returns most discussed stocks


## Usage
add file authenticate.py to main dir
```python
import praw

def redditAuthenticate():
    return praw.Reddit(client_id ='',
                         client_secret='',
                         username = '',
                         password = '',
                         user_agent='')
```
