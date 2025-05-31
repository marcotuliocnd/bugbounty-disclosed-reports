# Blind SQL Injection

## Report Details
- **Report ID**: 771215
- **URL**: https://hackerone.com/reports/771215
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-09T18:55:08.616Z
- **Disclosed**: 2022-04-29T13:57:24.014Z

## Reporter
- **Username**: mido0x0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
###Bug is : Blind Sql injection 

SQL injection is a vulnerability that allows an attacker to alter back-end SQL statements by manipulating the user input. An SQL injection occurs when web applications accept user input that is directly placed into a SQL statement and doesn't properly filter out dangerous characters. 

-----------------------------------------------

###Vulnerability in :
 https://███/ via ``` User-Agent: ```
I've confirmed the vulnerability using sleep SQL queries with various arithmetic operations. The sleep command combined with the arithmetic operations will cause the server to sleep for various amounts of time depending on the result of the arithmetic operation.

--------------------------

###Proof of concept : 
1- open https://███/  and intercept data 
2- put this payload in user agent parameter ``` if(now()=sysdate(),sleep(10),0)/*'XOR(if(now()=sysdate(),sleep(10),0))OR'"XOR(if(now()=sysdate(),sleep(10),0))OR"*/  ```  like poc 1
and as you see in poc 1 make sleep order for 10 sec 
3- and if we change order to make sleep for 5 sec  ``` if(now()=sysdate(),sleep(5),0)/*'XOR(if(now()=sysdate(),sleep(5),0))OR'"XOR(if(now()=sysdate(),sleep(5),0))OR"*/ ``` like poc 2


-----------------------------

###Fix :
Your script should filter metacharacters from user input. 
Check detailed information for more information about fixing this vulnerability

## Impact

An attacker can manipulate the SQL statements that are sent to the MySQL database and inject malicious SQL statements. The attacker is able to change the logic of SQL statements executed against the database.

## Attachments
No attachments
