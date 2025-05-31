# Add another email address without verification

## Report Details
- **Report ID**: 265987
- **URL**: https://hackerone.com/reports/265987
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-09-05T09:45:13.811Z
- **Disclosed**: 2017-10-05T12:24:43.391Z

## Reporter
- **Username**: tungpun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
## Introduction
In the normal case, to link another email address to the Weblate account, users need to own the email address and click the verification link. However, I found an issue, that allows adding another email address without clicking on the verification link.

## Description and PoC:
* Create a new openSUSE ID. Pick up a new email. In this example, I choose `admin@weblate.org`.
{F218492}
Of course, you don't need to verify the email address for this openSUSE ID.

* Then backs to weblate.org, go to Your profile > Authentication `https://demo.weblate.org/accounts/profile/#auth`.
Add the above openSUSE account as a new association.
{F218493}

* That all, go to Account tab `https://demo.weblate.org/accounts/profile/#account`, you will see the new email in your account's email field.
{F218494}

## Mitigation
Weblate should only accept the association from verified openSUSE ID.

## Attachments
- Screen_Shot_2017-09-05_at_5.25.09_PM.png
- Screen_Shot_2017-09-05_at_5.23.04_PM.png
- Screen_Shot_2017-09-05_at_5.23.11_PM.png
