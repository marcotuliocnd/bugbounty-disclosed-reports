# SSRF on local storage of iOS mobile

## Report Details
- **Report ID**: 746541
- **URL**: https://hackerone.com/reports/746541
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-11-26T10:37:16.194Z
- **Disclosed**: 2020-03-01T10:29:39.050Z

## Reporter
- **Username**: l0l1ch3ng
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
1. The tester uploaded the text file, containing "test ssrf" message, in order to proof SSRF attack.
2. Next, the tester uploaded the common file and then manipulate the content and extension file to html format in order to find the application path: <svg/onload=document.write(document.location)> 
3. The tester access that file and found the application path to use for SSRF local file disclosure.
4. Then, the tester uploaded the common file and then manipulate the content and extension file to html format in order to view the local file via SSRF attack: <iframe src="file://.../ssrfpoc.txt" width="400" height="400"></iframe> 
5. The tester access that file and found that this application allow you to access and read the local file successfully.

## Impact

This allow anyone to use other URLs such as that can access documents on the system/application (using file://) a.k.a Sensitive Data Exposure.

## Attachments
- Step_1.PNG
- Step_2.png
- Step_3.PNG
- Step_4.png
- Step_5.PNG
