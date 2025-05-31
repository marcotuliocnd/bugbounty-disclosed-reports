# Access to tomcat-manager with default creds

## Report Details
- **Report ID**: 1267174
- **URL**: https://hackerone.com/reports/1267174
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-07-17T23:24:05.276Z
- **Disclosed**: 2023-02-05T12:59:44.752Z

## Reporter
- **Username**: 0xjackal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: jetblue

## Vulnerability Information
## Summary:
Hi jetblue Security Team.

I Found that this domain `█████████` using Apache Tomcat/6.0.35 , And i was able to login to https://██████████/manager/html With default credentials `tomcat:tomcat`
See the following Screenshots:-

██████████

███

## Steps To Reproduce:
1. Go To https://███████/manager/html
2. Login with default creds `tomcat:tomcat`

## Supporting Material/References:
- https://book.hacktricks.xyz/pentesting/pentesting-web/tomcat

## Impact

Improper Authentication
Default Credentials lead to access admin manager.

##Fix:-
- Change default creds.

## Attachments
No attachments
