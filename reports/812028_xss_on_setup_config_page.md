# xss on setup config page 

## Report Details
- **Report ID**: 812028
- **URL**: https://hackerone.com/reports/812028
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-03-06T08:56:57.544Z
- **Disclosed**: 2021-02-14T16:21:26.534Z

## Reporter
- **Username**: jackzhou
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Nextcloud version: 18.0.1
In setup config page，setting `mysql Username` with payload`<script>alert(1)</script>`, and set others. F739076
then submit . F739077
this gif will show poc: F739069

## Impact

This is because the code does not filter dangerous characters. so dangerous characters need to be escaped.

## Attachments
- 2xss.gif
- 2xss-0.png
- 2xss-1.png
