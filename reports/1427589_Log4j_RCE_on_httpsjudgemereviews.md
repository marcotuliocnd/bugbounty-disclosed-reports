# Log4j RCE on https://judge.me/reviews

## Report Details
- **Report ID**: 1427589
- **URL**: https://hackerone.com/reports/1427589
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-12-15T10:30:12.992Z
- **Disclosed**: 2021-12-21T08:57:29.170Z

## Reporter
- **Username**: bhishma14
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: judgeme

## Vulnerability Information
Summary:
CVE-2021-44228, also named Log4Shell or LogJam, is a Remote Code Execution (RCE) class vulnerability. If attackers manage to exploit it on one of the servers, they gain the ability to execute arbitrary code and potentially take full control of the system.
What makes CVE-2021-44228 especially dangerous is the ease of exploitation: even an inexperienced hacker can successfully execute an attack using this vulnerability. According to the researchers, attackers only need to force the application to write just one string to the log, and after that they are able to upload their own code into the application due to the message lookup substitution function.

Supporting Material/References:
Picture and Logs was Uploaded as a proof.

https://www.tenable.com/blog/cve-2021-44228-proof-of-concept-for-critical-apache-log4j-remote-code-execution-vulnerability

Remediation:
Update the log4j jar to 2.15 or 2.16

## Impact

Successful attack leads Arbitary Code Execution on the application

## Attachments
- Judgeme_1.png
- Judgeme_2.png
- Judgeme_3.png
