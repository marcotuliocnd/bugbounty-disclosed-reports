# Html injection

## Report Details
- **Report ID**: 2061049
- **URL**: https://hackerone.com/reports/2061049
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-07-10T13:29:48.944Z
- **Disclosed**: 2023-08-30T15:46:22.508Z

## Reporter
- **Username**: ped_baq
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mars

## Vulnerability Information
## Issue Description
Hypertext Markup Language (HTML) injection is a technique used to take advantage of non-validated input to modify a web page presented by a web application to its users. Attackers take advantage of the fact that the content of a web page is often related to a previous interaction with users. When applications fail to validate user data, an attacker can send HTML-fomatted text to modify site content that gets presented to other users. A specifically crafted query can lead to inclusion in the web page of attacker-controlled HTML elements which change the way the application content gets exposed to the web. 

## Issue Identified
The consultant identified that the `show` parameter can reflect into the html page, the outline below demonstrates the steps taken to exploit and reproduce.
## Risk Breakdown
- Risk: **Medium**
 
- Difficulty to Exploit: **Medium**
 
- CVSS:3.1 Score: **5.4** [(/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N)](████:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N)

## Affected URLs
 - █████


## Exploit Link
 ```html
 ██████████
 ```

## Steps to Reproduce
The following steps indicate a proof of concept outlined in three(2) steps to reproduce and execute the issue.

**Step 1:**
Open the `Exploit Link` and you will see the `special offer` with `malicious link` as shown in the image below

![alt text](███████ "malicious page")



**Step 2:**
When the user clicks on the link, redirected to the attacker's site


## References
 - [1] [snyk](███████)
 - [2] [OWASP](████████)

## Impact

Fraud and deceiving site users

## Attachments
No attachments
