# Subdomain takeover of █████████

## Report Details
- **Report ID**: 1457928
- **URL**: https://hackerone.com/reports/1457928
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-01-22T10:31:04.873Z
- **Disclosed**: 2022-09-06T18:50:52.831Z

## Reporter
- **Username**: martinvw
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
I have found a subdomain of `███████` to be vulnerable to takeovers via a CNAME to unclaimed domain. I have claimed this domain and redirected them to a blank page to prevent a bad actor from doing so in the meantime, and hosted a POC file at obscure URLs. These are the following domains I discovered and the outdated endpoints on Azure to which they point:

█████ --> ████

...and the proof-of-concept file is at the following location:

https://████████/proof.e7437329-ab61-4f22-a049-df5b3685313a.txt

I have not hosted any other file nor attempted any other vector of attack.

## Impact

You're probably familiar with takeovers like this by now, but through this vulnerability, it would be possible for an attacker to obtain cookies and other sensitive information from your users via phishing, cookie hijacking, or XSS.

More info on possible attack vectors can be found at MDN: https://developer.mozilla.org/en-US/docs/Web/Security/Subdomain_takeovers

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
To confirm the issue visit:

https://████████/proof.e7437329-ab61-4f22-a049-df5b3685313a.txt

## Suggested Mitigation/Remediation Actions
Remove CNAME of █████



## Attachments
No attachments
