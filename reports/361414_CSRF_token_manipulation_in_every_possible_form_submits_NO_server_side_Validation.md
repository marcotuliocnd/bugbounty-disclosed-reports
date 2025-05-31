# CSRF token manipulation in every possible form submits. NO server side Validation

## Report Details
- **Report ID**: 361414
- **URL**: https://hackerone.com/reports/361414
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-06-03T22:02:05.112Z
- **Disclosed**: 2018-06-04T16:16:00.589Z

## Reporter
- **Username**: mah1ndra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
Web Application is generating  CSRF_token values inside cookies
which is not a best practice for web applications the revelation of cookies can reveal CSRF Tokens as well.
Authenticity tokens should be kept separate from cookies and should be isolated to change operations in the account only.

Multiple CSRF token manipulation found across liberapay in possible form submits
1. Both signup and login.
2.After logging in. In profile section: All the following sections are vulnerable. =>Name, Avatar, Currencies,   
 Goal, Statement, Accounts ElseWhere, Privacy. Their URLs
> https://liberapay.com/<username>/edit/username 
>https://liberapay.com/<username>/edit/avatar
>https://liberapay.com/<username>/edit/currencies
>https://liberapay.com/<username>/edit/goal
>https://liberapay.com/<username>/edit/statement
>https://liberapay.com/<username>/edit/elsewhere
>https://liberapay.com/<username>/edit/privacy

3. In Account Elsewhere section. We can link all other platforms and delete them. CSRF token manipulation can be done while deleting them. Cause no server check.
4. In About > teams  section: where we can create teams also vulnerable to CSRF token Manipulation.
URL: https://liberapay.com/about/teams
5. Liberapay Donation section is also Vulnerable to CSRF token Manipulation.
URL: https://liberapay.com/Liberapay/donate 
6. Settings > password change: also vulnerable to CSRF token Manipulation.
URL: https://liberapay.com/<username>/settings/ 
7. In Identity Section: where we can Submit 1.Personal info 2.Organisation Info 3. Legal Representation details.
URL: https://liberapay.com/<username>/identity  
8. Emails & Notifications sections: where we can add emails and update notification options through checkboxes are vulnerable to CSRF token Manipulation.
URL: https://liberapay.com/<username>/emails/ 
9. Creating new communities section: Where we can create new communities. It is also Vulnerable to CSRF token Manipulation.
URL: https://liberapay.com/for/new

## Impact

The CSRF token Which is inside cookie can be manipulated with proxies. So CSRF tokens can be manipulated.

 The server application is not verifying the existence and correctness of CSRF token before processing the request.
Actually, It should be verified on the server application and If the token is missing or incorrect, the request should be rejected.
This can probe to serious issues if exploited.

A detailed POC Video is uploaded below.
Thank you.

## Attachments
- liberapay.mp4
