# SQL Injection - https://███/█████████/MSI.portal

## Report Details
- **Report ID**: 674838
- **URL**: https://hackerone.com/reports/674838
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-08-16T05:23:53.689Z
- **Disclosed**: 2020-05-14T17:03:25.984Z

## Reporter
- **Username**: arkaic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
https://███████/███████/MSI.portal has a form page which is vulnerable to SQL injection.

**Description:**
URL: https://████/██████/MSI.portal?_nfpb=true&_pageLabel=msi_portal_page_61#query

The above url has a form where the field MSI_queryType is vulnerable to time based blind SQL injection. I verified that sqlmap could identify the DBMS, and if the account had DBA rights. No other data was collected about the database.

See attached screenshot for sqlmap output.

## Impact

Critical - The database user which processes the form input has full DBA access, which allows the ability to read and write database information. There are also methods which would for executing commands as the database user, which could lead to compromise of the entire system housing the database.

## Step-by-step Reproduction Instructions

1. Visit this url, using an intercepting proxy - https://███/██████/MSI.portal?_nfpb=true&_pageLabel=msi_portal_page_61#query
2. Pick various form options for a search query and submit.
3. Capture POST via intercepting proxy
4. Use sqlmap to process captured POST request.
5. sqlmap is able to determine that form field MSI_queryType allows for time based blind SQL, along with details about the database type and user account.

## Product, Version, and Configuration (If applicable)
Oracle 11g

## Suggested Mitigation/Remediation Actions
Ensure that all parameters are sanitized before being processed as queries to the backend database, whether they are submitted via GET, POST, or any other means.

Perform rate limiting on the number of requests which can be submitted to the web site. Time based sql injection is slower than other methods, so would require a large amount of network traffic to retrieve data from the system.

## Impact

An attacker would have full control over reading and writing information in the database. The could allow several things, such as retrieving all database information, altering existing information, displaying malicious code on the web site, and potentially full control of the system running the database.

## Attachments
No attachments
