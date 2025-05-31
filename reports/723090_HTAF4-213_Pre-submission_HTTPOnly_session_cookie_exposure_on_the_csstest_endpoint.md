# [HTAF4-213] [Pre-submission] HTTPOnly session cookie exposure on the /csstest endpoint

## Report Details
- **Report ID**: 723090
- **URL**: https://hackerone.com/reports/723090
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-26T01:04:23.490Z
- **Disclosed**: 2024-06-18T17:08:40.852Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Description
We were able to identify endpoint which prints request headers into the page. This included sensitive HTTPOnly session cookies which shouldn't be accessible in the DOM.

##POC
https://█████████/csstest
███████
There will be `JSESSIONID` cookie reflected.

##Suggested fix
Remove the page, it's content, or restrict access to it.

## Impact

This in combination with any XSS attack will result in session cookie steal and likely authentication bypass (by default this isn't possible because XSS can't access HTTPOnly cookies), since attacker can request `/csstest` page with XSS and read the response.
We will try to find one and chain the vulns together.

## Attachments
No attachments
