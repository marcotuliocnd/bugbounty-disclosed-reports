# ap_find_token() Buffer Overread

## Report Details
- **Report ID**: 241610
- **URL**: https://hackerone.com/reports/241610
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-20T08:36:29.423Z
- **Disclosed**: 2017-08-10T12:55:58.516Z

## Reporter
- **Username**: javier_sensepost
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Versions Affected:
httpd 2.2.32
httpd 2.4.24 (unreleased)
httpd 2.4.25

Description:
The HTTP strict parsing changes added in 2.2.32 and 2.4.24 introduced a
bug in token list parsing, which allows ap_find_token() to search past
the end of its input string. By maliciously crafting a sequence of
request headers, an attacker may be able to cause a segmentation fault,
or to force ap_find_token() to return an incorrect value.

Mitigation:
2.2.32 users should either apply the patch available at
https://www.apache.org/dist/httpd/patches/apply_to_2.2.32/CVE-2017-7668.patch
or upgrade in the future to 2.2.33, which is currently unreleased.

2.4.25 users should upgrade to 2.4.26.

You can contact me on javijmor@gmail.com or javier@sensepost.com

I would like to donate the bug bounty's money (if any) to charity and preferably do it in behalf of my company, SensePost..

## Attachments
No attachments
