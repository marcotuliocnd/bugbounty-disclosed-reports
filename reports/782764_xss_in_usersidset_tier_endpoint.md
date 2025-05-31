# xss in /users/[id]/set_tier endpoint

## Report Details
- **Report ID**: 782764
- **URL**: https://hackerone.com/reports/782764
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-24T19:03:14.075Z
- **Disclosed**: 2020-01-25T07:27:32.522Z

## Reporter
- **Username**: gabriel-kimiaie
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ratelimited

## Vulnerability Information
## Summary:
[add summary of the vulnerability]
Hello there ! I found an XSS since you forgot to add the json content-type response header right there:
https://github.com/gtsatsis/RLAPI-v3-OOP/blob/508d3c610ccc9076753bdc81151a5e8d76871a3e/src/Controller/UserController.php#L93
The tier parameter is therefore returned with the wrong Content-Type (text/html).
I have been able to verify the existance of the XSS.
Note that you can bypass the '\' added to both " & / by using comments such as:
## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Deploy to a test instance
  2. Create one admin user with correct api key filled in the database
  3. the /users/[id]/set_tier "tier" POST parameter is vulnerable to XSS injection.

## Supporting Material/References:


  * Selection_033.png =>burp capture attached

## Impact

Reflected cross site scripting should be fixed, as an user might be able to steal cookies/escalate privileges.

## Attachments
- Selection_033.png
