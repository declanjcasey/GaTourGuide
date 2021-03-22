from Contextualizer import Contextualizer
from Tweet import Tweet
import pandas as pd

class Tweet:

with open('tweet.json') as f:
  data = json.load(f)

    def __init__(self, tweet):
        # All the tweet fields we care about
        self.fields = {}
        # Immediately parse
        self.tweet = tweet
        self.tweet = self.parse()

    def parse(self):
        fields = self.tweet.split("\t")
        self.fields['msg'] = fields[0]
        self.fields['t_id'] = fields[1]
        self.fields['context'] = Contextualizer(fields[0])
