# SQL injection in  https://www.acronis.cz/ via the log parameter

## Report Details
- **Report ID**: 1109311
- **URL**: https://hackerone.com/reports/1109311
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-23T07:48:46.720Z
- **Disclosed**: 2021-06-11T12:58:04.810Z

## Reporter
- **Username**: mmg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
I have discovered a SQL injection in https://www.acronis.cz/ using the POST request via the log parameter.
Using sqlmap, I have retrieved the current user: 'u_acronis@localhost''

The command used:
sqlmap  -p log -r request-cz.txt --current-user  --level=2 --risk=2

I did not perform any other actions.

## Impact

An attacker can use SQL injection it to bypass a web application's authentication and authorization mechanisms and retrieve the contents of an entire database.
This can also be used by an attacker to execute OS commands, which may then be used to escalate an attack even further.

## Attachments
- request-cz.txt
