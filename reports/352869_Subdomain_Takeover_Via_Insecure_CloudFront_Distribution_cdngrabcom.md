#  Subdomain Takeover Via Insecure CloudFront Distribution cdn.grab.com

## Report Details
- **Report ID**: 352869
- **URL**: https://hackerone.com/reports/352869
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-05-16T13:40:17.516Z
- **Disclosed**: 2021-02-24T01:52:42.853Z

## Reporter
- **Username**: todayisnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grab

## Vulnerability Information
Good day, I truly hope it treats you awesomely on your side of the screen :)


I have found that your website cdn.grab.com is pointed via a cname to a cloudfront instance

cdn.grab.com => *.cloudfront.net

This was not registered on Amazon Aws Cloudfront.

I was able to take over the domain:

See my POC (Pug of Concept)
http://cdn.grab.com/index.html



Options How to fix:

1) Remove the Cname record on cdn.grab.com to not point to cloudfront.net

2) Ask me to remove my registered cdn.grab.com on cloudfront, and you can re register yours :)

May you be well on your side of the screen :)

-Eric

## Impact

Impact:

Cyber attackers can launch a phishing campaign leveraging your established (soon to be impacted) brand reputation.

The victim has no way of telling, whether the content is served by the domain owner or the cyber attacker.

Attackers can also chain higher severity attacks to this. Many applications expose session cookies to a wildcard domain (*.example.com),
so any subdomain can access them. An attacker can take a forgotten subdomain, trick the user to visit it, and extract cookies 
(even those with secure flag). This can be seen as an advanced version of XSS.

## Attachments
No attachments
