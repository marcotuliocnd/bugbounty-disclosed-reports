# SQLi | in URL paths

## Report Details
- **Report ID**: 2958619
- **URL**: https://hackerone.com/reports/2958619
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2025-01-26T07:59:46.766Z
- **Disclosed**: 2025-03-06T11:54:55.130Z

## Reporter
- **Username**: almuntadhar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
A SQL Injection vulnerability was discovered in the customerId parameter of the URL path:
`███████`
We can observe this by adding a little quote in the customerId:
█████████
which will show the following error, indicating that its vulnerable to SQL Commands Injection:
███████

## Steps To Reproduce:
We can use any SQL Commend here, by just closing the Statement ( putting `')` and then use a command and also we make sure to make the rest as a comment, here is a basic SQL command i used:
███████
or we can use tools like SQLmap to get access to the database, here is the command i used:
```
sqlmap -u "██████
```
██████

## Impact

## Summary:

An attacker can exploit this to dump and download the database, Which will give them access to user informations.

## Attachments
No attachments
