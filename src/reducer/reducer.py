import json

def rt_info(doc):
    info = {
        "op":None,
        "time":None,
    }
    try:
        info["op"] = doc["retweeted_status"]["user"]["screen_name"]
    except KeyError:
        pass
    return info

file = open("gatos.json","r")
data = json.load(file)

condensed = {
    "docs":[]
}

for doc in data["docs"]:
    print(rt_info(doc))
    record = {
        "user":doc["user"]["screen_name"],
        "content":{
            "msg":doc["text"]
        }
    }
    condensed["docs"].append(record)

data = json.dumps(condensed)

with open("gatos-reduced.json","w") as o:
    o.write(data)
