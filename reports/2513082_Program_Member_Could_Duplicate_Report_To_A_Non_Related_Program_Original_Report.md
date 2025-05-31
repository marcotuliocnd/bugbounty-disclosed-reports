# Program Member Could Duplicate Report To A Non Related Program Original Report 

## Report Details
- **Report ID**: 2513082
- **URL**: https://hackerone.com/reports/2513082
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-05-20T16:30:35.847Z
- **Disclosed**: 2024-06-19T12:22:44.517Z

## Reporter
- **Username**: v0id1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Hello Hackerone team, I found a vulnerability on setting duplicate report as program owner. I'm able to duplicate a report to a report that doesn't have relation with the program. For example we can duplicate to a public report in hacktivity. 

### Steps To Reproduce
1. Create a sandbox program
2. On a report, select closed as duplicate and select another report from your program
3. Then intercept a request sent to /reports/bulk. Change the `original_report_id` parameter to 2279010 (A report to Portswigger #2279010)
{F3284733}  
{F3284729}

In addition after some analysis, I found that we also could mark as duplicate to a private report based on who's marking as duplicate. For example for me I would be able to duplicate to a report with id #2441985 which was a private report
{F3284759}

## Impact

- A Program could mark as duplicate a report that even doesn't have correlation to the original report and security researcher wouldn't be able to validate it
- Integrity issue since the duplicate report should be only come from the program related report

## Attachments
- image.png
- image.png
- image.png
