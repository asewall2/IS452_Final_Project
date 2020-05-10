# 1.) importing all the modules I need to get this code to work
import tweepy
import json
import pathlib

# 2.) creating a dictionary of variables to import the keys for my API. Code is borrowed from Beyond Data Science blog post.
twitter_keys = {
        'consumer_key':        '___YOUR_KEY___',
        'consumer_secret':     '___YOUR_SECRET___',
        'access_token_key':    '___YOUR_KEY___',
        'access_token_secret': '___YOUR_SECRET___'
    }

# 3.) using tweepy to establish a connection with the API. Code adapted from Beyond Data Science blog post.
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

# 4.) calling on the API
api = tweepy.API(auth)

# 5.) using the api call to grab tweets from my main timeline
public_tweets = api.home_timeline()

# 6.) exporting the messy json data into a list and exporting it into a json file where tweet data is clumped together in a
# human readable format
clusters = []
for tweet in public_tweets:
    data = tweet._json
    clusters.append(data)
print(clusters)

# 7.) export the data to a json file, adapted from the week 3 notes Elizabeth sent me about writing out json files
with open(pathlib.Path('jsontweetchunks.json'),'w') as jout:
     json.dump(clusters, jout, indent= 4)
