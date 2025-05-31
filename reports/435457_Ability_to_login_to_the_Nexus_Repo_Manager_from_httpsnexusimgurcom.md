# Ability to login to the Nexus Repo Manager from https://nexus.imgur.com/ 

## Report Details
- **Report ID**: 435457
- **URL**: https://hackerone.com/reports/435457
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-11-07T02:32:40.014Z
- **Disclosed**: 2018-12-13T19:02:43.939Z

## Reporter
- **Username**: sbakhour
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: imgur

## Vulnerability Information
Hello Imgur Administrators,

I am not sure if this falls in your scope but I wanted to alert you that your Nexus Repository Manager can be accessed through https://nexus.imgur.com/
Usually the default user/pass for the NRM are admin/admin123 but there is an alternative way to login using the below default credentials.
user: anonymous
pass: anonymous

I was able to login and I got access to check all the repositories available. I uploaded the attached video as a proof of traversal.
Kindly arrange to remove the user anonymous or change its password & limit the access to the Nexus Repo Manager site https://nexus.imgur.com/

## Impact

The attacker can manage to proxy, collect, and manage your dependencies (delete components & Analyze applications).

## Attachments
- Nexus_Repo_Manager_IMGUR.mp4
