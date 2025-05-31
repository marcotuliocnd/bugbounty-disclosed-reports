# Publicly editable GitHub wikis

## Report Details
- **Report ID**: 460121
- **URL**: https://hackerone.com/reports/460121
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-12-10T22:08:57.783Z
- **Disclosed**: 2018-12-12T18:37:04.801Z

## Reporter
- **Username**: strukt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
Hello team,

While browsing `https://github.com/liberapay` I found that many of the repositories have their wikis publicly editable by any GitHub user. The following are some of the affected repositories:
```
https://github.com/liberapay/cardregistration-js-kit/wiki
https://github.com/liberapay/mangopay2-python-sdk/wiki
```

I went on and created the following wiki page as a PoC:
`https://github.com/liberapay/cardregistration-js-kit/wiki/PoC`

## Impact

This enables an attacker to edit the wiki pages of the affected repositories completely remotely, adding content that may link to malicious code libraries that would be installed and used by developers or information that may mislead your users.

## Attachments
No attachments
