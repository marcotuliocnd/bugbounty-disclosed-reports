# Reports submitted by a non 2fa setupped user account can be transferred to a 2fa require submission program 

## Report Details
- **Report ID**: 2569993
- **URL**: https://hackerone.com/reports/2569993
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-06-22T04:36:13.990Z
- **Disclosed**: 2024-07-11T15:22:56.974Z

## Reporter
- **Username**: aloneh1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello team,

While testing the report submission function i found that when setting up the 2fa require to submit new reports to the program even the program staff can not  able to submit report to the program but using transfer report method the reporter who doesn't setuped the 2fa has submitted the report to other program and that report can be transferred to this 2fa require submission program .

Step to reproduce:-

1:- create two programs for testing like `h1R` and  `h1B`
2: Now got `h1B` program settings and select submission requirements settings and choose 2fa requirements to submit new reports.
3: from a no 2fa setuped hackerone account submit a report to `h1R`
4: Now as a program manager of the two program above mentioned in 1st step transfer the  report from step 3  to `h1B` it successfully transferred the report even the reporter who doesn't have setupped the 2fa. 

POC VIDEO:-

█████████

## Impact

No proper validation while transfferring the report to a 2fa require submission program weather the reporter have settuped the 2fa to his/her account.

Thanks,
aloneh1

## Attachments
No attachments
