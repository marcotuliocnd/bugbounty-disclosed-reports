# Time-based blind SQL injection

## Report Details
- **Report ID**: 2759243
- **URL**: https://hackerone.com/reports/2759243
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-10-04T01:23:41.980Z
- **Disclosed**: 2025-01-24T14:46:41.739Z

## Reporter
- **Username**: leofmlopes
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
A time-based blind SQL injection vulnerability was discovered at https://█████/app/SearchDocs.aspx?doctypes=19&filename=*&sdate=&edate=&content=&sortBy=1%20WAITFOR%20DELAY%20%270%3a0%3a5%27--%20udTV&sortOrder=&custom={%22customFields%22%3A[]}, when this request is sent, it is possible to manipulate the server's response time. This type of vulnerability can potentially be exploited to extract sensitive information from the database or even gain full control over the application's backend.
The vulnerable parameter is the `sortBy` parameter.

## References
OWASP SQL Injection
https://owasp.org/www-community/attacks/SQL_Injection

Similar report
https://hackerone.com/reports/2312334

## Impact

This vulnerability allows an attacker to:
- Confirm the existence of SQL injection by observing server response delays
- Potentially extract sensitive information from the database, such as usernames, passwords, or other critical data. 
The sensitive information could be extracted by sending payloads like "IF (SUBSTRING(DB_NAME(), 1, 1) = 'A') WAITFOR DELAY '00:00:05'; --". In this example, if the response is delayed, the attacker would know that the database name starts with 'A', then they would keep sending more payloads until they discover the full database name. They could also discover more information using the same method, like table names, column names and records stored in the database

## System Host(s)
██████████



## Steps to Reproduce
1. Open a browser
- The vulnerability can be tested directly in the browser by altering the URL parameters


2. Insert the following URL:
https://███/app/SearchDocs.aspx?doctypes=19&filename=*&sdate=&edate=&content=&sortBy=1%20WAITFOR%20DELAY%20%270%3a0%3a5%27--%20udTV&sortOrder=&custom={%22customFields%22%3A[]}

- This request is injecting a delay in the `sortBy` parameter. After sending the request, notice the server's response is delayed by 5 seconds


3. Insert the following URL:
https://███████/app/SearchDocs.aspx?doctypes=19&filename=*&sdate=&edate=&content=&sortBy=1%20WAITFOR%20DELAY%20%270%3a0%3a0%27--%20udTV&sortOrder=&custom={%22customFields%22%3A[]}

- This request has no delay, it returns immediately


4. These two requests have different response times, which confirms the presence of a time-based blind SQL injection vulnerability

In the following video, I recorded a demontration of the vulnerability using Burp Suite. First, a request with a 5-second delay is sent. Then another one with a 0-second delay is sent. The difference in response times can be clearly seen
██████

## Suggested Mitigation/Remediation Actions
- Implement input validation to prevent SQL queries from being executed. User-supplied data should be validated and sanitized to remove potentially harmful characters, such as single quotes ('), semicolons (;), and SQL keywords
- Use prepared statements and parameterized queries. User-supplied data should not be concatenated in SQL queries



## Attachments
No attachments
