# Text Only Content Spoofing on ubermovement.com Community Page

## Report Details
- **Report ID**: 153095
- **URL**: https://hackerone.com/reports/153095
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-22T07:20:53.698Z
- **Disclosed**: 2016-07-26T00:26:27.432Z

## Reporter
- **Username**: vivek-p
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Text Only Content Spoofing on ubermovement.com Community Page

Vulnerable URL:
http://ubermovement.com/community?tag=%20Stories%20have%20false%20information.%20Visit%20http://attacker.com%20for%20real%20stories.

Content Spoofing is an attack technique that allows an attacker to inject a malicious payload that is later misrepresented as legitimate content of a web application. This approach is common on error pages, or sites providing story or news entries. The content specified in this parameter is later reflected into the page to provide the content for the page. If an attacker where to replace this content with something more sinister they might be able to falsify statements on the destination website. Upon visiting this link the user would believe the content being displayed as legitimate
.
This attack exploits the trust relationship established between the user and the web site. 

The community page says about the stories from driver-partner. An attacker can specify misleading/falsified information about the stories through ‘tag’ parameter and trick the user into clicking the URL via email. This falsified information is reflected back on to the browser by the application and user consider it as a legitimate content, thereby follow the information provided by the attacker.
In this example the falsified content is directly reflected back on the same page. Please refer the attachment.
 
Valid Page: http://ubermovement.com/community?tag=Washington
Modified Page: http://ubermovement.com/community?tag=%20Stories%20have%20false%20information.%20Visit%20http://attacker.com%20for%20real%20stories.

It is recommended to allow the user to supply only trusted input using white-listing technique in order to maintain the trust between the user and web site.


## Attachments
- POC.PNG
