# Server version disclosure on [jenkins.brew.sh]

## Report Details
- **Report ID**: 221989
- **URL**: https://hackerone.com/reports/221989
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-04-18T19:09:28.452Z
- **Disclosed**: 2017-04-19T14:36:48.095Z

## Reporter
- **Username**: neutrinoguy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: homebrew

## Vulnerability Information
Hello Homebrew security team,

I know this is a low severity issue but I thought to get you in notice will be best. The site
**jenkins.brew.sh** discloses the Nginx server version.

**Impact**
The information is can be used by attacker for further finding of exploits and information gathering.

```
curl -i jenkins.brew.sh
HTTP/1.1 301 Moved Permanently
Server: nginx/1.6.2
Date: Tue, 18 Apr 2017 18:59:21 GMT
Content-Type: text/html
Content-Length: 184
Connection: keep-alive
Location: https://jenkins.brew.sh/

<html>
<head><title>301 Moved Permanently</title></head>
<body bgcolor="white">
<center><h1>301 Moved Permanently</h1></center>
<hr><center>nginx/1.6.2</center>
</body>
</html>
```

**Fix**
In Ngnix configuration set:

```server_tokens off;```

Thanks


## Attachments
No attachments
