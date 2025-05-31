# Insufficient session expiration in the **com.shopify.ping** android app

## Report Details
- **Report ID**: 1172205
- **URL**: https://hackerone.com/reports/1172205
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-04-22T13:18:10.560Z
- **Disclosed**: 2021-11-26T06:02:18.709Z

## Reporter
- **Username**: fr4via
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
It was identified that despite a logout action will be taken by the user at the com.shopify.ping application, the authentication token is not invalidated which allows fully recovery of the initially acquired session. More specifically, after the user provides the required credentials, an **access_token** will be fetched from the server at accounts.shopify.com/oauth/token. After establishing a session and by selecting logout from the corresponding control, the application will send the following DELETE request:

```
DELETE /api/v1/logout HTTP/1.1
authorization: Bearer atkn_**********************************
Host: accounts.shopify.com
Connection: close
Cookie: __cfduid=***********; _y=***************; _shopify_y=***************; request_method=POST
User-Agent: okhttp/3.12.12
```

The server will reply as follows:

```
{"error":"Missing Logout Token Hint"}
```
And will cancel the invalidation process, as the token will still be valid on a subsequent request (e.g.):

```
GET /oauth/userinfo HTTP/1.1
Accept-Encoding: gzip, deflate
authorization: Bearer ***************
....
```
REPLY:
```
{"sub":"...","email":".....@gmail.com","email_verified":true,"family_name":"Doe","given_name":"....","locale":"en","name":".... ...","nickname":".....","updated_at":.....,"zoneinfo":"....","tfa_enabled":false}
```

## Impact

An application should always revoke an access token by the time that the end user choses to Log Off from a session. Keeping a token active, while the user is not aware of it imposes a big risk, since by the time that an unauthorised entity fetches it, may recover a fully "functional" session.

## Attachments
No attachments
