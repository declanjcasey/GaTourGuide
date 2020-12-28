import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# from textblob import TextBlob
#
# import spacy
#
# text = """
# Dave watched as the forest burned up on the hill,
# only a few miles from his house. The car had
# been hastily packed and Marta was inside trying to round
# up the last of the pets. "Where could she be?" he wondered
# as he continued to wait for Marta to appear with the pets.
# """
#
# # Load english model, tokenize the text with the nlp constructor
# nlp = spacy.load("en_core_web_sm")
# doc = nlp(text)
# token_list = [token for token in doc]
#
# # remove stop words
# filtered_tokens = [token for token in doc if not token.is_stop]
#
# # readable list of tokens and lemmas using .lemma_
# lemmas = [
#     f"Token: {token}, lemma: {token.lemma_}"
#     for token in filtered_tokens
# ]

consumer_key = "jmDsjxJ2BDxSW4asJUBf8ATGr"
consumer_secret = "SDUe0DszTpoqkC0ofivJXaZyIrnZ9gXJ93MPL4JS9A96jDJE5F"
access_token = "1286383020497342464-QRnWtkTBfu7ndyPhOvYzfWiWYn7Qzd"
access_token_secret = "UTDhI3gJN84CMGOSRc9q1krMQsSxLL6Dyu6BMWbdOl3z"

class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])

# Pipe collected data into a txt
# python twitter_streaming.py > twitter_data.txt


# # add keys once access is obtained
# consumer_key = "z4zfC23il2tNXGQjZK0Ln3p9az"
# consumer_secret = "zeYOeM2wSC9a2shvIPChjQJm58i9CaarnH05bMGInMvhSL9AhM"
# access_token = "1286383020497342464-1FcqvM3lIWtvZzxlHHV2B2zdsoNMpp"
# access_token_secret = "emUCFINqs6ssVn8JxYrXZA2y3wSbNNDWoe5pldmmFDZZf"
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)
#
# # only manually enter tweets in at the moment
# public_tweets = api.search('La Sagrada Familia')
#
# for tweet in public_tweets:
#     print(tweet.text)
#     analysis = TextBlob(tweet.text)
#     print(analysis.sentiment)
#
# # now begin using spacy rather than textblob
