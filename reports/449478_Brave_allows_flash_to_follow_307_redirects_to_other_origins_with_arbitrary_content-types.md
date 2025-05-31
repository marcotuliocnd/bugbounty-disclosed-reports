# Brave allows flash to follow 307 redirects to other origins with arbitrary content-types

## Report Details
- **Report ID**: 449478
- **URL**: https://hackerone.com/reports/449478
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-11-25T07:41:37.412Z
- **Disclosed**: 2018-12-12T19:20:29.745Z

## Reporter
- **Username**: tvgfvghjbhunj
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
Steps to reproduce:

Used https://github.com/sp1d3r/swf_json_csrf in latest available version of flash to send a post request cross-domain with a non-simple content type.


Actual results:

The request is sent in firefox.


Expected results:

The request should either not be sent or the content-type should not be allowed to be a non-simple content-type without a cors preflight request being made.

## Impact

https://bugzilla.mozilla.org/show_bug.cgi?id=1436241&fbclid=IwAR1iyg5ooZF46A-9BCtKGBIQgCsxQC419U3BaHzj8VnP9pcx8W_CRmBSbZQ

## Attachments
No attachments
