# Session cookie missing SecureFlag on git.edoverflow.com.

## Report Details
- **Report ID**: 345166
- **URL**: https://hackerone.com/reports/345166
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-04-30T20:01:07.995Z
- **Disclosed**: 2018-05-03T14:41:43.943Z

## Reporter
- **Username**: tangent90ninety
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ed

## Vulnerability Information
Assigned to:-ED
Assigned by:- Kirtikumar Anandrao Ramchandani
Assigned on:- 01/05/2018
Bug overview:- Session Cookie without secure flag.
Cookie Name:- _gitlab_session
Description:-Risk description:
Since the Secure flag is not set on the cookie, the browser will send it over an unencrypted channel (plain HTTP) if such a request is made. Thus, the risk exists that an attacker will intercept the clear-text communication between the browser and the server and he will steal the cookie of the user. If this is a session cookie, the attacker could gain unauthorized access to the victim's web session. 
Recommendation:I recommend reconfiguring the web server in order to set the flag(s) Secure to all sensitive cookies. 
Reference:-https://blog.dareboost.com/en/2016/12/secure-cookies-secure-httponly-flags/.

Impact
The secure flag is an option that can be set by the application server when sending a new cookie to the user within an HTTP Response. The purpose of the secure flag is to prevent cookies from being observed by unauthorized parties due to the transmission of a the cookie in clear text.
To accomplish this goal, browsers which support the secure flag will only send cookies with the secure flag when the request is going to a HTTPS page. Said in another way, the browser will not send a cookie with the secure flag set over an unencrypted HTTP request.
By setting the secure flag, the browser will prevent the transmission of a cookie over an unencrypted channel.
Thank you very much sir :) whatever you can award it will be a great honour for me to secure your website at just age of 15. Once again thank you very much and have a tip: I had learned we should never apologlize if we have learned any lesson. Have a great day and have a great day,

Kind regards,
Kirti

## Impact

The secure flag is an option that can be set by the application server when sending a new cookie to the user within an HTTP Response. The purpose of the secure flag is to prevent cookies from being observed by unauthorized parties due to the transmission of a the cookie in clear text.

## Attachments
No attachments
