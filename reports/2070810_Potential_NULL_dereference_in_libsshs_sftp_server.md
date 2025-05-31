# Potential NULL dereference in libssh's sftp server

## Report Details
- **Report ID**: 2070810
- **URL**: https://hackerone.com/reports/2070810
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-07-16T02:48:19.125Z
- **Disclosed**: 2023-09-14T16:33:24.916Z

## Reporter
- **Username**: wct
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Missing allocation check in sftp server processing read requests may
cause NULL dereference on low-memory conditions. The malicious client
can request up to 4GB SFTP reads, causing allocation of up to 4GB buffers,
which is being unchecked for failure.

## Impact

This will likely crash the authenticated user sftp server's connection
(if implemented as forking as we recommend). For thread-based
servers, this might cause DoS also for legitimate users.

## Attachments
No attachments
