# Information leakage on django.aspen.io

## Report Details
- **Report ID**: 272982
- **URL**: https://hackerone.com/reports/272982
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-09-29T13:42:44.839Z
- **Disclosed**: 2017-09-29T15:15:44.853Z

## Reporter
- **Username**: the_krisk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: aspen

## Vulnerability Information
Hi Team,

I got a error message that disclose the version of nginx with OS detail, since The version of nginx is vulnerable to integer overflow.
Impact:
By seeing this information attacker can throw only interger overflow attack in order to get sensitive information 
Finally Request you to remove those Information while throwing an error.

Note: I attached POC in the attachment.

Thank you.

## Attachments
- Aspen.io.jpg
