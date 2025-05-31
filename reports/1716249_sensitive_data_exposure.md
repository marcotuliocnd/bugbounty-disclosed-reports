# sensitive data exposure

## Report Details
- **Report ID**: 1716249
- **URL**: https://hackerone.com/reports/1716249
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-09-29T04:04:17.013Z
- **Disclosed**: 2022-11-10T14:41:12.389Z

## Reporter
- **Username**: saibalaji143_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
[A Password hash entry was found in /etc/passwd. This is a major vulnerability since /etc/passwd is a world-readable file by default. Once the password hash is found, an attacker may extract the password using a program like crack.]

## Impact:
it is high impact vulnerability .once hacker found password hash it may be leads to develop a program like crack

## Steps To Reproduce:
[https://www.reddit.com/etc%2fpasswd]

  1. [add step]
  1. [add step]
  1. [add step]

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

A Password hash entry was found in /etc/passwd. This is a major vulnerability since /etc/passwd is a world-readable file by default. Once the password hash is found, an attacker may extract the password using a program like crack.

## Attachments
- Screenshot_2022-09-28_23_22_43.png
