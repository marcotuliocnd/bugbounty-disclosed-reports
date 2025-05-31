# brute force attack allowed on admin page https://www.stellar.org/wp-admin/

## Report Details
- **Report ID**: 342977
- **URL**: https://hackerone.com/reports/342977
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-04-25T03:08:06.911Z
- **Disclosed**: 2020-02-23T16:21:28.604Z

## Reporter
- **Username**: abo-jehad
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stellar

## Vulnerability Information
hi security team
-due to your bug bounty program , i found basic authentication method
-by doing many trials the server will response and will not block the logging process
- the attack can be automated by burp intruder till getting access to admin page
- in second screen the request is intercepted by burp proxy
F290121:

-in third anf forth screen i used burp intruder to automate  bruit force attack (i tried only 9 times to make POC)
F290122:
F290123:

## Impact

if the attack coleted , admin page is accessed

## Attachments
- 2018-04-24_23_57_22-401_Authorization_Required.png
- 2.png
- 2018-04-25_00_00_41-Intruder_attack_2.png
- 2018-04-25_00_01_05-Intruder_attack_2.png
