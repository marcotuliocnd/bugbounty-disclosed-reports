# Open redirect in switch account functionality

## Report Details
- **Report ID**: 390663
- **URL**: https://hackerone.com/reports/390663
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-08-05T10:40:30.222Z
- **Disclosed**: 2019-04-23T13:05:50.617Z

## Reporter
- **Username**: sumni
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: revive_adserver

## Vulnerability Information
To reproduce this vulnerability:
1. You have to be logged in user
2. Enter address: http://<your_local_installation>/www/admin/account-switch.php?return_url=http://127.0.0.1:12345/test 

This is due to unrestricted redirection url passed in in the `return_url` parameter. I would recommend to use some kind of whitelisting or a check if you are redirecting to the same domain you were before.

## Impact

This kind of open redirect vulnerabilities are used in fishing campaigns. I assume that in this case a support request containing a crafted url would have a higher chances of success. For additional malicious url obfuscation you can:
- add some unused parameters that would suggest identifiers of campaigns, other accounts and other revive specific information
- register a domain name similar to the attacked one

## Attachments
No attachments
