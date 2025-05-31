# Exposed FTP Credentials on ███████

## Report Details
- **Report ID**: 235216
- **URL**: https://hackerone.com/reports/235216
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-01T02:53:56.499Z
- **Disclosed**: 2019-12-02T18:59:13.550Z

## Reporter
- **Username**: z3t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
An exposed configuration file leaks FTP credentials to a DoD server.
**Description:**
The config file hosted on`ftp://█████████/pub/misc/FTP_███████Sign.exe.config` exposes a username `█████████` and associated password `███████`. These are valid credentials for the FTP server operating on `██████████:21`. This was verified by establishing a connection to the server with the credentials - no file data was transferred.
## Impact
Read access to any file on the `████` FTP server.

## Step-by-step Reproduction Instructions

1. Navigate to `ftp://████/pub/misc/FTP_██████Sign.exe.config` (establishes an anonymous FTP session on modern browsers)
2. Verify credentials are in the `userSettings` XML section
3. Establish an FTP connection to `████████` using the credentials

## Suggested Mitigation/Remediation Actions
Anonymous FTP access should be disabled on `██████████` and the credentials exposed in the configuration file should be changed.

## Attachments
No attachments
