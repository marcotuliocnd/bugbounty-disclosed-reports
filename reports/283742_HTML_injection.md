# HTML injection 

## Report Details
- **Report ID**: 283742
- **URL**: https://hackerone.com/reports/283742
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-10-28T11:49:46.965Z
- **Disclosed**: 2017-10-31T10:30:42.556Z

## Reporter
- **Username**: nihadrekanym
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
hi team ...

i found HTML i on https://infogram.com/app/#/library
step

..
1- go to https://infogram.com/app/#/library
2- choose Report Templates .
3- Use Report Classic
4- click to edit_data
5- edit cell __Employee ID__
5- payload

  >  <h1>hacked</h1>
    <marquee behavior="scroll" direction="left">hacked</marquee>
   <h1 style="background-color:#000099;">hacked</h1>

6-execute HTML .. 

POC .. video on attached




## Attachments
- html_code.avi
