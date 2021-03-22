#!/usr/bin/env python

import argparse, cgitb, getopt, json, tweepy, re, sys, yaml
from chardet import detect

#with open("credentials.json") as f:
#  contents = f.read()

#keys = json.loads(contents)

f = open("credentials.json","r")
keys = json.load(f)


CONSUMER_KEY = keys["CONSUMER_KEY"]
CONSUMER_SECRET = keys["CONSUMER_SECRET"]
ACCESS_KEY = keys["ACCESS_KEY"]
ACCESS_SECRET = keys["ACCESS_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

hashtag = ""
hashtags = []

class hashbot():

  def start(self):
    try:
      tweepy.streamListener = processTweets()
      twitterStream = tweepy.Stream(auth, listener=processTweets())
      twitterStream.filter(track=[hashtag])
    except tweepy.TweepError as t:
      print(t)
      time.sleep(60)
    except Exception as e:
      print(sys.exc_info())
    #   time.sleep(60)

class processTweets(tweepy.StreamListener):

  def on_data(self,data):
    row = ""
    decoded = json.loads(data)
    if 'text' in decoded:
      message = decoded['text'].lower()
      encoding = lambda message: detect(message)['encoding']
      for tag in hashtags:
        if tag in message and not "@" in message and tag.lstrip() != "" and tag.rstrip() != "":
          row = tag + "\t" + message
          self.update_log(row)

  def on_error(self,status):
    return false

  def update_log(self,row):
    # RLY BAD LOGGING THING
    try:
      file = '-'.join(hashtags)+"-log.csv"
      with open(file,'a') as f:
        f.write(row+"\n")
    except Exception as e:
      print("Exception at update_status: " + str(e))

if __name__ == '__main__':

  parser = argparse.ArgumentParser(description='Hashtag expression; separate multiples by comma.')
  parser.add_argument('tags',metavar="tags",type=str)
  args = parser.parse_args()

  hashtag = args.tags
  hashtags = hashtag.split(",")

  print("Starting search for: " + hashtag)

  hashbot().start()
