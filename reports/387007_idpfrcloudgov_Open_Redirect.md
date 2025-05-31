# [idp.fr.cloud.gov] Open Redirect

## Report Details
- **Report ID**: 387007
- **URL**: https://hackerone.com/reports/387007
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-07-26T04:18:20.909Z
- **Disclosed**: 2018-11-01T18:49:53.069Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
**Description:** Open Redirect

**Domain:** idp.fr.cloud.gov

**Steps To Reproduce:**
Open URL:
```
https://idp.fr.cloud.gov//blackfan.ru/..;/css
```

**HTTP Response**
```
HTTP/1.1 302 Found
...
Location: //blackfan.ru/..;/css/
...
```

## Impact

A web application accepts a user-controlled input that specifies a link to an external site, and uses that link in a Redirect. This simplifies phishing attacks.

## Attachments
No attachments
