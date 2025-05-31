# Sensitive Data Exposure via wp-config.php file

## Report Details
- **Report ID**: 1912671
- **URL**: https://hackerone.com/reports/1912671
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2023-03-20T00:36:50.155Z
- **Disclosed**: 2023-05-15T15:04:32.303Z

## Reporter
- **Username**: 0r10nh4ck
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**

Hi team,
A copy of the WordPress config file wp-config.php has been found at  █████████ endpoint. It contains sensitive information, such as MySQL and AWS credentials, and various keys.

## References

https://codex.wordpress.org/WordPress_Files

## Impact

The page provides information to users who do not need it.

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Go to: ███/wp-config.php_
2. See the information.

## Suggested Mitigation/Remediation Actions
Implement access control.



## Attachments
No attachments
