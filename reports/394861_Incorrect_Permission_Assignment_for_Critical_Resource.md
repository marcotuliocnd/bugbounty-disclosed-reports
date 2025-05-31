# Incorrect Permission Assignment for Critical Resource

## Report Details
- **Report ID**: 394861
- **URL**: https://hackerone.com/reports/394861
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-08-14T10:20:51.773Z
- **Disclosed**: 2018-11-14T09:03:30.215Z

## Reporter
- **Username**: dhiraj-mishra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mariadb

## Vulnerability Information
Dear Team, 

Product Affected: https://github.com/MariaDB/server

File:
 /server/blob/10.3/sql/mysqld.cc#L2761

```
}
    if (!SetSecurityDescriptorDacl(&sdPipeDescriptor, TRUE, NULL, FALSE))
{
```

This was purely identified on code review, Never create NULL ACLs.

A mail was sent to security@mariadb.org and MariaDB team is working on this and a fix will be pushed in next version, attached mail headers for your reference.

## Impact

An attacker can set it to Everyone (Deny All  Access), which would even forbid administrator access and may lead to privilege escalation.

## Attachments
- MailFrom-security_mariadb.org.txt
- MariaDB.png
- MariaDB-2.png
