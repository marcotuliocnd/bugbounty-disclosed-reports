# Using plain git protocol (vulnerable to MITM)

## Report Details
- **Report ID**: 181214
- **URL**: https://hackerone.com/reports/181214
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-11-09T23:34:30.865Z
- **Disclosed**: 2016-11-09T23:47:38.262Z

## Reporter
- **Username**: e3amn2l
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
Using plain git protocol (git://domain) is insecure as the server is not verified (MITM attacker can return different content if last commit not checked against known one)
more information about this issue (Protocols to choose from when cloning): 
https://gist.github.com/grawity/4392747
vcs-field-uses-insecure-uri check details:
https://lintian.debian.org/tags/vcs-field-uses-insecure-uri.html

in:
https://github.com/paragonie/airship/blob/master/.travis.yml#L12
```
- git clone git://github.com/jedisct1/libsodium.git
```

fix: 
1. use https protocol instead of git. (https:// vs git://)
2. implement verification of last commit/tag if possible (known commit/tag is fetched instead of master), more details about possible implementations in report: "Missing GIT tag/commit verification in Docker"
https://hackerone.com/reports/181212

## Attachments
No attachments
