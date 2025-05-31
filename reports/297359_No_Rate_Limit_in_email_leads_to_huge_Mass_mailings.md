# No Rate Limit in email leads to huge Mass mailings

## Report Details
- **Report ID**: 297359
- **URL**: https://hackerone.com/reports/297359
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-12-12T20:57:12.709Z
- **Disclosed**: 2018-06-01T22:36:20.502Z

## Reporter
- **Username**: trabajoduro_2
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi Team,

I have found a logical flaw(NOT DoS) in the website 'https://app.mopub.com/' 


1.Use Burp Suite and capture below request upon navigation to *Code integration*
2.Click on Send button after entering email address in the input field of 'Enter one or more email addresses and we'll send you links to the integration instructions for this ad unit.'
{code}
POST /web-client/api/ad-units/email-instructions HTTP/1.1
Host: app.mopub.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://app.mopub.com/ad-unit?key=█████████&showIntegration=true
Content-Type: application/json
x-csrftoken: █████████
Content-Length: 88
Cookie: _ga=████; _gid=███; csrftoken=███; mp_mixpanel__c=8; sessionid=████████; mp_c99579c4804fba6b8aeed7a911581652_mixpanel=%7B%22distinct_id%22%3A%20%22405f9ac1ce5749abb6092834819b3ec4%22%2C%22accountKey%22%3A%20%22748a6b56971b4bdf94ea73e4cc35e93f%22%2C%22accessLevel%22%3A%20%22member%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.mopub.com%2Fget-started%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.mopub.com%22%7D
Connection: close

{"addresses":["§████@mailinator.com§"],"key":"███"}
{code}
3.Send the captured request to INtruder and repeat the request in loop
4.Observe that email box is flooded with MoPub ad unit integration instructions

Remediation:
Rate limiting should be implemented

Regards
Akhil Kakkireni

## Impact

E-mail bombs hack may create Denial of service (DoS) conditions against your e-mail software and even your network and Internet connection by taking up a large amount of bandwidth and, sometimes, requiring large amounts of storage space

## Attachments
- hackerone-Mopub.jpg
- hackerone-Mopub2.jpg
