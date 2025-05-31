# Otp  bypass in verifying nin

## Report Details
- **Report ID**: 1314172
- **URL**: https://hackerone.com/reports/1314172
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-08-21T06:46:42.331Z
- **Disclosed**: 2022-10-17T06:27:51.044Z

## Reporter
- **Username**: mr_sparrow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:

while conducting my research in your website I found that while verifying NIN number it send the otp to the enterd mobile number that can be bypassed.

## Steps To Reproduce:

1) Go to https://nin.mtnonline.com/nin/
2) click submit nin.Now it will redirect to another page https://nin.mtnonline.com/nin/
3) It asks for mobile number and National Identity Number [NIN].
4) Enter the mobile and NIN number and click Next.It will send the otp to the mobile number.
5) Enter any 6 digit code and click verify and capture the request in bupsuite and click action and select "Do intercept and response to the request"
6) Now change the response status to success.
------>Now successfully verified mobile number.

## Impact

The attacker can able to verify NIN with any number.


Note: I had attached the poc video below please take a look.


Regards,
@aaruthra.

## Attachments
No attachments
