#  Github Account hijack through broken link in developer.twitter.com

## Report Details
- **Report ID**: 1031321
- **URL**: https://hackerone.com/reports/1031321
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-11-11T06:59:11.886Z
- **Disclosed**: 2021-02-04T06:25:16.411Z

## Reporter
- **Username**: milankatwal99
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Description
A link in    https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries   was broken and anyone could create that account which leads to account impersonate

Steps To Reproduce
1) Visit https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries
2) Scroll down to Javascript/Node.js and click on by @HunterLarco (v2)
3)  Create github username HunterLarcol
4) When someone visits and scroll down to  javascript/Node.js and click on @HunterLarco (v2). They are redirected to my account

similar report
https://hackerone.com/reports/265696



To solve this issue 
put this link https://github.com/HunterLarco

Please let me know if you have any questions. I am happy to help

## Impact

Impact
The users are coming from developer.twitter.com So, the attacker can put malicious content on the github  and many users will be the victim for example https://github.com/HunterLarcol/twitter-v2. Moreover it leads to the loss in the reputation of the company

## Attachments
- developer_twitter.jpg
- account.jpg
- profile1.jpg
- profile.jpg
