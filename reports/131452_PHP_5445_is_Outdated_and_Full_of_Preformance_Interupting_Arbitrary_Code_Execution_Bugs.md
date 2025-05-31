# PHP 5.4.45 is Outdated and Full of Preformance Interupting Arbitrary Code Execution Bugs

## Report Details
- **Report ID**: 131452
- **URL**: https://hackerone.com/reports/131452
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-16T22:49:59.379Z
- **Disclosed**: 2017-08-21T13:29:40.785Z

## Reporter
- **Username**: sondash128
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Your PHP version is affected by quite a few remote arbitrary code execution, remote file renaming, and remote file rewriting bugs that require no authentication and can cause big problems, from performance interruptions and messing with server files to DoS attacks. These are not related to any particular non-default module, but php itself.

Here's a little list I compiled:
                CVE-2015-2301
                CVE-2014-9652
               CVE-2014-5459
               CVE-2014-4698
               CVE-2014-4670
               CVE-2014-3981

## Attachments
No attachments
