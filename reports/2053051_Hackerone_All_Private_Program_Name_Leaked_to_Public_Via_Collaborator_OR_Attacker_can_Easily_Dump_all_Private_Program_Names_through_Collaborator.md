# Hackerone All Private Program Name Leaked to Public Via Collaborator OR Attacker can Easily Dump all Private Program Names through Collaborator 

## Report Details
- **Report ID**: 2053051
- **URL**: https://hackerone.com/reports/2053051
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-07-06T14:41:08.343Z
- **Disclosed**: 2023-08-11T13:43:22.464Z

## Reporter
- **Username**: hackit_bharat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi Team,

I hope you are doing well.

I found a Critical Vulnerability using this attacker can easily dump all the private program names of Hackerone and it breaks the confidentiality because if attacker got name of the program Rest of the Data is not needed because it's googleable about the program.

I found that Using Collaborator Feature attacker can easily got all Program's Names one by one or he can automate through Burp Intruder.

Steps to Reproduce :- 1. Create a Report on Hackerone in which Collaboration is allowed.
2. After creating it add a Random Collaborator and Capture this Request in Burp suite.
3. In the Request there is `report_id` change this id to `2052164`.
4. You got this error if program is Public :- 

█████

5. Now change this `report_id` change this id to `2052163 ,  2052158 , 2052154 , 2052162 , 2053029`.
6. As these all `report_id ` belongs to private programs you got leaked Name of Private program Like :- 

██████

█████████

7. Attacker can easily Brute-Force through intruder and Dump the whole DB of Private Hackerone program Name this breaks the Confidentially of Private program because if Someone known name he can easily google and find it the information about it.

## Impact

1. Broken Confidentiality of Hackerone Feature about Private Programs.
2. Attacker can easily dump all the Private program Names and it also breaks the Confidentiality between Hackerone and Client.

POC Attached

If you need further info I am here to help you.

Thanks and Regards,
BhaRat

## Attachments
No attachments
