
import csv
import json
import tweepy
import spacy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob

# with open('keys.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     for row in csv_reader:
#         print(row)

    # CONSUMER_KEY = csv_reader[0]
    # CONSUMER_SECRET = csv_reader[1]
    # ACCESS_KEY = csv_reader[2]
    # ACCESS_SECRET = csv_reader[3]

# CONSUMER_KEY = keys[0]
CONSUMER_KEY = "jmDsjxJ2BDxSW4asJUBf8ATGr"
CONSUMER_SECRET = "SDUe0DszTpoqkC0ofivJXaZyIrnZ9gXJ93MPL4JS9A96jDJE5F"
ACCESS_KEY = "1286383020497342464-Ng02IUfTRfyw9GKRgibnIPJD2Dx7p3"
ACCESS_SECRET = "Z8jDstdpyPzd4oK4PsW2adM9NUfdo2qu2MLqLhFfsjeVe"

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

tweets = api.search('La Sagrada Familia')

class hashbot():

    def start(self):
        try:
            tweepy.StreamListener = processTweets()
            twitterStream = tweepy.Stream(auth, listener=processTweets)
            # twitterStream.filter(track=[hashtag]) # does this search or filter hastags?
        except: tweepy.TweepError as t:
            print(t)
            time.sleep(60)
        except Exception as e:
            print(sys.exc_info())

class processTweets(tweepy.StreamListener):

    def on_data(self, data):
        # data = {}
        data = []
        decoded = json.loads(data)
        row = '\t'.join(data) # does this join the whole

    # unnecesary?
    def on_error(self, status):
        return false

    def update_log(self, row):
        # how to improve this
        try:
            file = '-'.join(tweets)+"tweets.csv"
            with open(file,'a') as f:
                f.write(row+"\n")
            except Exception as e:
                print("Exception at update_status: " +str(e))

if __name_ == "__main__":

    hashbot().start()
