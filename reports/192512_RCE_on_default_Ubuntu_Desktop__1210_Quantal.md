# RCE on default Ubuntu Desktop >= 12.10 Quantal

## Report Details
- **Report ID**: 192512
- **URL**: https://hackerone.com/reports/192512
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2016-12-19T19:08:28.034Z
- **Disclosed**: 2019-11-12T23:49:19.620Z

## Reporter
- **Username**: donnchac
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I recently reported a number of vulnerabilities in Canonical's Apport crash report software. These bugs provided RCE on a default install of Ubuntu Desktop >= 12.10 upon opening a malicious file. I reported the issues to the Apport maintainers and we coordinate the disclosure of these issues. 

Is the Internet Bug Bounty interested in providing bounties for RCE bugs affecting default Ubuntu installations? I have included a link to the Launchpad ticket and my blog post describing the issues in detail. Please let me know if this is something that you are interested in. I am happy to provide any further information that you require. 

https://bugs.launchpad.net/bugs/1648806
https://donncha.is/2016/12/compromising-ubuntu-desktop/

## Attachments
- minimal-rce.crash
