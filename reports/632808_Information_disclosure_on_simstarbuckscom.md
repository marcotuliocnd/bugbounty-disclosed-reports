# Information disclosure on sim.starbucks.com

## Report Details
- **Report ID**: 632808
- **URL**: https://hackerone.com/reports/632808
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-06-30T12:11:42.971Z
- **Disclosed**: 2019-11-13T00:41:11.544Z

## Reporter
- **Username**: johnstone
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
**Description:** 
       Hi,there.I found the sim.starbucks.com host deployed the jira server which version is 7.9.2,there is many public vulnerability on this low version.

**Information disclosured vulnerability** 
1.(CVE-2019-3403)https://jira.atlassian.com/browse/JRASERVER-69242
visit the URL address,you can check the user whether is exist on this host
```
https://sim.starbucks.com/rest/api/2/user/picker?query=admin
```
So the attacker can enumerate all existing users on this jira server.

2.(CVE-2019-8442)https://jira.atlassian.com/browse/JRASERVER-69241
visit the URL address,the server will leaking some server's information
```
https://sim.starbucks.com/s/thiscanbeanythingyouwant/_/META-INF/maven/com.atlassian.jira/atlassian-jira-webapp/pom.xml
```


## Recommendations for fix
updated the jira server's version or fixed

PS:Can starbucks's team check my other report #533836 status?the report is not updated for too long.
Thank you.looking forward for your reply.
Best regards!
@johnstone

## Impact

Leaking some information about the server

## Attachments
No attachments
