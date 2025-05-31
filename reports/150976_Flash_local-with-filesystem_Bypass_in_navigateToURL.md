# Flash “local-with-filesystem” Bypass in navigateToURL

## Report Details
- **Report ID**: 150976
- **URL**: https://hackerone.com/reports/150976
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-12T19:56:24.819Z
- **Disclosed**: 2019-10-17T20:08:04.985Z

## Reporter
- **Username**: irsdl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
This issue has been patched by Adobe: https://helpx.adobe.com/security/products/flash-player/apsb16-25.html
(CVE-2016-4178)


Flash “local-with-filesystem” policy can be bypassed using the “navigateToURL” function. 

It is not possible to target the local files using a Flash file in a website using normal methods such as the “file://” protocol or the “\\localhost\c$” path due to the Flash “local-with-filesystem” security policy.

However, a method was found that could bypass this protection. For instance the following payload could be used to open the Windows directory in the C drive:
\\.\localhost/c:\windows\

Example (should be tested in IE):
http://0me.me/demo/xss/flash/link_protocol_test.swf?input=\\.\localhost/c:\windows\

It was possible to open local files and directories in an Iframe as well. The following old PoC page can be used for this purpose:
http://0me.me/demo/xss/flash/iframe_link_protocol_test.html
The “link_protocol_test.swf?input=\\.\localhost/c:\windows\starter.xml” payload can be used as an example in the “Custom Address” field of this HTML page.

Note: This will only work in Internet Explorer as other browsers do not allow Flash to access local filesystem.

Note: Other vectors: "\\.\/C:\" or "\\.\/\\.\\..\C:\" also reported to Adobe afterwards. These payloads were discovered by Matthew Evans from NCC Group.

History before reporting this issue:
Similar issues were reported to Adobe a few years ago by a number of security researchers after this blog post was published by me: https://soroush.secproject.com/blog/2013/10/catch-up-on-flash-xss-exploitation-part-2-navigatetourl-and-jar-protocol/


## Attachments
No attachments
