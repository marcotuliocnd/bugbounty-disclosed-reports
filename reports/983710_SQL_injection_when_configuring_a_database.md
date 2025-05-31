# SQL injection when configuring a database 

## Report Details
- **Report ID**: 983710
- **URL**: https://hackerone.com/reports/983710
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-09-16T18:31:34.972Z
- **Disclosed**: 2021-01-14T21:33:09.846Z

## Reporter
- **Username**: solov9ev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: impresscms

## Vulnerability Information
## Summary:
I found a SQL Injection in the form of a system install (Database configuration)

## Steps To Reproduce:
- Run command: `git clone https://github.com/ImpressCMS/impresscms.git`
- Stop at a menu item: `Database configuration`
- In the `Database name` field, insert the following exploit:


```sql
 impresscms`;create database `vuln
```

{F990522}

-  Submit the form

{F990524}

- Two databases (`impresscms`, `vuln`) created successfully. POC is attached to the report

## Supporting Material/References:
[PHP addslashes](https://www.php.net/manual/en/function.addslashes.php) - single quote ('), double quote ("), backslash, NUL (the NUL byte), but **Backtick is not escaped!**

## Impact

Executing arbitrary code on a database

## Attachments
- _________________2020-09-16_21-12-49.png
- _________________2020-09-16_21-12-49_(_____).png
- Peek_2020-09-16_21-17.mp4
