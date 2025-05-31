# Blind stored XSS due to insecure contact form at https://█████.mil leads to leakage of session token and 

## Report Details
- **Report ID**: 1036877
- **URL**: https://hackerone.com/reports/1036877
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-11-17T16:35:52.709Z
- **Disclosed**: 2021-01-25T19:53:39.164Z

## Reporter
- **Username**: ahmedelmalky
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Summary:
I have discovered a blind stored cross site scripting vulnerability due to an insecure Contact form available here  https://███████.mil/  This form does not properly sanitize user input allowing for the insertion and submission of dangerous characters such as angle brackets. I was able to submit a blind xss payload through the form which was triggered in backend /admin panel.
##Steps To Reproduce:
1-Browse to the page at https://██████.mil/and fill out the contact form submitting your blind XSS payload in First name , Last name, Company and description field.
2-Submit the form and have and admin access the information.
3-This will trigger XSS in the admin panel and a notification to the XSS hunter service with details of the event.

##Supporting Material/References:
(the screenshot )[██████████]

The IP address that triggered the XSS payload is  ████████ 

Xss hunter Report █████████

## Impact

An attacker is able to access critical information from the admin panel. The XSS reveals the administrator’s IP address, backend application service, titles of mail chimp customer and internal subscription emails, admin session cookies.
An attacker can exploit the above cookies to access the admin panel.

## Attachments
No attachments
