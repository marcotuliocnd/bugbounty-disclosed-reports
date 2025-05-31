# User enumeration through forget password

## Report Details
- **Report ID**: 1166054
- **URL**: https://hackerone.com/reports/1166054
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-04-15T21:54:00.995Z
- **Disclosed**: 2021-05-16T01:59:36.203Z

## Reporter
- **Username**: mohanad987
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
Vulnerability:-
->User enumeration is possible through forgot password feature.
steps to reproduce:-
->Go to the above selected domain and go to forgot password.
->submit random email and then intercept request  by burp suit 
->in response you will get { HTTP/1.1 500 Internal Server Error with {{"err":"No account with that id found."} } 

Remediation:-
->It should display like "if that mail address exists in our system, then we will send password reset link."
I hope that you will consider this issue as you also welcome the reports of best practices.
Thank you

## Impact

Leaking users' emails. / Information Disclosure.

## Attachments
No attachments
