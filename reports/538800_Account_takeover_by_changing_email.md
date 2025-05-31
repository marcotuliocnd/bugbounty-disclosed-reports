# Account takeover by changing email

## Report Details
- **Report ID**: 538800
- **URL**: https://hackerone.com/reports/538800
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-04-15T19:54:17.948Z
- **Disclosed**: 2019-05-17T03:35:49.134Z

## Reporter
- **Username**: tomoh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
The endpoint `/signup/email` allows users to change their email before they confirm their account email. This endpoint is not protected from CSRF. Thus, any account that is not yet "confirmed" is vulnerable to account takeover using the following steps:
1. Attacker obtains new email address not associated with a KA account.
2. Attacker then lures a new KA user to visit a URL linking to a page that sends a `POST` request to `/signup/email` with the POST body : `casing=camel&email=ATTACKER_EMAIL`.
3. The email change will go through and the attacker would then be able to take over the unconfirmed account using password reset.
4. The original user would not be able to reclaim account since the original email is now not associated with any KA account.

## Impact

Attackers would be able to takeover any unconfirmed account on Khan Academy. And since unconfirmed users can participate in most activities on the website, this could lead to leakage of personal info. Since this ATO does not require any knowledge of the user's email address or KAID, it would become possible to launch large scale attacks by posting malicious links on forums or other places on the internet that KA users would visit.

## Attachments
No attachments
