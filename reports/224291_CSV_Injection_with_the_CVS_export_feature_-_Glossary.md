# CSV Injection with the CVS export feature - Glossary

## Report Details
- **Report ID**: 224291
- **URL**: https://hackerone.com/reports/224291
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-27T11:17:22.094Z
- **Disclosed**: 2017-05-17T14:19:37.838Z

## Reporter
- **Username**: amsda
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi,

The "Download as a CSV" feature of Weblate does not properly "escape" fields. Here is more information about this issue: http://www.contextis.com/resources/blog/comma-separated-vulnerabilities/

Here is one method to reproduce this issue:

1) I can add new information in Glossary with a name starting with "=1+1;" or "-2+3+cmd|' /C calc'!G2;"
2) I choose to export all Glossary to CSV containing the issue in (1)
3) I now open this CSV file in excel or another spreadsheet program
4) You can see the cell containing the issue name in (1) is displayed as "2" (=1+1;) which means the code is executed.



## Attachments
- Record_2017_04_27_08_14_47_181.mp4
