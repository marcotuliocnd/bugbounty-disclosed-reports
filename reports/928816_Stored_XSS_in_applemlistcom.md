# Stored XSS in app.lemlist.com

## Report Details
- **Report ID**: 928816
- **URL**: https://hackerone.com/reports/928816
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-07-21T18:32:17.979Z
- **Disclosed**: 2020-07-23T13:20:13.506Z

## Reporter
- **Username**: solov9ev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lemlist

## Vulnerability Information
## Summary:
[add summary of the vulnerability]

## Steps To Reproduce:
  - Go to Company > Buddies-to-Be > Custom variables
  - Add malicious code: `" onmouseover="confirm(document.domain)" a="`

{F915718}

  -  Go to Company > Messages > Blank email
  - In the WYSIWYG  editor select `Custom variables`
  - Malicious code executed

{F915719}

## Impact

With this vulnerability, an attacker can for example steal users cookies or redirect users on malicious website.

## Attachments
- _________________2020-07-21_21-29-55.png
- _________________2020-07-21_21-29-51.png
