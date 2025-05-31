# Blind SSRF due to img tag injection in career form

## Report Details
- **Report ID**: 236301
- **URL**: https://hackerone.com/reports/236301
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-06-03T19:55:27.379Z
- **Disclosed**: 2017-07-19T02:35:17.610Z

## Reporter
- **Username**: encrypt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mixmax

## Vulnerability Information
Hi,
There is SSRF vulnerability due to img tag injection in career form. Attacker can inject multiple tags and perform multiple requests on remote hosts.

**POC**
1. Visit https://mixmax.com/careers.
2. Click on `Apply now`.
3. Insert img tag `<img src=https://your_choice.com>` in all the fields.
4. Click on `Send Application`.
5. Check server logs.

I got the following ip and user-agent headers.
IP: 66.249.84.213
User-Agent: Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)

Thanks

## Attachments
- ip_useragent.png
- request.png
