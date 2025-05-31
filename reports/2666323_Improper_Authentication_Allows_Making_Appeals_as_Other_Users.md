# Improper Authentication Allows Making Appeals as Other Users

## Report Details
- **Report ID**: 2666323
- **URL**: https://hackerone.com/reports/2666323
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-08-16T09:29:30.222Z
- **Disclosed**: 2025-02-12T20:51:35.115Z

## Reporter
- **Username**: roseh4cks
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
### Note: I am submitting reports for each affected endpoint as requested by the program.
 
This vulnerability allows unauthenticated users to submit appeals by manipulating HTTP responses. By changing server responses from a redirect (302) to a successful response (200), attackers can bypass the application's authentication requirements and perform actions reserved for logged-in users. This can lead to unauthorized submissions, email spoofing, and potential exploitation of the application's workflow. The flaw undermines both the security and integrity of the application, posing significant risks to user data and trust.

## Impact

Submit requests as other users of the application, impacting the integrity of the system and the confidentiality of information on its users.

## System Host(s)
██████████.mil

## Affected Product(s) and Version(s)
PAL V: ?

## CVE Numbers


## Steps to Reproduce
Note: I included a video for another URL and endpoint, but the steps to reproduce are the same. Only changes will be the URL and endpoint.

1. Capture a GET  request to endpoint "/App/createappeal.aspx"
2. Forwarded the request and intercept the server's response. 
3. After intercepting the response, change the 302 to a 200 response and forward the modified request to the browser.
4. From this point, fill in the required fields, intercepting and modifying the response for several of the dropdown selections as well in order to be able to proceed.
5. For the email field, we are able to input the email address of another application user.

### Note: An unauthenticated user can validate emails using the following URL:
/app/CreateAppeal.aspx?email=turbul3nce@wearehackerone.com

After supplying an email and filling in the required fields, submit the request. As a result, an email will be sent to the victim's email address verifying successful submission.

## Suggested Mitigation/Remediation Actions
To remediate this vulnerability, the application should enforce strict authentication checks on all requests to sensitive endpoints, ensuring that only authenticated users can access them. Additionally, responses should be validated on the server side to prevent unauthorized manipulation of HTTP status codes. Implementing these measures will ensure that only legitimate, authenticated users can perform actions like submitting requests.



## Attachments
No attachments
