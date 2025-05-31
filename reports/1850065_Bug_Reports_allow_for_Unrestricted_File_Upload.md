# [█████] Bug Reports allow for Unrestricted File Upload

## Report Details
- **Report ID**: 1850065
- **URL**: https://hackerone.com/reports/1850065
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-01-28T21:30:01.346Z
- **Disclosed**: 2023-02-24T19:07:39.166Z

## Reporter
- **Username**: b911bade858ce8e6a0f50f8
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
The web page https://███████/ allows for users to submit bug reports. Users are allowed to attach a file to a bug report. The extension and size of files are not validated by the web server.

## Impact

An attacker can attach a malicious file to a bug report. If a support agent opened the malicious file, malware would be executed on the support agent's system.

## System Host(s)
████████

## Affected Product(s) and Version(s)
Version: 3.4 Build: 35 Revision: 1

## CVE Numbers


## Steps to Reproduce
1. Navigate to the following web page: https://████████/
2. Create an account
3. Log in to the account that you created
4. Click on the text that reads `Report a Bug`
5. Enter any text in to the `Description` input field
6. Attach a file with an allowed file extension to the bug report
7. Click on the text that reads `Submit`
8. Intercept the `HTTP` request and change the extension of the attached file to one that is not allowed

Observe that the bug report was successfully submitted. This should not be the case, as the attached file has a file extension that is not allowed. The same method can be used to attach a file whose size is greater than 5 megabytes.

## Suggested Mitigation/Remediation Actions
Ensure that the extension and size of a file are validated by the web server.



## Attachments
No attachments
