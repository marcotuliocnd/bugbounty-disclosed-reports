# Stored XSS in the banner block description

## Report Details
- **Report ID**: 1065964
- **URL**: https://hackerone.com/reports/1065964
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-24T18:23:13.107Z
- **Disclosed**: 2021-03-09T10:11:48.691Z

## Reporter
- **Username**: solov9ev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
## Steps To Reproduce:

- Create a new template and add a banner block

{F1128944}

- Add a description to the banner block description: `"><img src=1 onerror=alert(document.domain)>`

- Malicious code executed

{F1128945}

## Proof Of Concept:

{F1128942}

## Impact

With this vulnerability, an attacker can for example steal users cookies or redirect users on malicious website.

## Attachments
- stored_xss.mp4
- _________________2020-12-24_21-17-22.png
- _________________2020-12-24_21-17-35.png
