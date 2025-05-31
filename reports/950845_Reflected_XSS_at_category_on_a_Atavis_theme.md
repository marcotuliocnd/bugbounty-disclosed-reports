# Reflected XSS at /category/ on a Atavis theme 

## Report Details
- **Report ID**: 950845
- **URL**: https://hackerone.com/reports/950845
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-04T12:37:57.006Z
- **Disclosed**: 2020-11-18T14:22:03.590Z

## Reporter
- **Username**: bugra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hi team,
This report is similar to #947790
You fixed the XSS on search, but I found another XSS at `/category/xsspayload`

For PoC you can check these URLs :
https://magazine.atavist.com/category/%22%3E%3Csvg%20onload%3Dalert%60XSS%60%3E
https://docs.atavist.com/category/%22%3E%3Csvg%20onload%3Dalert%60XSS%60%3E

You can encode " ' < > characters with HTML encoding in this endpoint.

## Impact

Reflected XSS - cookie stealing

Thanks,
Bugra

## Attachments
No attachments
