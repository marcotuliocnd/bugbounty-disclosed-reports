# Session Cookie Without Secure Flag 

## Report Details
- **Report ID**: 343928
- **URL**: https://hackerone.com/reports/343928
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-04-27T12:50:26.732Z
- **Disclosed**: 2018-04-28T11:44:36.167Z

## Reporter
- **Username**: cybertiger
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ed

## Vulnerability Information
Hi Ed,

The bug mentioned in the report #343095 is not yet correctly patched I believe.

Previously, the Researcher reports that the cookie(_gitlab_session) is not Secure (Missing Secure Flag) and u closed that report as Informative and said that 
"Expoitability of this issue is so low that it does not warrant an immediate fix. 
In order to actually exploit this issue you would need to find an XSS vulnerability. 
Please feel free to prove me wrong by hacking me."

U said:
In order to actually exploit this issue you would need to find an XSS vulnerability. 

But Let me tell u that it doesn't require XSS to exploit. Insecure HTTPOnly cookies require XSS.
It requires MITM(Man-In-The-Middle) Attack to steal that cookie.

I submit this report only for your comment "Please feel free to prove me wrong by hacking me."

Thanks
Cheers
Anas

## Impact

Attacker may steal session cookie through MITM.

## Attachments
No attachments
