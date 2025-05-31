# [h1-2006 CTF] Multiple vulnerabilities leading to account takeover and two-factor authentication bypass allows to send pending bounty payments

## Report Details
- **Report ID**: 895722
- **URL**: https://hackerone.com/reports/895722
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-06-10T23:42:09.687Z
- **Disclosed**: 2020-07-06T16:02:24.238Z

## Reporter
- **Username**: kapytein
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
Hi,

First things first, the flag of the CTF challenge.

{F863095}

### Write-Up

I've published my write-up at https://kapytein.nl/texts/2020-06-10-h1-2006-ctf-writeup-2cf34abd3ed/, in order to avoid a lengthy report 😅. 

### TL;DR

1) 2FA bypass as we control both values on the comparison. 
2) SSRF to `software.bountypay.h1ctf.com` to discover a BountyPay Android application.
3) Solve Android challenges using deeplinks. Use leaked Authorization token for `api.bountypay.h1ctf.com`.
4) Leaked staff ID on the badge of [Sandra](https://twitter.com/SandraA76708114) allows access to `staff.bountypay.h1ctf.com` via a `POST /api/staff` call on `api.bountypay.h1ctf.com`.
5) Privilege escalation using GET CSRF.
6) 2FA bypass via a CSS injection.

Thank you for organizing this challenge!

## Impact

This allows an attacker to process bounty payments of customers.

## Attachments
- flagfound.png
