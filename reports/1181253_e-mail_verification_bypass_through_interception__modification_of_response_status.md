# e-mail verification bypass through interception & modification of response status

## Report Details
- **Report ID**: 1181253
- **URL**: https://hackerone.com/reports/1181253
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-04-30T15:12:40.843Z
- **Disclosed**: 2021-09-02T14:46:49.499Z

## Reporter
- **Username**: rptl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_vdp

## Vulnerability Information
Hi,

During registration of account at https://tams.preprod.gsa.gov, e-mail verification (code validation) can be bypassed through intercepting & modifying the response status-from "success":false to "success":true
Video {F1284281} is for reference.

##Steps To Reproduce
1. Open User Registration  Url - https://tams.preprod.gsa.gov/userEmailReg
2. Enter the email & submit.
3. Prompt to enter the verification code will appear.
4. Enter any wrong value (6 digits), submit & capture in burp.
5.Before submitting, select the option in burp - Do Intercept response to this request
6. After receiving the response. Modify the value false to true for success parameter.
7. You would be able to continue the registration process. 
8. A pop up appears in the next stage. You can close & go ahead with registration process.

## Impact

Bypass of e-mail verification processes.

## Attachments
- recording-1619794572349.webm
