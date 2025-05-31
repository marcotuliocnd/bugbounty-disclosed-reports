# MSSQL injection via param Customwho in https://█████/News/Transcripts/Search/Sort/ and WAF bypass

## Report Details
- **Report ID**: 577612
- **URL**: https://hackerone.com/reports/577612
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-05-11T22:00:06.207Z
- **Disclosed**: 2019-10-10T19:13:15.046Z

## Reporter
- **Username**: bohdansec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**

MSSQL injection via param `Customwho` in https://███████/News/Transcripts/Search/Sort/

**Description:**

MSSQL injection via param `Customwho` in https://██████████/News/Transcripts/Search/Sort/

There is WAF, but we can make bypass and via global variable `@@LANGID` we can know that the base is used here - MSSQL

## Impact

Critical

## Step-by-step Reproduction Instructions

Via global variable `@@LANGID` we can find out that here is MSSQL database. ████

https://█████/News/Transcripts/Search/Sort/?Customwho=31002/**/|/**/@@LANGID

And if use a non-existing global variable, then we get an error. ██████

https://██████████/News/Transcripts/Search/Sort/?Customwho=31002/**/|/**/@@nonexisting

## Suggested Mitigation/Remediation Actions

Using prepared statement

## Impact

We can read and do other manipulations in the database. We can also try to make RCE

## Attachments
No attachments
