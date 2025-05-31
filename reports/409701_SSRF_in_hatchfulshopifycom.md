# SSRF in hatchful.shopify.com

## Report Details
- **Report ID**: 409701
- **URL**: https://hackerone.com/reports/409701
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-09-14T05:22:39.504Z
- **Disclosed**: 2019-04-04T13:09:45.098Z

## Reporter
- **Username**: zhurig
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
This vulnerability similar to https://hackerone.com/reports/156877 , that I found in your old version of your logo-creator.
During logo-creating process the user can select logo in  wysiwyg editor, then enter email address and wait. In this moment server send to user's browser large amount of data through websockets. Among these data there are svg files (with escaped characters ",quotation mark ) . Then, this svg-files browser send to server to convert in png, and png-files send to user through link in email.

User can change svg-files that browser send to server, and can insert own xlink:href object and :

Link to local image files, to fingerprint versions of libraries installed on server;
"Billion laughs" attack, possible DoS attack to converter server;
Try to change protocol to ftp and connect to ftp-servers;
Try to exploit vulnerabilities like "Imagetragic", or XXE

## Impact

Read files from the  server
Abuse the trust relationship between the vulnerable server and others
Retrieve sensitive information from server

Try to :
Scan the internal network to which the server is connected to
Use other image-converter vulnerabilities

## Attachments
No attachments
