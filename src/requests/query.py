import requests
import json
import couchdb
from time import sleep

k = open("GaTourGuide/secrets/credentials.json", "r")
#k = open("../GaTourGuide/secrets/credentials.json", "r")
keys = json.load(k)

TOKEN = keys["FULL_ARCHIVE_BEARER"]
user = keys["DB_USER"]
pwd = keys["DB_PWD"]
db = keys["DB_NAME"]
op = "_bulk_docs"
host = "127.0.0.1:5984"

get_headers = {
    "content-type":"application/json",
    "authorization": f"Bearer {TOKEN}"
}

post_headers = {
    "accept":"application/json",
    "content-type":"application/json",
    "referer":f"{host}"
}

#page = "" # None

#while page is not None:
    # Archive references
#    query = {
#        "query":"lang:es has:geo gatos",
#        "max_results":500,
#        "next_token":None
        # "fromDate":"201402010000",
        # "toDate":"201902282359"
#    }

    # GET REQUESTS

#    get_response = requests.get(
#        "https://api.twitter.com/2/tweets/search/all",
#        headers = get_headers,
#        params = query
#    )

#    get_results = json.loads(get_response.text)

#    page = get_results['meta']['next_token']

#    print(page)

# for data in get_results["data"]:
#     print("Tweet ID:", data['id'])
#     print("Message:", data['text'])
#     print("\n")

#print(get_results) # says 'data' instead of 'docs'

def make_bulk_doc(tweets):
    bulk = {
        "docs":tweets
    }
    return json.dumps(bulk)

def make_post_request(docs):
    post_response = requests.post(
        f"http://{user}:{pwd}@{host}/{db}/{op}",
        headers=post_headers,
        data=docs
    )

    print(post_response.text)

def get_full_place_name(data, id):
    # Look at each dictionary
    for d in data:
        try:
            # Try to match the data in the `id` key
            val = list(d.keys())[list(d.values()).index(id)]
            # If matches, get the `full_name` key
            if val: return d['full_name']
        except ValueError:
            # If it's not there, it b0rkz
            pass

def get_pages(page_token=None):
    global get_headers
    sleep(5) # wtf
    query = {
        "query":"lang:es has:geo gato place_country:ES ",
        "expansions":"geo.place_id",
        "tweet.fields":"geo",
        "place.fields":"contained_within",
        "max_results": 10,
        "next_token":page_token,
        #"start_date":,
        #"end_date":
    }
    get_response = requests.get(
        "https://api.twitter.com/2/tweets/search/all",
        headers=get_headers,
        params=query
    )

    data = json.loads(get_response.text)
    # tweets = {
    #     'data': data['data'],
    #     'includes': data['includes']
    # }
    tweets = data['data']
    locations = data['includes']['places']
    for tweet in tweets:
        idx = tweets.index(tweet)
        # A bit long, but you get the idea; cross-reference IDs and results to make sure
        tweet['geo']['full_name'] = get_full_place_name(locations,tweet['geo']['place_id'])
        tweets[idx] = tweet
    print(tweets)

    make_post_request(
       make_bulk_doc(tweets)
    )
    print(make_bulk_doc(tweets))
    next_page = data['meta']['next_token']
    if next_page is not None: # likely not best end condition
        get_pages(next_page)

get_pages()

# TODO:
# 1. Get an accredited list of the most commonly visited cities in Spain.
# 2. Add tweets with that city as location into DB.
