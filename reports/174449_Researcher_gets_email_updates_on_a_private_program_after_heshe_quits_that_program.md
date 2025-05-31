# Researcher gets email updates on a private program after he/she quits that program.

## Report Details
- **Report ID**: 174449
- **URL**: https://hackerone.com/reports/174449
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-07T06:40:41.033Z
- **Disclosed**: 2016-11-21T08:12:53.406Z

## Reporter
- **Username**: sasi2103
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
I found out that after I quit private program, I still gets update about that program, e.g. new scope changes/amount of money and etc.

**Description (Include Impact):**
I noticed that if I quit program I still gets email updates about the private program, private data can be leak on that email.

### Steps To Reproduce
1. I got invite to █████ private program.
2. After period of time I quit that program.
3. I still get email updates about that program.

### soultions
1. Remove email address from program once hacker quit.
2. Set boolean flag, true/false once the user quit. (The flag can help once the user gets invite again or if he/she wants to rejoin).

Thanks,
Sasi

## Attachments
No attachments
