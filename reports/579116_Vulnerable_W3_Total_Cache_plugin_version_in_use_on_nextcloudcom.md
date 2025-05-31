# Vulnerable W3 Total Cache plugin version in use on nextcloud.com

## Report Details
- **Report ID**: 579116
- **URL**: https://hackerone.com/reports/579116
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-05-13T15:02:55.043Z
- **Disclosed**: 2019-06-21T09:10:01.856Z

## Reporter
- **Username**: bc1cc2612e41cc49fc0540f
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi there,

I noticed you are currently using a vulnerable version of W3 Total Cache, as the changelog containing the plugin version is publicly reachable: https://nextcloud.com/wp-content/plugins/w3-total-cache/changelog.txt

W3 Total Cache makes the site vulnerable to a series of attacks, including XSS, CSRF and SSRF.

Some references:

https://wpvulndb.com/vulnerabilities/8629
https://wpvulndb.com/vulnerabilities/9269
https://secupress.me/blog/4-new-security-flaws-w3-total-cache-0-9-4-1/

### Mitigation

Update the plugin to the last version (or manually patch the vulnerabilities).

On a separate note, I saw this domain is not eligible for bounty :) But wanted to bring this to your attention the same, being WordPress a common target.

Furthermore, this specific vulnerability could lead to a full website defacement: https://blog.mazinahmed.net/2014/12/w3-total-caches-w3totalfail.html

Best Regards,
Francesco

## Impact

Being the vulnerabilities easy to detect with an external scan, hackers could take advantage of, and use the website to run various malicious activities.

## Attachments
No attachments
