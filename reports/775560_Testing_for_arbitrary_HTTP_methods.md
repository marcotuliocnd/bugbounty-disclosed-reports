# Testing for arbitrary HTTP methods

## Report Details
- **Report ID**: 775560
- **URL**: https://hackerone.com/reports/775560
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-01-15T14:42:39.337Z
- **Disclosed**: 2020-07-06T12:11:05.320Z

## Reporter
- **Username**: sandesh_shinde
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: drive_net_inc

## Vulnerability Information
Test for allowed HTTP methods on the server. Below are the steps to reproduce it.
Step 1. Navigate the url
Step 2. Intercept the GET http request using burp suite 
Step 3. change GET to ABCD as shown in screenshot and forward this request to server
Step 4. Observe the http response from the server, it shows Allow header and http methods enabled on the server

## Impact

There seems to be no major impact If the tester gets a "405 Method not allowed" or "501 Method Unimplemented", but the target application showing what methods are allowed on the server. here in this case there are PUT and DELETE methods are shown. Using this methods attacker can use exploits to get server access or file upload using PUT method.

## Attachments
- 1.PNG
