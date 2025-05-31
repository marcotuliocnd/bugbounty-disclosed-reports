# SAML Response Reuse on hackerone.com/users/saml/auth

## Report Details
- **Report ID**: 888930
- **URL**: https://hackerone.com/reports/888930
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-06-01T21:34:28.618Z
- **Disclosed**: 2020-07-24T18:51:30.591Z

## Reporter
- **Username**: samtink
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
When logging in with SAML, the user's IDP authenticates the user and generates a SAML response. The IDP then redirects the user's browser back to HackerOne to submit the SAML response. Upon receiving the SAML response, HackerOne validates it, sets a session cookie in the user's browser, and logs the user in. The SAML response can be captured and resubmitted to H1 repeatedly until it expires. Every time H1 receives the captured SAML response it sets a new session cookie and logs the user in.

**Description:**

### Steps To Reproduce

1. Make sure your email address is set to use your organization's SSO provider. Make sure you can capture and replay traffic using Burp suite or some other proxy.
2. Go to the H1 login screen and enter your email. Press the login button to be sent to your organization's SAML provider (IDP).
3. Log into your org's IDP and capture the SAML response from the IDP. The request that needs to be captured is the POST request to hackerone.come/users/saml/auth. In the message body you can find the SAML response. The easiest way to capture and replay is to send it to the repeater tab in Burp. 
4. Resend the POST request with the SAML response to H1 and observe the successful response with a new session identifier. Send 4-5 more times and observe the successful responses and new session id's. 

### Your Environment (Browser version, Device, etc)

 * Burp Version: ████████
 * Browser: █████████
 * SSO Provider: █████████
 * SAML Response TTL: ██████████.

### Remediation:

After a SAML response is used store the assertion ID and it's expiration in a list. When a SAML response has been received and validated, check the assertion ID against the previously mentioned list. If the ID is in the list, throw an error and do not log the user in. Once an ID in the list is past it's expiration then remove it from the list (since it will fail anyway for being expired).

## Impact

Likelihood:
There is a fairly high barrier of entry to be able to use this flaw. An attacker would have to obtain a valid SAML response. This could be done via MITM, phishing, XSS, etc. None of which are super easy but none are impossible. The likelihood of an attacker being able to obtain a SAML response varies greatly between different organizations and their respective security postures. The likelihood increases the longer the SAML response is valid for. It can be set to as little as a few minutes or up to several weeks. The organization's IDP is responsible for setting how long a SAML response is valid. 

Impact:
If an attacker would successfully capture and use a SAML response they would log into H1 as the user who generated the SAML response. Depending on which user they log in as they could have full control over an organizations H1 program or they could have only read only permissions. This could allow the attacker to see undisclosed vulnerabilities and full instructions on how to exploit them. The attacker could also pose as a member of the organization and tarnish relations with security researchers. The attacker could lock members of the organization out by removing permissions. So ultimately, the attacker would inherit whatever permissions from the user they stole the SAML response from.

## Attachments
No attachments
