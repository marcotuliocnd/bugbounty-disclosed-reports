# IP restriction bypass via X-Forwarded-For header

## Report Details
- **Report ID**: 1224089
- **URL**: https://hackerone.com/reports/1224089
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-06-11T17:06:34.826Z
- **Disclosed**: 2024-12-05T04:38:52.794Z

## Reporter
- **Username**: mrityu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
#Hello Team, 
Hope you all are well.

So, I have found a 403 bypass on nginx_status/, this endpoint doesn't give that much info but it had 403, so I was able to bypass to see 200 and see the content.

#Steps To Reproduce:
1.  First try to access https://branded-us4-cloud.acronis.com/nginx_status/, you'll see 403 
2. Now add a header, X-Forwarded-For: 127.0.0.1:80, you'll see 200 response code and you'll see the content

## Impact

Information Disclosure that the company doesn't want to reveal.

## Attachments
No attachments
