# Critical sensitive information Disclosure. [HtUS]

## Report Details
- **Report ID**: 1626236
- **URL**: https://hackerone.com/reports/1626236
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-07-05T14:04:33.153Z
- **Disclosed**: 2023-01-13T18:05:48.810Z

## Reporter
- **Username**: berserkbd47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
(Database user,Database password,Database name) 
on https://██████.edu/

I got sensitive information:
view-source:https://██████████.edu/database.php.orig


Database information (Database user,Database password,Database name)
$hostname     = '████████.edu';
$db         = '█████████';
$username     = '████_user';
$password     = '████';

## Impact

Bug impact:
Sensitive information disclosed and possible for an attacker can access into the system.

## Attachments
No attachments
