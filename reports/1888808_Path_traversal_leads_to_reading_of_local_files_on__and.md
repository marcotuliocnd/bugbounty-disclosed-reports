# Path traversal leads to reading of local files on ███████ and ████

## Report Details
- **Report ID**: 1888808
- **URL**: https://hackerone.com/reports/1888808
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-02-28T07:20:22.276Z
- **Disclosed**: 2023-03-24T17:33:04.996Z

## Reporter
- **Username**: rodriguezjorgex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
The ██████████ web application has a feature that allows the downloading of files when you first go to the login screen. The endpoint that manages those downloads is the downloadForm endpoint with the filename parameter.

https://███/████/login/downloadForm?filename=█████

The filename parameter has a directory traversal vulnerability which allows an attacker to add two (2) dots and a backslash (../) to traverse parent directories and view files that are not meant to be viewed.

POC:
Viewing /etc/hosts file

Using bash, run the following command:
curl https://█████████/███/login/downloadForm?filename=../../../../../../../../etc/hosts

Or simply access the POC URL in a web browser, and the hosts file will be downloaded to the workstation.

Initially, I attempted to read the /etc/passwd file, but I believe there's some form of WAF blocking the request. I didn't attempt to bypass the WAF, but if the WAF is bypassed the /etc/passwd file contains sensitive information about the users in the system. Furthermore, with the user information, an attacker can attempt to view the id_rsa keys of users in the system to gain ssh access to the server.

## References
https://portswigger.net/web-security/file-path-traversal

## Impact

A directory traversal vulnerability that allows an attacker to read files on a system can have serious consequences, depending on the sensitivity of the information that can be accessed. Here are a few examples of the potential impact:

Disclosure of sensitive information: An attacker who can read files on a system can potentially access sensitive information such as user credentials, financial records, confidential business information, or other sensitive data. This could lead to identity theft, data breaches, or other forms of fraud.

System compromise: In some cases, directory traversal vulnerabilities can be used to read sensitive configuration files or scripts that can be used to gain full access to the system. Once an attacker has access to the system, they can execute arbitrary code, install malware, or take other actions that can compromise the system's security.

Reputation damage: If sensitive information is leaked due to a directory traversal vulnerability, it can damage the reputation of the organization responsible for the system. This can have serious consequences for businesses, particularly those in industries where trust and confidentiality are critical.
Overall, a directory traversal vulnerability that allows an attacker to read files can be a serious security risk that should be addressed as soon as possible to minimize the potential impact.

## System Host(s)
██████,███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Visit https://██████████/████/login/downloadForm?filename=../../../../../../../../etc/hosts

## Suggested Mitigation/Remediation Actions
Validate user input: One of the most common causes of directory traversal vulnerabilities is insufficient validation of user input. To prevent this, all user input should be validated to ensure that it is within expected bounds and does not contain characters that could be used to navigate outside of the intended directory.

Sanitize file paths: Before accessing files, all file paths should be sanitized to remove any characters that could be used to navigate outside of the intended directory.

Use secure coding practices: Developers should follow secure coding practices to prevent common vulnerabilities, such as directory traversal attacks. This includes using functions that are designed to handle file operations safely, such as realpath() or basename(), and avoiding the use of user input to construct file paths.



## Attachments
No attachments
