# Two out-of-bounds array reads in Python AST builder (Re-opening 520612 with CVEs)

## Report Details
- **Report ID**: 746766
- **URL**: https://hackerone.com/reports/746766
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-11-26T17:21:45.088Z
- **Disclosed**: 2021-08-25T20:51:45.994Z

## Reporter
- **Username**: blarsen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I'm re-submitting #520612 after getting CVEs issued, as instructed in an automated email from November 17th.

Getting CVEs issued took a while, but here they are:

- https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-19274
- https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-19275

## Impact

A service that takes Python snippets as payload, but doesn't necessarily execute them, could possibly be caused to crash, leading to a denial of service. Examples of such services include online playgrounds for static analysis tools, syntax highlighting & formatting services, etc.

I didn't copy-and-paste all the original details here; see the original issue ( #520612 ) for that.

## Attachments
No attachments
