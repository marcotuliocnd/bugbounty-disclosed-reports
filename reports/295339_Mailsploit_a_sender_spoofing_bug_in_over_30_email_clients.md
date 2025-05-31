# Mailsploit: a sender spoofing bug in over 30 email clients

## Report Details
- **Report ID**: 295339
- **URL**: https://hackerone.com/reports/295339
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-12-05T11:38:04.408Z
- **Disclosed**: 2019-09-19T20:34:46.811Z

## Reporter
- **Username**: pwnsdx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Mailsploit is a collection of bugs in email clients that allow effective sender spoofing and code injection attacks. The spoofing is not detected by Mail Transfer Agents (MTA) aka email servers, therefore circumventing spoofing protection mechanisms such as DMARC (DKIM/SPF) or spam filters.

Bugs were found in over 30 applications, including prominent ones like Apple Mail (macOS, iOS and watchOS), Mozilla Thunderbird, various Microsoft email clients, Yahoo! Mail, ProtonMail and others.

In addition to the spoofing vulnerability, some of the tested applications also proved to be vulnerable to XSS and code injection attacks.

More informations are available on mailsploit.com

## Impact

It allows the attacker to display an arbitrary sender email address to the email recipient while bypassing spoofing protection mechanisms such as DMARC (DKIM/SPF) or spam filters.

## Attachments
No attachments
