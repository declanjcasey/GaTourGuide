env_name: `dev`
bearer_token: `AAAAAAAAAAAAAAAAAAAAANaMKwEAAAAAkS5IugPiUSkPuwZT2fuiD5LHGb8%3DNmRqWOeUujbX72miuSpUW19HBeDoAJ8ozjRuPPdoCZOgw8PTck`
```
curl --request POST \
  --url https://api.twitter.com/1.1/tweets/search/fullarchive/dev.json \
  --header 'authorization: Bearer AAAAAAAAAAAAAAAAAAAAANaMKwEAAAAABYJy6efV7KEojGYLPK9%2BuEXnFyk%3Da3Qb8sopPKwVzil7hgMfpqnEnsHDQfSVKYwcL5D7rfhnO8RzeC' \
  --header 'content-type: application/json' \
  --data '{
                "query":"lang:es",
                "keyword":"La Sagrada Familia",
                "maxResults": "10000",
                "fromDate":"201402010000",  
                "toDate":"201902282359"
                }'

```              