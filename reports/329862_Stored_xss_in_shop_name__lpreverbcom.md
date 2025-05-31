# Stored xss in shop name @ lp.reverb.com

## Report Details
- **Report ID**: 329862
- **URL**: https://hackerone.com/reports/329862
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-03-26T04:04:28.168Z
- **Disclosed**: 2018-10-01T12:47:19.119Z

## Reporter
- **Username**: sandeep_hodkasia
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reverb

## Vulnerability Information
hello team,

There is a stored xss in lp.reverb.com.
Attacker can inject malicious script into server while adding shop name as `lll"></script><script>alert('xss');</script>`.
Exploit: https://lp.reverb.com/shops/faniyos-boutique/listings

Steps to reproduce:
1. Navogate to https://reverb.com/my/lp_shop/edit
2. Change your lp shop name to this: lll"></script><script>alert('xss')</script>
3. Save the changes.
4. View your lp shop.

Fix:
Sanitise the given input in the backend and encode the special characters.

Thanks,
Sandeep

## Impact

Attack can save malicious script directly into the server. Malicious script can be used to gain users session.

The hacker selected the **Cross-site Scripting (XSS) - Stored** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://lp.reverb.com/shops/faniyos-boutique/listings

**Verified**
Yes



## Attachments
- Screen_Shot_2018-03-26_at_9.33.45_AM.png
