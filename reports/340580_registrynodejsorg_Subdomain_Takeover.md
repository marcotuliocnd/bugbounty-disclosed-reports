# registry.nodejs.org Subdomain Takeover

## Report Details
- **Report ID**: 340580
- **URL**: https://hackerone.com/reports/340580
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-04-19T16:17:44.299Z
- **Disclosed**: 2018-05-04T17:11:18.503Z

## Reporter
- **Username**: dade
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
I recently found an abandoned and/or overlooked nodejs.org subdomain that was indirectly pointing to Fastly. Fastly doesn't require any proof of DNS ownership to register new distributions that use a given domain, so I was able to effectively take it over.

Vulnerability: Subdomain Takeover via Fastly
Host: http://registry.nodejs.org

Solution:
There are two possible solutions to remediate this issue:

1.) If you no longer wish to use registry.nodejs.org, you can simply delete the registry.nodejs.org CNAME record that is currently pointing to registry.npmjs.org.

2.) Alternatively, if you would like to continue using and/or supporting registry.nodejs.org, you can coordinate with me, I will delete my Fastly service so that someone from nodejs.org can add the registry.nodejs.org domain to the "Domains" field in the related Fastly service.  This should be done in a timely and coordinated fashion to prevent another researcher (or less savory type) from registering it before you are able to.

## Impact

Since discovering this vulnerability I have received more than 300 requests for various npm packages. A malicious attacker could have used this access to begin delivering backdoored (or otherwise malicious) packages to users who were not using the correct registry setting of registry.npmjs.org.

## Attachments
No attachments
