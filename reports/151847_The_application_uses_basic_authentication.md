# The application uses basic authentication.

## Report Details
- **Report ID**: 151847
- **URL**: https://hackerone.com/reports/151847
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-17T00:23:47.250Z
- **Disclosed**: 2016-07-18T19:53:39.463Z

## Reporter
- **Username**: roshanpty
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Basic authentication is enabled on file access requests
====================
Description
---------------------
Basic authentication is enabled on the server if we request for the direct URL of a file.  The issues of using Basic Authentication can be read here -> [OWASP: Basic Authentication](https://www.owasp.org/index.php/Basic_Authentication). Though your threat model considers brute-forcing as an acceptable risk, it is also worth noting that use of basic authentication makes the brute-force attacks much easier and faster. 

Detailed Steps
---------------------
**Step 1:** Open the browser and request for the direct URL of a file. Eg: (http://nc.hostiso.cloud/remote.php/webdav/Photos/Squirrel.jpg)
{F105383}
**Step 2:** Enter the username and password and capture the request in a proxy tool.
**Step 3:** It can be observed that the header with Base64 encoded username password is being sent in the request to server. 
{F105384}

## Attachments
- 2016-07-16_20_10_24-New_Tab.png
- 2016-07-16_20_10_59-Movies___TV.png
