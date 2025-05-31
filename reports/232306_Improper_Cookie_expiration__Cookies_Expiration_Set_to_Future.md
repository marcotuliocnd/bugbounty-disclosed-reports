# Improper Cookie expiration | Cookies Expiration Set to Future 

## Report Details
- **Report ID**: 232306
- **URL**: https://hackerone.com/reports/232306
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-26T20:37:56.115Z
- **Disclosed**: 2017-08-31T09:50:11.424Z

## Reporter
- **Username**: sadhu16
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi Team,
I have found at many instances or places from signup till getting logged into application ( in domain "demo.weblate.org"  ) that session maintaining cookies such as csrf token and session id's expiration dates are set to future date. As part of secure session management one should prohibit or avoid the use of persistent cookies specially for those cookies which contain sensitive information.Ideally application should use only cookies of non persistent nature.

Here Application is setting cookie expiration to future date.

Here an adversary may get an access to victim's cookies (session ids and csrf token ) and can reuse them in further getting valid session on behalf of them or he can directly use them for any activity which cause harm to victims.

Attached screenshots for reference please see them.


See the below mentioned link for details:

https://www.owasp.org/index.php/Testing_for_cookies_attributes_(OTG-SESS-002)





## Attachments
- Session_Id_expiration_date_is_set_to_future_date.png
- Session_Id_expiration_date_is_set_to_future_date-1.png
- Session_Id_expiration_date_is_set_to_future_date-2.png
- Session_Id_expiration_date_is_set_to_future_date-3.png
