# IDOR leading unauthenticated attacker to download documents discloses PII of users and soldiers via https://www.█████████/Download.aspx?id= [HtUS]

## Report Details
- **Report ID**: 1626508
- **URL**: https://hackerone.com/reports/1626508
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-07-05T14:44:29.678Z
- **Disclosed**: 2024-06-27T17:31:00.723Z

## Reporter
- **Username**: berserker22
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Summary:
Hey team, I have found this API endpoint leads to leaking attachments and documents of users. The attachments leaked are banks taxes, contracts, PII such as full address and mobile number, emails, etc. The vulnerable URL is at [https://www.████████/Download.aspx?id=4675]

##Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Go to this URL [https://www.█████████/Download.aspx?id=4675]
  2. Add any desired id 
  3. then you will see a variety of sensitive files and contracts which contain PIIs and other classified documents

## Impact

An unauthenticated attacker is able to obtain PII of users and soldiers also an attacker is able to leak classified documents

## Attachments
No attachments
