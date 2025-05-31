# Stored Xss on bugzilla.mozilla.org via comment edit feature from non-admin to admin.

## Report Details
- **Report ID**: 2111291
- **URL**: https://hackerone.com/reports/2111291
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-08-16T05:14:13.951Z
- **Disclosed**: 2023-09-20T10:16:33.329Z

## Reporter
- **Username**: r3dpars3c
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
Hi There !
There is Stored xss on comment feature.
The XSS executed when admin tries to edit the comment. The XSS fires.
I tried to Bypass the CSP But was not able to.

Steps To Reproduce.
1. Create a report in bugzilla.mozilla.org as users.
2.  Comment this xss payload as users ``</base</sTyle/</scRIpt/</textArea/</noScript/</tiTle/-->＜h1/<h1><image/onerror="import('data:application/javascript;charset=utf-8;base64,YWxlcnQoZG9jdW1lbnQuZG9tYWluKTtjb25zb2xlLmxvZyhkb2N1bWVudC5kb21haW4pOy8v')//%27"src><script>``
3. Now as admin, TRy to edit the comment, you will see xss popup with document.domain when csp disabled.

I am working on to bypass the csp
I have filed a bug report on bugzilla with my xss containing comment.
https://bugzilla.mozilla.org/show_bug.cgi?id=1848911
Try to edit and  check your browser console if csp is enabled. if csp isn't enabled, you will be able to see popup.
I tested this on my local instance, and this worked.

Thanks
Best Regards
r3dpars3c

## Impact

Client side javascript execution.

## Attachments
No attachments
