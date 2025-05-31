# Server Side Request Forgery on JSON Feed

## Report Details
- **Report ID**: 280511
- **URL**: https://hackerone.com/reports/280511
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-19T14:22:14.085Z
- **Disclosed**: 2017-12-06T10:18:15.005Z

## Reporter
- **Username**: mr_r3boot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
Hi Team, I would like to report SSRF issue.

#PoC:
1. Navigate to ```https://infogram.com/app/[user-project]```.
2. Click on edit logo fields and click on add JSON Data.
3. Enter ```[url][openport]``` response is ```Download failed```
4. Enter ```[url][closedport]``` response is ```Invalid data source```

#Fix:
Don't give permission to port related connections or use single error message.

Regards,
Mr.R3boot.

## Attachments
No attachments
