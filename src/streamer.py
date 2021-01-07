import csv, json, tweepy, sys
#import spacy

#from geopy.geocoders import Nominatim
#from tweepy.streaming import StreamListener
#from tweepy import OAuthHandler
#from tweepy import Stream
#from textblob import TextBlob

k = open("../secrets/credentials.json", "r")
keys = json.load(k)

CONSUMER_KEY = keys["CONSUMER_KEY"]
CONSUMER_SECRET = keys["CONSUMER_SECRET"]
ACCESS_KEY = keys["ACCESS_KEY"]
ACCESS_SECRET = keys["ACCESS_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# geopy methods, where to incorporate?
#geolocator = Nominatim(user_agent="GatourGuide")
#location = geolocator.geocode("La Sagrada Familia")
#print(location.latitude, location.longitude)

# tweets = api.search('La Sagrada Familia') # where to implement this

#terms = ["Sagrada Familia","sagrada familia","Sagrada familia","sagrada Familia"]
terms = ["guggenheim","Guggenheim"]

class hashbot():

    def start(self):
        try:
            tweepy.StreamListener = processTweets()
            twitterStream = tweepy.Stream(auth, listener=processTweets())
            twitterStream.filter(languages=["es"],track=[','.join(terms)]) # does this search or filter hastags?
        except tweepy.TweepError as t:
            print(t)
            time.sleep(60)
        except Exception as e:
            print(sys.exc_info())

class processTweets(tweepy.StreamListener):

    def on_data(self, data):
        decoded = json.loads(data)
        print(decoded)
        msg = decoded['text'].replace("\n"," ")
        t_id = decoded['id_str']
        lang = decoded['lang']
        row = '\t'.join([msg, t_id, lang]) # does this join the whole
        self.update_log(row)

    # unnecesary?
    def on_error(self, status):
        return false

    def update_log(self, row):
        # how to improve this
        try:
            file = terms[0] + "-TestTweets.csv"
            with open(file,'a') as f:
                f.write(row+"\n")
        except Exception as e:
            print("Exception at update_status: " +str(e))

if __name__ == "__main__":
    hashbot().start()

