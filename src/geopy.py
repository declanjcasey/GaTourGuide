import tweepy
from geopy.geocoders import Nominatim

GEOLOCATOR = Nominatim(user_agent="GatourGuide")

def calcCoordinates(self, location):
    coordinates = location.latitude, location.longitude
    return coordinates


# method to search for tweets by coordinates
# needs implementation in streamer
def tweetsByCoordinates(self, location):
    coordinates = calcCoordinates(location)
    


# Other functions to add: calcDistance
