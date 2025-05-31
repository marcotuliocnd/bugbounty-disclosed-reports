# HTML injection on newsroom.snap.com/* via search?q=1

## Report Details
- **Report ID**: 2018615
- **URL**: https://hackerone.com/reports/2018615
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-06-08T20:23:08.358Z
- **Disclosed**: 2023-08-14T16:46:05.200Z

## Reporter
- **Username**: jotita3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
Hi security team members,

Hope you are well!

I found an unauthenticated HTML injection in the browser of NewRooms section: https://newsroom.snap.com/[code_country]/*. It is possible to inject any HTML code from the "?q=" parameter of the following endpoints newsroom.snap.com/[code_country]/search?q= since the text input in the search engine is not sanitized at all.

The steps to reproduce the attack are:

1. Inject any HTML code into the URL: https://newsroom.snap.com/es-ES/search?q=%3Ca%20style=%22position:absolute;margin:50px;%20background-color:%20yellow;%20z-index:1000;top:50px;padding:100px;font-weight:bold;font-size:45px;color:red;%22%20href=%22https://evil.com%22%3EClick%20here%20for%20win%201000%E2%82%AC!%3C/a%3E

2. In this PoC example, an attacker would send this seemingly legitimate URL to victims pretending that Snapchat is offering money as an excuse. In reality, these users would access the attacker's website (https://evil.com/) if they click on the <a></a> element.

## Impact

An attacker can inject as much HTML code as desired and edit the style of the website to cause a Defacement in order to deceive users through Phishing, links to other websites controlled by the attacker through scams,... . There are many scenarios .

## Attachments
- htmlinjection.png
