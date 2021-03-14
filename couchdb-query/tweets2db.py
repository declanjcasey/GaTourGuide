import couchdb
import json
import pandas as pd

k = open("../secrets/credentials.json", "r")
keys = json.load(k)

user = keys["DB_USER"]
pwd = keys["DB_PW"]
db = keys["DB_NAME"]

# some lines have more than 4 fields, how to fix this?
data = pd.read_csv("")

# pesudocode-ish doc creation
log = # whatever csv contains logged data
doc = {
    "msg": row[msg] # pull message from log
    "t_id": row[t_id] # pull t_id from log
    "lang": row[lang] # pull language from log
    "location": row[location] # pull location from log
}

db.save(doc)


# class TweetStore(object):
    
#     def __init__(self, dbname, url='http://127.0.0.1:5984/'):
#         try:
#             self.server = couchdb.Server(url=url)
#             self.db = self.server.create(dbname)
#             self._create_views()
#         except couchdb.http.PreconditionFailed:
#             self.db = self.server[dbname]

#     def _create_views(self):
#         count_map = 'function(doc) { emit(doc.id, 1); }'
#         count_reduce = 'function(keys, values) { return sum(values); }'
#         view = couchdb.design.ViewDefinition('twitter', 
#                                             'count_tweets', 
#                                             count_map, 
#                                             reduce_fun=count_reduce)
#         view.sync(self.db)

#         get_tweets = 
#         'function(doc) { emit(("0000000000000000000"+doc.id).slice(-19), doc); }'
#         view = couchdb.design.ViewDefinition('twitter', 'get_tweets', get_tweets)
#         view.sync(self.db)