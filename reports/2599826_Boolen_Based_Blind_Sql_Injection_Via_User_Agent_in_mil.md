# Boolen Based Blind Sql Injection Via User Agent in ███.mil

## Report Details
- **Report ID**: 2599826
- **URL**: https://hackerone.com/reports/2599826
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-07-12T18:27:41.560Z
- **Disclosed**: 2025-01-24T14:47:28.868Z

## Reporter
- **Username**: iamunixtz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
### Bug Bounty Report: Boolean-Based Blind SQL Injection

#### **Summary**

I have discovered a boolean-based blind SQL injection vulnerability in the `User-Agent` header of the `https://███████.mil/` application. This vulnerability can be exploited to extract sensitive data from the backend database by leveraging boolean-based blind SQL injection techniques.
█████████

## Impact

- **Information Disclosure:** Attackers may infer database schema details and potentially sensitive information.
**Database and Web Server Details**

- **Database Management System:** MySQL 8 (MariaDB fork)
- **Web Server Operating System:** Windows
- **Web Application Technology:** Microsoft SharePoint 16.0.0.5452

## System Host(s)
████████.mil

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
#### **Steps to Reproduce**

1. **Set Up SQLMap:**
   Run the following `sqlmap` command to initiate a boolean-based blind SQL injection test:

   ```bash
   sqlmap --url https://█████████.mil/ --random-agent -risk 3 --level 5 --batch
   ```

2. **Identify Vulnerable Parameter:**
   The `User-Agent` header is used to inject payloads. In this case, I used the following payload to test the boolean-based blind injection:

   ```
   Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/523.10.3 (KHTML, like Gecko) Version/3.0.4 Safari/523.10' AND 8074=8074-- KwOG
   ```
3. **Confirm Vulnerability:**
   By injecting the payload, you can observe that the application responds differently based on the boolean condition provided (`8074=8074`).

4. **Test Using SQLMap or Burp Suite:**
   - **SQLMap:** You can use `sqlmap` to further exploit the vulnerability and extract data.
   - **Burp Suite:** Manually craft and test boolean-based blind SQL injection payloads to infer database information.

## Suggested Mitigation/Remediation Actions
1. **Sanitize User Inputs:** Ensure that all user inputs, including headers like `User-Agent`, are properly sanitized and validated to prevent SQL injection attacks.
2. **Use Prepared Statements:** Implement parameterized queries using prepared statements to safeguard against SQL injection vulnerabilities.
3. **Regular Security Audits:** Conduct regular security assessments and penetration testing to identify and mitigate potential vulnerabilities.
4. **Update and Patch Systems:** Regularly update and patch all components of the web application and database management system to protect against known vulnerabilities



## Attachments
No attachments
