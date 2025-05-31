# Twitter Account hijack @nextcloudfrance

## Report Details
- **Report ID**: 1916565
- **URL**: https://hackerone.com/reports/1916565
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-03-24T08:20:24.962Z
- **Disclosed**: 2023-03-30T14:05:03.536Z

## Reporter
- **Username**: devokta
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Broken Link Hijacking (BLH) is a web-based attack where it exploits external links that are no longer valid. The attackers take over this expired, stale, and invalid external links on credible websites or web applications for malicious or fraudulent purposes.

Link Hijacking attacks occur because the website/ web application continues to contain links to expired/ stale resources/pages (loaded using external URLs).

Steps :

1. Go to https://nextcloud.com/fr/

2. Go to last and click on Twitter icon.

3. It redirects you to the
 https://twitter.com/nextcloudfrance

4. It gives 404 at first and i takeover the username for Testing Purpose .

5. If you go to https://nextcloud.com/fr/ and click on Twitter Icon , now it redirect you to Attacker ( My ) Profile .

The best way to prevent Broken Link Hijacking attacks is to proactively identify such stale/ dead links and remove them from the website regularly. 

Ref :
https://hackerone.com/reports/1031321
https://hackerone.com/reports/1607429

## Impact

Since the link can be hijacked so any attacker can claim the link and make fake twitter profile of Nextcloud  and can do scam with them.

## Attachments
No attachments
