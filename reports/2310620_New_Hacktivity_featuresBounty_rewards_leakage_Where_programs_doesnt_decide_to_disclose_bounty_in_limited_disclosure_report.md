# New Hacktivity features:Bounty rewards leakage Where programs doesn’t decide to disclose bounty in limited disclosure report

## Report Details
- **Report ID**: 2310620
- **URL**: https://hackerone.com/reports/2310620
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-01-10T07:10:41.233Z
- **Disclosed**: 2024-03-28T11:27:32.680Z

## Reporter
- **Username**: nitsec7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
hello,

few months ago i submit  #2030964 and sadly its closed as duplicate of this #1961639 , but i found to access same issue i.e:  users hidden bounty information  leak as new feature method that is bounty amount filter on hacktivity.

█████████

steps to reproduce
-
go to hacktivity page 
add filter - ` total_awarded_amount:10000` or `total_awarded_amount:8000`
you can see bounty awarded amount on report which is not visible as normal 

i add some report please check
-
https://hackerone.com/reports/977212
https://hackerone.com/reports/881901
https://hackerone.com/reports/513236

now the feature to hide bounty amount is not worth here. please fix this so a non- authorized users, or no-one can see if hackers want hide bounty amount

## Impact

due to new features hacktivity filter  Anyone can seen total bounty award even hackers want to be hide from public

## Attachments
No attachments
