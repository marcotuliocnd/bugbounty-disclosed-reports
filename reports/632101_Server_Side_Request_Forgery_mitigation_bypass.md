# Server Side Request Forgery mitigation bypass

## Report Details
- **Report ID**: 632101
- **URL**: https://hackerone.com/reports/632101
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-06-29T12:45:33.724Z
- **Disclosed**: 2020-04-18T12:17:25.803Z

## Reporter
- **Username**: mclaren650sspider
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

This vulnerability allows attacker to send arbitrary requests to local network which hosts GitLab and read the response. This is possible due to flawed DNS rebinding protection.

The attack is possible due to flaw here: https://gitlab.com/gitlab-org/gitlab-ce/blob/108c3cf16bed5733ffae086fb62c226961356560/lib/gitlab/url_blocker.rb#L59

The `validate` function performs DNS lookup to check whether the IP address of a domain belongs to the local network. If the IP address belongs to the local network, the `validate` function raises an error and no HTTP request is sent. Furthermore, `validate` returns URI as well as the IP address of the domain to protect against DNS rebinding attacks.
However, if `validate` encounters an error while resolving the domain (for example, the domain does not resolve), the DNS rebinding protection is not applied.

### Steps to reproduce
 1. Create a webhook for a repository on GitLab.com. Use the URL `http://990.hacker1.xyz`. It may return error but let's ignore it now.
 2. Wait about 10 seconds and test webhook by clicking on "Test" and "Push events".
 3. After the hook has executed, you should see content of `http://169.254.169.254` returned.

Wait about 15 seconds between testing attempts, otherwise it may not work due to DNS caching.

The code for proof-of-concept DNS server which hosts `hacker1.xyz` is attached. The PoC uses a chain of CNAME records to prevent caching.

### What is the current *bug* behavior?

The outgoing HTTP requests from webhooks can be sent to the internal network.

### What is the expected *correct* behavior?

It is expected that HTTP requests cannot be sent to the internal network.

### Relevant logs and/or screenshots

F519096
Content of `http://169.254.169.254`

F519095
Content of `http://127.0.0.1`

### Output of checks

This bug happens on GitLab.com

## Impact

Attacker can use SSRF to access sensitive information on the internal network. Furthermore, SSRF in Google Cloud can be leveraged to Remote Code Execution depending on the setup. Publicly disclosed $25,000 #341876 describes a way to gain root access to Google Cloud server via a SSRF vulnerability.

## Attachments
- Screen_Shot_2019-06-29_at_15.37.14.png
- Screen_Shot_2019-06-29_at_15.36.41.png
