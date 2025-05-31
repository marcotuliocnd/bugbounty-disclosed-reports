# The software does not implement sufficient measures to prevent multiple failed authentication attempts within in a short time frame, making it more su

## Report Details
- **Report ID**: 1591504
- **URL**: https://hackerone.com/reports/1591504
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-06-05T05:14:29.461Z
- **Disclosed**: 2022-06-15T18:18:31.610Z

## Reporter
- **Username**: suryasnn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: linkedin

## Vulnerability Information
example->

String username = request.getParameter("username");
String password = request.getParameter("password");

int authResult = authenticateUser(username, password);



the security tokens can be bypassed easily , they are dont make user account safe .

//script -> check attached  file

## Impact

Technical Impact: Bypass Protection Mechanism
An attacker could perform an arbitrary number of authentication attempts using different passwords, and eventually gain access to the targeted account.

## Attachments
- request_content_valid_linkedin.txt
- httpdata_linkedin_valid_account.xml
- valid_linkedin_account.png
- successful_request_linkedin.png
- request_content_using_invalid_account.txt
- httpdata_on_invalid_account_linkedin.xml
- invalid_responces_using_invalid_account_linkedin.png
- failed_attempt.png
- script_file_to_make_login_attempt.txt
