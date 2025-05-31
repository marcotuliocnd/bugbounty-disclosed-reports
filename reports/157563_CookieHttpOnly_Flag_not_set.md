# Cookie:HttpOnly Flag not set

## Report Details
- **Report ID**: 157563
- **URL**: https://hackerone.com/reports/157563
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-08-08T07:36:46.577Z
- **Disclosed**: 2016-08-08T15:00:38.071Z

## Reporter
- **Username**: akanshaminti
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
A cookie has been set without the HttpOnly flag, which means that the cookie can be accessed by
JavaScript. If a malicious script can be run on this application then the cookie will be accessible and can
be transmitted to another site.

## Attachments
- HttpOnly_not_set.png
