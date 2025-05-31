# Partial disclosure of undisclosed programs through <meta> tags

## Report Details
- **Report ID**: 302620
- **URL**: https://hackerone.com/reports/302620
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-01-05T08:29:05.519Z
- **Disclosed**: 2018-01-11T04:45:49.894Z

## Reporter
- **Username**: bigbug
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary**

Report pages contain <meta> tags that contains the description of the report. New browsers create thumbnails of recently visited pages that that display the content of the <meta description> tags. Since the meta tags contain the contents of report, private report contents are partially disclosed.     


**Description**

Modern browsers create thumbnails of visited pages along with the content provided in the <meta> tags.

It was seen that all private report pages contain <meta> tags with **description** attribute as the actual content of the report. When browser creates a thumbnail of this page, it also contains private content of the undisclosed program.

**Browser Used**

+ Tested on Firefox 57.0.4

**Steps followed**

Demonstration includes a test program

1. Sign in. Click on inbox. Right click on any private/undisclosed program and click *Open Link in New Tab*. Make sure to open link in new tab else the report will open in the container itlsef.


1. Note the content of the report. I used a test report - https://hackerone.com/reports/302447 {F251580} 


1. Right click and click *View Page Source* {F251581}   As we can see in the image the description contains the content of actual report.


1. Click on new tab. Under hihglghts tab you will be able to see the thumbnail with actual Report id, Report title and Report content. **Note** - This is tested on firefox 57.0.4. Features may differ on other browsers. {F251583}  


Also attaching a POC video demonstrating the same. The video demonstrates above steps using firefox 57.0.4.

## Impact

Leak contents of undisclosed reports.

## Attachments
- m1.PNG
- m2.PNG
- m3.PNG
