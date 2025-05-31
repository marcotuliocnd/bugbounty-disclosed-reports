# Private invitation links/tokens leak to third-party analytics site

## Report Details
- **Report ID**: 1491127
- **URL**: https://hackerone.com/reports/1491127
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-02-24T17:31:44.193Z
- **Disclosed**: 2022-04-05T06:57:54.754Z

## Reporter
- **Username**: bigbug
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Private invite links are normally FILTERED before sending to  third-party analytics sites. But it is seen that in few cases where the invitation link that requires users to accept NDA policy, the private invitation links are still sent to third party analytics site. 


**Steps to reproduce**

1. Click on the invitation link that has NDA policy.
2. Look for request to https://www.google-analytics.com/collect with private invitation link in the `dl` parameter.

I am attaching a video PoC demonstrating the steps

██████

## Impact

1. As seen in majority of the cases, private links are normally redacted/FILTERED by hackerone before sending to third-party analytics sites. Some links like ones in the report, miss these security validations.
2. Leaking of private program links can be a privacy issue to the program and users.

## Attachments
No attachments
