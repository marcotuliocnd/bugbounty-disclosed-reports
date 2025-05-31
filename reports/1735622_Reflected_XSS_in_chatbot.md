# Reflected XSS in chatbot

## Report Details
- **Report ID**: 1735622
- **URL**: https://hackerone.com/reports/1735622
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-10-14T14:27:13.365Z
- **Disclosed**: 2022-11-19T15:56:51.530Z

## Reporter
- **Username**: roland_hack
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
Reflected XSS attacks, also known as non-persistent attacks, occur when a malicious script is reflected off of a web application to the victim's browser. The script is activated through a link, which sends a request to a website with a vulnerability that enables execution of malicious scripts
Proof of Concept
1)Go to the website https://mtn.com.gh/
2)click on the MTN chat and where it asks to enter a number enter an xss payload
3)In my case I put the following payload:<button onClick="alert('xss')">Submit</button>

## Impact

If an attacker can control a script running in the victim's browser, they can usually completely compromise that user. Among other things, the attacker can: Perform any action in the application that the user can perform.

## Attachments
- mtn_chatbot_xss_2.png
- recording-1665764779722.webm
