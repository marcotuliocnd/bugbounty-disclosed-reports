# [marketplace.informatica.com] Persistent XSS through document title

## Report Details
- **Report ID**: 181816
- **URL**: https://hackerone.com/reports/181816
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-12T19:57:22.548Z
- **Disclosed**: 2017-02-02T04:29:44.457Z

## Reporter
- **Username**: kasperkarlsson
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
Document titles are not properly escaped before being printed on https://marketplace.informatica.com/docs/ . By including a payload in a document title, an attacker can create a document with a persistent XSS vector which executes for anyone viewing the document page.

Proof of concept
===
The following steps are accompanied by screenshots attached to this report.

1. Log into https://marketplace.informatica.com/ and go to your profile page. Select New -> Document.
2. Choose a location for your new document - "Your Documents" will work just fine.
3. Enter some text in the document body and insert the following XSS vector in the document title: `";alert("XSS in "+document.domain);//`
4. Hit "Publish" on the bottom of the page.
5. Visiting the document page causes the XSS payload to execute.

This test was performed using Mozilla Firefox 49.0.2 and was also confirmed in Google Chrome 54.0.2840.87. The exploit should work in any browser, as the persistent payload cannot be distinguished from a legitimate script from the server.

Recommended solution
===
Make sure to correctly output encode the document title before printing it to a javascript scope of the document page.

## Attachments
- 1_new_document.png
- 2_new_document.png
- 3_payload.png
- 4_publish.png
- 5_xss.png
