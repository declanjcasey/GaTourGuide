import requests
import json
import couchdb

k = open("GaTourGuide/secrets/credentials.json", "r")
keys = json.load(k)

user = keys["DB_USER"]
pwd = keys["DB_PWD"]
db = keys["DB_NAME"]
op = "_bulk_docs"
host = "127.0.0.1:5984"

couch = couchdb.Server('http://declan:d3cl4nsh0us3@127.0.0.1:5984')


headers = {
    "accept":"application/json",
    "content-type":"application/json",
    "referer":f"{host}"
}

# _find op

#query = {
#    "selector": {
#        "location": {
#            "$regex":"(?i)madrid"
#        }
#    }
#}

file = open("reducer/gatos-reduced.json","r")
query = json.load(file)

# cURL command substitute

response = requests.post(
    f"http://{user}:{pwd}@{host}/{db}/{op}",
    headers=headers, # <-- -H
    data=json.dumps(query) # <-- -d
)

# Prints what returns from the request
print(response.text)

# Result of _find op

# Now, for the part we care about

#results = json.loads(response.text)

#for doc in results["docs"]:
#    print(f"t_id:\t{doc['t_id']}")
#    print(f"msg:\t{doc['msg']}")
#    print(f"loc:\t{doc['location']}")
