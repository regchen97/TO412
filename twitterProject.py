import tweepy
import pandas as pd
import numpy as np


key = "Pfv5AqNYvf2dpTAqOiJLRXbsk"
secret = "MZ8jQBF39lpukzQw0mCQ2xEIS1M1XdqZIl7V5MsevhspspIFQs"

comps = ["wendys", "burgerking", "mcdonalds", "arbys"]
auth = tweepy.OAuthHandler(key, secret)
api = tweepy.API(auth)
tweets = {}
df = pd.DataFrame(columns = ["text", "created", "re", "fav", "followC", "sn"])

for comp in comps:
    df = pd.DataFrame(columns = ["text", "created", "re", "fav", "followC", "sn"])
    compTweets = tweepy.Cursor(api.user_timeline, comp)
    for page in compTweets.pages():
        for tweet in page:
            #print(tweet.text.rstrip().replace("\n", "").replace(",","").replace("\r",""))
            df = df.append({
                "text": tweet.text.rstrip().replace("\n", "").replace(",","").replace("\r",""),
                "created": tweet.created_at,
                "re": tweet.retweet_count,
                "fav": tweet.favorite_count,
                "followC": tweet.user.followers_count,
                "sn": tweet.user.screen_name
            }, ignore_index=True)

    tweets[comp] = df

#print(tweets["wendys"].to_string())


#tweet.
    #text
    #created_at
    #retwee_count
    #favorite_count
    #user.followers_count
    #user.name.user.screen_name
    #follower