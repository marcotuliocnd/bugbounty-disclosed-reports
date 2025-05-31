# SSH server compatible with several vulnerable cryptographic algorithms

## Report Details
- **Report ID**: 318068
- **URL**: https://hackerone.com/reports/318068
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-21T02:23:21.045Z
- **Disclosed**: 2018-03-02T20:44:31.260Z

## Reporter
- **Username**: northivanastan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
An ssh-audit scan found that ssh.fr.cloud.gov supports sha1 for various purposes(including exclusively for MAC addresses), as well as arcfour. Both of these are outdated and known vulnerable.

The algorithms used are also indicative of an outdated SSH version (OpenSSH 6 or Dropbear 2013). It's probably a good idea to upgrade.

The output of ssh-audit is attached.

## Impact

A man-in-the-middle attack may expose data encrypted with arcfour and/or hashed with sha1, which can then be decrypted to find things like passwords or payloads sent over SSH.

## Attachments
- ssh-audit-out.txt
