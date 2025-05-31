# http: Reading unprocessed HTTP request with unbounded chunk extension allows DoS attacks

## Report Details
- **Report ID**: 2375446
- **URL**: https://hackerone.com/reports/2375446
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-02-15T18:19:30.150Z
- **Disclosed**: 2024-03-05T12:09:56.321Z

## Reporter
- **Username**: bart
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I'd like to report Node.js vulnerability (CVE-2024-22019) that was recently fixed:
- HackerOne report: https://hackerone.com/reports/2233486
- Release notes: https://nodejs.org/en/blog/vulnerability/february-2024-security-releases

## Impact

This is a major issue because it allows unbounded resource (CPU, network bandwidth) consumption of the standard Node.js http server. The standard methods which could help blocking a malicious requests like timeouts and limiting request body size do not seem to work.

## Attachments
No attachments
