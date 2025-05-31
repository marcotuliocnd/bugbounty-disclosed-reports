# Privilege Escalation From user to SYSTEM via unauthenticated command execution 

## Report Details
- **Report ID**: 544928
- **URL**: https://hackerone.com/reports/544928
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-04-22T00:58:17.010Z
- **Disclosed**: 2019-11-08T16:37:35.196Z

## Reporter
- **Username**: b0yd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
The vulnerability, or feature depending how you look at it, is the ability to execute commands using the 
evostream API interface that is exposed on localhost:7440. Since the evostream service is running as SYSTEM a user can use the launchprocess command,  http://docs.evostream.com/2.0/launchProcess.html, to execute any binary with supplied arguments. The only thing that is keeping this "feature" from allowing remote code execution is the fact that it listens on localhost only. However, if it were couple with an SSRF, an attacker could achieve full remote code execution.

## Impact

The ability to run arbitrary commands as SYSTEM from any user.

## Attachments
- poc.py
- 2019-04-21_17-47-17.mp4
