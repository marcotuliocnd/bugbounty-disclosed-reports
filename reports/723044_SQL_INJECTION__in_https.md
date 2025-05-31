# SQL INJECTION  in https://████/██████████ 

## Report Details
- **Report ID**: 723044
- **URL**: https://hackerone.com/reports/723044
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-25T22:00:26.116Z
- **Disclosed**: 2022-04-29T13:56:20.270Z

## Reporter
- **Username**: mido0x0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Bug is : Sql injection in https://██████████/████████  via Referer
I've confirmed the vulnerability using sleep SQL queries with various arithmetic operations. The sleep command combined with the arithmetic operations will cause the server to sleep for various amounts of time depending on the result of the arithmetic operation.

##Proof of concept :
1- go to https://██████████/████████  and capture Request 
2- put this payload in Referer '+(select*from(select(sleep(6*6)))a

## Impact

##Impact :
An attacker can manipulate the SQL statements that are sent to the MySQL database and inject malicious SQL statements. The attacker is able to change the logic of SQL statements executed against the database.

## Attachments
No attachments
