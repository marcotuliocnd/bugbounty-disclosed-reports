# Subdomain takeover of datacafe-cert.starbucks.com

## Report Details
- **Report ID**: 665398
- **URL**: https://hackerone.com/reports/665398
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-08-01T10:49:53.145Z
- **Disclosed**: 2019-08-28T16:43:06.664Z

## Reporter
- **Username**: parzel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
**Summary:**
The subdomain datacafe-cert.starbucks.com had an CNAME record pointing to an unclaimed Azure webservice. This is a high severity security issue because an attacker can register the subdomain on Azure and therefore can own the subdomain datacafe-cert.starbucks.com.

**Description:**
The dangling CNAME record of datacafe-cert.starbucks.com is pointing to s00397nasv101-datacafe-cert.azurewebsites.net which was not claimed by you. I registered a service with this name and therefore was able to takeover the subdomain. Every attacker doing this has afterwords full control over the contents served on this subdomain.

**Platform(s) Affected:** 
http://datacafe-cert.starbucks.com/
https://datacafe-cert.starbucks.com/

## Supporting Material/References:
view-source:http://datacafe-cert.starbucks.com/

## How can the system be exploited with this bug?
The full domain can be taken over. Arbitrary content can be served under it.

## How did you come across this bug ?
I noticed the dangling CNAME record of datacafe-cert.starbucks.com.

## Recommendations for fix
1) Remove the dangling CNAME record from datacafe-cert.starbucks.com
2) I release s00397nasv101-datacafe-cert.azurewebsites.net
3) You can reclaim it if you want

## Impact

This issue can be exploited in several ways, for example but not limited to: XSS, Phishing, Session Hijacking due to bypassing of SOP

## Attachments
No attachments
