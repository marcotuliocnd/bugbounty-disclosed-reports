# [demo.weblate.org] Stored Self-XSS via Editor Link in Profile

## Report Details
- **Report ID**: 223331
- **URL**: https://hackerone.com/reports/223331
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-24T09:16:48.255Z
- **Disclosed**: 2017-05-17T14:20:03.777Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi,

Input validation and/or sanitisation is not currently applied to the "Editor Link" in the user's [Preferences](https://demo.weblate.org/accounts/profile/#preferences). Consequently, it is possible to store a JavaScript payload which is stored and executes in the Weblate instance context.

{F178717}

## Steps to reproduce
1. Visit the above Preferences page and identify the Editor Link field
2. Populate the field with: `javascript:confirm(document.domain)`
3. Visit a [translation page](https://demo.weblate.org/translate/hello/master/zh_CN/?checksum=6412684aaf018e8e) and select a Source String Location
4. The XSS will trigger upon clicking on a Source String (e.g. `main.c`)

{F178716}

Please let me know if you require any additional information regarding this issue.

Thanks!

## Attachments
- EditorLink.png
- WeblateXSS.png
