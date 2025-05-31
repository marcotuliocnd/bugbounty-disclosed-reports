# invalid homepage URL causes 'uncaught typeerror' or blank state

## Report Details
- **Report ID**: 177184
- **URL**: https://hackerone.com/reports/177184
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-20T23:04:19.190Z
- **Disclosed**: 2017-06-12T20:06:08.574Z

## Reporter
- **Username**: tsug0d
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

The issue is when you set the homepage as https://brave.com;https://google.com.vn and then change the setting to launch brave with homepage

## Products affected: 

Tested on  windows7 x64 + BraveSetup-ia32

## Steps To Reproduce:

1.go to Settings -> General, inject to "My home page is": https://brave.com;https://google.com.vn
2. close browser and reopen it
3. The browser become blank (forever?)

I try to unistall and reinstall brave but this issue still happen, so i have to go to my virtual machine to test it again. 

If the attacker can trick user to change their homepage using this payload, they can shutdown user's browser (forever?)

we can set homepage by javascript, and trick user to click this button, attacker can build those script too.

or simply told victim to set their homepage to "https://brave.com;https://google.com.vn" to see some fun.
## PoC:
https://cloud.githubusercontent.com/assets/17010094/19560362/d31ad10c-96f1-11e6-8895-161a6018e056.gif

## Attachments
No attachments
