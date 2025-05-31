# Self XSS in Create New Workspace Screen

## Report Details
- **Report ID**: 1442017
- **URL**: https://hackerone.com/reports/1442017
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-01-05T20:10:50.045Z
- **Disclosed**: 2022-02-20T09:08:08.589Z

## Reporter
- **Username**: unnamedx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mattermost

## Vulnerability Information
Hi team,
I have found an vulnerability on your website .
step to reproduce :

1.firstly i want to say sorry for this .please read carefully
when im testing on your website .i was redirected to  : https://customers.mattermost.com/cloud/connect-workspace
2.then navigate to create new workspace 
3.on workspace name input this payload : "/><img src=x onerror=alert(document.cookie)>
4.xss will trigger 

I know this domain is in out of scope ,but attacker can steal user cookies . I dont want any rewards for this i just want to aware you guys for this vulnerability .Hope you can understand .
Thanks for reading my report

## Impact

attacker can steal user cookies

## Attachments
- simplescreenrecorder-2022-01-06_01.09.57.mkv
