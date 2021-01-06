
import csv, json, tweepy, spacy

from geopy.geocoders import Nominatim
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob

k = open("credentials.json", "r")
keys = json.load(k)

CONSUMER_KEY = keys["CONSUMER_KEY"]
CONSUMER_SECRET = keys["CONSUMER_SECRET"]
ACCESS_KEY = keys["ACCESS_KEY"]
ACCESS_SECRET = keys["ACCESS_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# geopy methods, where to incorporate?
geolocator = Nominatim(user_agent="GatourGuide")
location = geolocator.geocode("La Sagrada Familia")
print(location.latitude, location.longitude)

# tweets = api.search('La Sagrada Familia') # where to implement this

class hashbot():

    def start(self):
        try:
            tweepy.StreamListener = processTweets()
            twitterStream = tweepy.Stream(auth, listener=processTweets)
            # twitterStream.filter(track=[hashtag]) # does this search or filter hastags?
        except tweepy.TweepError as t:
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
