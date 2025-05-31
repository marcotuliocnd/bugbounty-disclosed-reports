# Program managers can see draft reports using Export Reports feature

## Report Details
- **Report ID**: 1664920
- **URL**: https://hackerone.com/reports/1664920
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-08-09T22:26:01.612Z
- **Disclosed**: 2023-05-18T11:42:08.022Z

## Reporter
- **Username**: alp
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

Hello. I have discovered a bug in the new draft feature. 

Program managers can see draft reports using Export Reports feature. 

### Steps To Reproduce

1. Make a draft (do not send) report on a public/private program.
2. Go to the `https://hackerone.com/<program-handle>/export_reports` page and export reports.
3. Check your e-mail and download the file got from HackerOne.
4. Check the CSV file:

{F1860656}

As you see, it says draft and disclosed report title, severity, weakness, etc.

When you try to find it in the program inbox you can't find it, so completely sure this is a bug.

{F1860658}

## Impact

Program managers can see draft reports using Export Reports feature leads to PII disclosure without reporter permission.

## Attachments
- report.PNG
- request.PNG
