# Subdomain misconfiguration [mail.legalrobot.com]

## Report Details
- **Report ID**: 250766
- **URL**: https://hackerone.com/reports/250766
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-07-18T08:14:45.944Z
- **Disclosed**: 2017-07-31T01:46:28.610Z

## Reporter
- **Username**: dilip_prakash
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hi Team,

You subdomain mail.legalrobot.com has a CNAME record that resolved to ghs.google.com and shows error when navigating to subdomain,
should remove CNAME entry for that subdomain pointing towards ghs.google.com.I couldn't verify the domain ownership process to fully takeover subdomain.
mail.legalrobot.com canonical name = ghs.google.com
For POC i have claim the domain of gsuite account using mail.legalrobot.com

Fix:
To fully resolve the issue you need to remove the CNAME record and put in place a web forwarding rule for mail.legalrobot.com towards new web landing page.

Please find the attachment of POC.

Thanks 
_prakash


## Attachments
- legal_verify.png
- le_cname.png
