# HTML Injection on airlink.ubnt.com

## Report Details
- **Report ID**: 226783
- **URL**: https://hackerone.com/reports/226783
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-07T20:19:20.150Z
- **Disclosed**: 2017-06-22T14:13:24.451Z

## Reporter
- **Username**: ruisilva
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
Hi
I found an html injection vulnerability on airlink.ubnt.com

Steps to reproduce:

First go to: https://airlink.ubnt.com/#/ptp
Next go on Save Simulation button and as simulation name put: "><marquee><h1>HTMLINJECTIONHERE</h1></marquee> and save it
Now go on Open Simulation button and you will see html being executed :) 

Your team should fix it
Thanks 

## Attachments
- POC.png
