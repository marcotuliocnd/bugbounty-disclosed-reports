# Insecure Invitation Link Handling

## Report Details
- **Report ID**: 2586433
- **URL**: https://hackerone.com/reports/2586433
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-07-04T13:09:17.071Z
- **Disclosed**: 2024-10-31T11:17:21.122Z

## Reporter
- **Username**: mous_haxk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: productboard

## Vulnerability Information
## Summary:
This report outlines a critical security vulnerability in the invitation link handling process of ''satismeter.com''. The issue allows unauthorized users to join an organization using invitation links sent to different email addresses. If exploited, this vulnerability can lead to unauthorized access, privilege escalation, data breaches, and other severe impacts.
Vulnerability Details
Description
The invitation system is designed to send unique links to specific email addresses, allowing them to join an organization. However, it was discovered that these links can be used by email addresses other than the intended recipients. This flaw occurs because the system does not adequately verify that the email address using the invitation link matches the email address to which the link was sent.

NOTE:
when you want to create account it will ask for email verification, but in the scenario described down i was able to bypass verification process  

## Steps To Reproduce:
1-victim send an invitation to attacker
2-in attacker mailbox click on the invite you had received 
3-turn on burp
4-set up your password and turn the interception on
5- click signup and go to burp forward the request till you reach POST /graphql HTTP/2 with body
```
{"operationName":"SignUp","variables":{"input":{"email":"example@gmailll.com","link":null,"password":"wxxxxxxx","source":"invitation"}},"query":"mutation SignUp($input: SignUpInput!) {\n  auth {\n    signUp(input: $input)\n    __typename\n  }\n}"}
```
6-in the email parameter change the email to any email you want even one you don't own and finish signup process and you are now logged in with email that doesn't belong to you and have bypassed email verification 

## Supporting Material/References:
  * [attachment / reference]
F3410870

Recommendations
Immediate Actions
    Token Validation:
Ensure that the invitation link token is cryptographically tied to the specific email address. The token should include the email address and a unique identifier.
    Email Address Verification:
Verify that the email address of the user attempting to accept the invitation matches the email address associated with the token.
    Multi-Factor Authentication:
For high-privilege roles, require additional verification steps, such as a one-time password (OTP) sent to the invited email address.
Long-term Enhancements
    Single-Use Tokens:
Ensure that tokens are single-use and invalidate them after they are used.
    Link Expiration:
Set an expiration time for invitation links to limit their validity period.

## Impact

Potential Risks
    Unauthorized Access:
Unauthorized users can join the organization and gain access to sensitive information.
Privilege Escalation:
If the invitation grants high-privilege roles (e.g., owner), unauthorized users can perform actions restricted to these roles, potentially compromising the entire system.
Data Breach:
Confidential and sensitive data may be exposed, leading to data breaches and loss of proprietary information.
Operational Disruption:
Unauthorized changes to configurations, deletion of data, or disruption of services can impact business operations.
Email verification bypass.

## Attachments
- bandicam_2024-07-04_13-40-31-849.mp4
