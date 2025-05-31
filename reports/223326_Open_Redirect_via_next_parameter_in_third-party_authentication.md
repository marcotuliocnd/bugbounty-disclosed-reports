# Open Redirect via "next" parameter in third-party authentication

## Report Details
- **Report ID**: 223326
- **URL**: https://hackerone.com/reports/223326
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-24T09:02:48.477Z
- **Disclosed**: 2017-05-17T14:17:51.878Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi,

It is currently possible to execute an open redirection attack via the `next` parameter with the inclusion of a triple-slash prefix.

## Proof of Concept
### Redirect URL
```
https://demo.weblate.org/accounts/login/github/?next=///google.com
```

After authenticating, the user will be immediately redirected to the attacker-specified target.  I believe this affects all third-party authentication providers on the Weblate platform.

Please let me know if you require any additional details regarding this vulnerability.

Thanks!

## Attachments
No attachments
