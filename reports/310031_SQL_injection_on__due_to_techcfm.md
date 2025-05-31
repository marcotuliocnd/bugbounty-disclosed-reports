# SQL injection on █████ due to tech.cfm 

## Report Details
- **Report ID**: 310031
- **URL**: https://hackerone.com/reports/310031
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-01-28T20:20:51.983Z
- **Disclosed**: 2019-10-08T18:57:25.963Z

## Reporter
- **Username**: alyssa_herrera
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
The website appears to be vulnerable to SQL injection due to inducing an sql error using a single '
**Description:**
The following url, https://█████/hro/html/tech.cfm?Sort=Grade&ThisType=2 contains the parameter sort= which is vulnerable to SQLI. We know this due to the error disclosing the SQL query being used. 
```SELECT *, tbl_JobInfo.id as TJobID,tbl_JobDocs.id as DocID FROM dbo.tbl_JobInfo left outer join dbo.tbl_JobType on JobTypeID = tbl_JobType.id left outer join tbl_JobDocs on tbl_JobInfo.id = tbl_JobDocs.JobID WHERE JobTypeID = 3 AND JobTypeID > 1 AND Display = 'Y' Order by 'INJECTION' ASC1```  We can then demonstrate vulnerability by using time based queries and I opted to instead keep my queries low impact as to not violate the rules.
## Impact
High
## Step-by-step Reproduction Instructions

https://███/hro/html/tech.cfm?Sort=SLEEP(25)&ThisType=3
This will cause the page hang to hang momentarily 
This won't cause the website to hang, https://█████████/hro/html/tech.cfm?Sort=SLEEP()&ThisType=3
Additionally included timing screen shots showing the time  between the pages
## Product, Version, and Configuration (If applicable)
N/a
## Suggested Mitigation/Remediation Actions
Sanitize user input and prepare statements

## Impact

An attacker could access the Database and harvest potentially sensitive data from the website or even take over the entire website through using certain SQL commands.

## Attachments
No attachments
