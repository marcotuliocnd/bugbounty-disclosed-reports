# information disclosure lead to disclose users private notes

## Report Details
- **Report ID**: 1070081
- **URL**: https://hackerone.com/reports/1070081
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-01-02T08:38:24.060Z
- **Disclosed**: 2021-02-25T07:48:19.842Z

## Reporter
- **Username**: hamzadzworm
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
dear automattic 
the bug i will share with you a bug that allow attackers to access users notes without permission

the bug is here

http://simp.ly/p

and here
http://app.simplenote.com/


and its using  

web.archive.org website


web archive: is a website like google search but he save all links like you see here: 
████
███

and like you see in attached photos last notes date was in 31 december 2020 so before one day which mean this website is disclosing them

people dont want all people to access there notes the want only the people who they invite
but
http://web.archive.org/web/http://app.simplenote.com/*  and  http://web.archive.org/web/http://simp.ly/p/*


Show Notes links , you should block http://simp.ly/p/ and  http://app.simplenote.com from been on

in http://web.archive.org

because like that any one can access   them maybe (emails and passwords) they are notes they should be private  and see everything 
 just by searching about random notes
and it dosent work like that , its should be:

only people who i want them to see my notes can access them


not any random people find my notes on web.archive.org/


Short  poc video:


█████


Fix:

block  web.archive.org from disclose your websites


Note: this is not first time i found this type of bugs i already got it and it fixed many times .
so i really hope you will review that and fix it to keep your users safe because they maybe save emails or passwords or company informations and they want to share them only with company employers,  i will wait an update from you :)

## Impact

attacker can access notes without permission

## Attachments
No attachments
