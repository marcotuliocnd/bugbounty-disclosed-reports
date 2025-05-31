# Subdomain Takeover of brand.zen.ly

## Report Details
- **Report ID**: 1474784
- **URL**: https://hackerone.com/reports/1474784
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-02-08T19:12:14.808Z
- **Disclosed**: 2022-02-17T10:09:22.829Z

## Reporter
- **Username**: mega7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zenly

## Vulnerability Information
Hello Gents,

### Background:
> + Subdomain takeover vulnerabilities occur when a subdomain (subdomain.example.com) is pointing to a service (e.g. GitHub pages, Heroku, etc.) that has been removed or deleted. This allows an attacker to set up a page on the service that was being used and point their page to that subdomain. For example, if subdomain.example.com was pointing to a GitHub page and the user decided to delete their GitHub page, an attacker can now create a GitHub page, add a CNAME file containing subdomain.example.com, and claim subdomain.example.com.

### Summary:
+ I just went to `brand.zen.ly` and it shows an error "Not Found", also I've checked the CNAME is pointing to `brandpad.io`, which means it can be added to any account.
+ This is pretty serious security issue in some context, so please act as fast as possible.
+ I was able to takeover `brand.zen.ly` by registering at **Brandpad**.

### Vulnerable URL:
+ https://brand.zen.ly

### Proof of Concept:
```
└─$ dig brand.zen.ly
brand.zen.ly.		255	IN	CNAME	brandpad.io.
```
+ Please visit: https://brand.zen.ly.

+ {F1610891}

### Recommended Fix:
+ Check your DNS-configuration for subdomains pointing to services not in use.
+ Set up your external service so it fully listens to your wildcard DNS.

## Impact

+ Subdomain takeover is abused for several purposes:
1. Malware distribution.
2. Phishing / Spear phishing.
3. XSS and steal cookies.
4. Bypass domain security.
5. Legitimate mail sending and receiving on behalf of Datadog subdomain.

Thanks and have a nice day!

## Attachments
- simplescreenrecorder-2022-02-08_21.10.12.mp4
