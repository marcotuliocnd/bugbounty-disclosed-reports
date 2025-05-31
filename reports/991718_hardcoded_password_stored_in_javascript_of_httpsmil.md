# hardcoded password stored in javascript of https://████.mil

## Report Details
- **Report ID**: 991718
- **URL**: https://hackerone.com/reports/991718
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-09-26T00:29:16.549Z
- **Disclosed**: 2020-11-02T21:44:35.411Z

## Reporter
- **Username**: x3ph_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**

I have discovered a cleartext password stored within a javascript. This password allows me to authentication to https://█████.mil.

**Description:**

I have discovered a cleartext password stored within a javascript. This password allows me to authentication to https://███████.mil.


To confirm this vulnerability we will first navigate to https://███████.mil, you are now prompted to type a password. We will provide an incorrect password such as 'Password'.

██████████

███

We can confirm the password is invalid. However, reviewing the javascript data for '██████.chunk.js' we can confirm the authentication is validated based on a hardcoded password '█████████!'.

███████

We can now confirm if we can access the staging web app using hardcoded password.

██████

███████

## Impact

By knowing the password, it is possible to understand your password policy and structure which will encourage bruteforcing and password spray attacks in your environment.

## Step-by-step Reproduction Instructions

1. Navigate to https://█████████.mil.
2. Open your browser debugger by pressing F12.
3. Click on Network and refresh the page.
4. Open the javascript '██████████.chunk.js' and look for where the password is stored. You will see "(n=prompt("Enter Password","Password"),o="██████;" copy the password.
5. Now close out your browser debugger and refresh the page and type the password in.
6. You now have access to ████████.mil

## Suggested Mitigation/Remediation Actions

If this staging web application needs to be password protected, you can refer to the following AWS documentation on how to properly setup basic authentication https://docs.aws.amazon.com/speke/latest/documentation/authentication.html.

Resources:
https://owasp.org/www-community/vulnerabilities/Use_of_hard-coded_password

## Impact

By knowing the password, it is possible to understand your password policy and structure which will encourage bruteforcing and password spray attacks in your environment.

## Attachments
No attachments
