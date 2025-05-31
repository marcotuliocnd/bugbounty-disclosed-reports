# Local File Inclusion In Registration Page

## Report Details
- **Report ID**: 1007799
- **URL**: https://hackerone.com/reports/1007799
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-10-13T23:23:56.819Z
- **Disclosed**: 2020-11-23T18:27:36.444Z

## Reporter
- **Username**: moloshy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
When registering on https://████████ it is possible to use path traversal characters in a parameter allowing an attacker to read local files.

**Description:**
The registerUserInfoCommand.nextPageName parameter within the registration form is vulnerable to file path manipulation, where it is possible to submit a request containing path traversal characters (e.g. ../../../) followed by a local file, which will return the contents of the file. This can be used to read local files including sensitive configuration files such as /WEB-INF/web.xml, /WEB-INF/app-config.xml and /WEB-INF/spring/explicit-security-config.xml.

## Impact
An attacker could read local files on the web server that they would normally not have access to, such as the application source code or configuration files containing sensitive information on how the website is configured. 

## Step-by-step Reproduction Instructions

1. Browse to https://██████/████████/register/RegisterUserInfo.htm
2. Setup an intercepting proxy (e.g. BurpSuite) and click Next, catching the request in Burp (don't worry about filling out the form fields)
3. For ease here I would recommend copying and pasting the below parameters into the request, replacing the parameters that were there originally.  This request will fetch the /WEB-INF/web.xml configuration file, I have also attached two other requests which grab app-config.xml and explicity-security-config.xml. Once the parameters are there, forward the request to the server and you should see the web.xml file.  

```
registerUserInfoCommand.organization=Chantest+Corporation&registerUserInfoCommand.organizationId=49800&registerUserInfoCommand.currPageName=SearchUserOrgInfo.jsp&registerUserInfoCommand.nextPageName=..%2f..%2f..%2fWEB-INF%2fweb.xml&registerUserInfoCommand.prevPageName=jsp%2FRegistration%2FRegisterAccountInfo.jsp&registerUserInfoCommand.submitButton=Choose+This+Organization+and+Continue+%3E
```

## Product, Version, and Configuration (If applicable)
N/A

## Suggested Mitigation/Remediation Actions
Rather than placing the filename of the next page directly in a parameter, it would be better to maintain a whitelist of acceptable filenames and use a unique corresponding identifier to access the file. Then any request containing an invalid identifier can just be rejected. Additionally, you could also sanitise any path traversal characters that may be present in a request.

## Impact

An attacker could read local files on the web server that they would normally not have access to, such as the application source code or configuration files containing sensitive information on how the website is configured.

## Attachments
No attachments
