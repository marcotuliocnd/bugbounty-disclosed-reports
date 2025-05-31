# disable test send feature if user's email address isn't verified

## Report Details
- **Report ID**: 906226
- **URL**: https://hackerone.com/reports/906226
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-06-23T16:04:24.378Z
- **Disclosed**: 2020-06-30T00:28:18.131Z

## Reporter
- **Username**: vaalici
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: trycourier

## Vulnerability Information
## Summary:
There is no mechanism to limit the request in places while send the preview email

## Steps To Reproduce:
There is a weak account registration process, which allow user to register and login without any email confirmation.
L'say say for example that i'm the user A that want to send a phishing email or perform DOS against a targeted user

  1. Registration process by using the victim email address
  2. Craft the email example 
  3. Proced with the sent to me functionality to try the email send
  4. Intercept the request with a Proxy (Burp)
  5. Resend the request any times you want 

## Supporting Material/References:

CWE-400: Uncontrolled Resource Consumption
https://cwe.mitre.org/data/definitions/400.html

Below i have attached the evidence for the POC

## Impact

The most common result of resource exhaustion is denial of service.

## Attachments
- email_dos_0.PNG
- email_dos_1.PNG
- email_dos_2.PNG
