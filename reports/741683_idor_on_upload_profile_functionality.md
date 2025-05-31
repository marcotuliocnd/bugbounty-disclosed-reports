# idor on upload profile functionality 

## Report Details
- **Report ID**: 741683
- **URL**: https://hackerone.com/reports/741683
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-11-20T08:50:00.444Z
- **Disclosed**: 2020-05-14T17:12:54.195Z

## Reporter
- **Username**: risinghunter
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Vulnerable URL: https://██████████/███████ID/#Common/EditOne/Person/{account_id}
steps to reproduce:
1).browse the image and click on the upload button
2).capture this request in burp suite 
3). change the value 'personId' parameter to account2 account_id 
(please see screenshot1)
4).then goes to account2, then you will see the uploaded image is successfully goes to the approved tab 

please see video attach below you will understand completely

## Impact

an attacker is able to change profile image of any user

## Attachments
No attachments
