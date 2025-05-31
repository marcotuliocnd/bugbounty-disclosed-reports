# Subdomain Takeover uptime

## Report Details
- **Report ID**: 824909
- **URL**: https://hackerone.com/reports/824909
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-03-19T21:29:44.357Z
- **Disclosed**: 2020-05-05T20:50:32.622Z

## Reporter
- **Username**: ahmed_alwardani
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: btfs

## Vulnerability Information
Hello Team:

i can't report it to the company so i hope to accept it as a valid bug , i found subdomain takeover in your subdomain ```uptime.btfs.io``` , i found this subdomain pointed to uptimerobot and not claimed so i signedup in uptimerobot and claimed it.

POC:
------

1 - open https://uptime.btfs.io/
2 - you need a password to login ```A123456789```
3 - {F753695}

## Impact

- Subdomain takeover can be abused to do several things like :
Malware distribution
Phishing / Spear phishing
XSS
Authentication bypass
Legitimate mail sending and receiving on behalf of ford subdomain

## Attachments
- Screenshot_9.png
