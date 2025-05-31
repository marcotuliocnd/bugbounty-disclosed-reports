# Hacker can bypass 2FA requirement and reporter blacklist through embedded submission form

## Report Details
- **Report ID**: 418767
- **URL**: https://hackerone.com/reports/418767
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-04T02:41:19.585Z
- **Disclosed**: 2018-10-31T17:24:15.211Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi Team,

### Summary:

A program owner can enforce the hackers to setup the two-factor authentication before submitting new reports to their program here: https://hackerone.com/parrot_sec/submission_requirements (see below image)

{F355169}

The [Parrot Sec](https://hackerone.com/parrot_sec) program has this feature enabled to enforce the hackers to setup `2FA` before submitting reports. I removed my `2FA` to test and it is good that i was block from submitting new reports (see below image)

{F355168}

---

### BYPASS 2FA Requirements using Embedded Submission:

Now i was able to bypass this 2FA setup requirements by using the Parrot Sec program __Embedded Submission Form__.

## Steps to reproduce:

  1. Login to your account and __remove__ your 2FA on your account (if you already setup it)
  2. Now go to https://hackerone.com/parrot_sec and hit `Submit Report` button, observed that you cannot submit report unless you will enable your 2FA.
  3. __BYPASS:__ Get the `Embedded Submission` URL on their [policy page](https://hackerone.com/parrot_sec): i get this ->> https://hackerone.com/0a1e1f11-257e-4b46-b949-c7151212ffbb/embedded_submissions/new
  4. Now submit report using that embedded submission form and you can submit reports without setting-up your 2FA, despite the program __enforce__ the user to setup the 2FA before submitting new reports.
  5. 2FA requirements successfully bypassed!

## Impact

Bypassing the enabled protection/feature of the program.

Let me know if anything else is needed.

Regards
Japz

## Attachments
- 2fa_required.JPG
- enable_2fa_requirements.JPG
