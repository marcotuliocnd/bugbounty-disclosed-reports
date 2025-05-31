# SQL Injection in ████

## Report Details
- **Report ID**: 519631
- **URL**: https://hackerone.com/reports/519631
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-04-01T18:15:35.494Z
- **Disclosed**: 2019-08-19T12:21:33.198Z

## Reporter
- **Username**: arinerron2
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
## Summary

There is an SQL injection vulnerability in `████████` in the /█████/recruiter/updapp.aspx` page, exploitable through the `app_id` form parameter.

## Impact

An attacker could use this vulnerability to control the content in the database, exfiltrate information, and obtain remote code execution.

## Step-by-step Reproduction Instructions

1. Visit https://█████████/Gateway/sso.aspx and sign in. Note that any user can create a user (and any privilege level works for this vulnerability as long as a user is signed in), so this should be considered an unauthenticated vulnerability.
2. With the Network tab of devtools open, visit https://██████/████/recruiter/updapp.aspx
3. Replay the GET request that returned the HTTP 500 error as a POST request with the body `app_id='`. This can be done by right clicking on the request, copying it as cURL, pasting the command in terminal, and appending ` -k -X POST --data "app_id='"`.
4. Notice in the response, there is an error: `ORA-01756: quoted string not properly terminated`. This is because the single apostrophe (`'`) caused the SQL query to be syntactically invalid.
5. Replay the request in the same way as shown in #3, but with the body `app_id=''` (this time append ` -k -X POST --data "app_id=''"` to the cURL command). 
6. Notice in the response, there is an error: `ORA-01722: invalid number`. This is because the double apostrophes (`''`)  did not cause the SQL query to be syntactically invalid, but because aposrophes are not numbers, they caused a different error.
7. Repeat step #3 as many times as you like. An odd number of apostrophes (`'`) will cause the SQL query to fail because it is syntactically invalid, and an even number will cause it to fail because it is valid, but apostrophes are not numbers.

I did not want to exploit this to get remote code execution because this is a live production system, but to get RCE, simply execute an SQL query that writes the file at https://raw.githubusercontent.com/danielmiessler/SecLists/master/Web-Shells/laudanum-0.8/aspx/shell.aspx to `D:\██████\shell.aspx` using the `INTO OUTFILE` syntax, then visit https://███/█████████/shell.aspx

## Suggested Mitigation/Remediation Actions

Sanitize everything in the SQL query (use prepared statements), and validate the data before putting it in the query.

Note: I wouldn't have been able to find this vulnerability if it wasn't for the fact that verbose error pages were enabled. Because they were, it leaked source code, and I could see that the SQL injection vulnerability existed before testing.

## Impact

An attacker could use this vulnerability to control the content in the database, exfiltrate information, and obtain remote code execution.

## Attachments
No attachments
