# Information Disclosure of Garbage Collection Cycle

## Report Details
- **Report ID**: 981796
- **URL**: https://hackerone.com/reports/981796
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-09-14T15:56:50.707Z
- **Disclosed**: 2020-11-04T19:09:20.464Z

## Reporter
- **Username**: ahmd_halabi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
Hello,

Upon enumerating a subdomain content I found a directory that discloses the duration of the garbage collection cycles.
I think that these information should be kept private because public should not know information about the target application and how it operates or do its garbage collection process.

##Steps To Reproduce
1. Navigate to the target url: https://gopher.hey.com/metrics
2. See the data.

███

## Impact

This information may help attackers understand more things about the target application which may help in further investigation and exploitation.

Kind Regards.

## Attachments
No attachments
