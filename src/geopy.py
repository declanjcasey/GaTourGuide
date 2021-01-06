import tweepy
from geopy.geocoders import Nominatim

GEOLOCATOR = Nominatim(user_agent="GatourGuide")

def calcCoordinates(self, location):
    coordinates = location.latitude, location.longitude
    return coordinates


# Other functions to add: calcDistance
