# Information disclosure of website

## Report Details
- **Report ID**: 179121
- **URL**: https://hackerone.com/reports/179121
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-10-31T15:43:28.602Z
- **Disclosed**: 2016-11-16T06:21:09.486Z

## Reporter
- **Username**: 1_1_1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please fill all sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty.

## Summary:
Malicious application can see what the user is browsing
[add summary of the vulnerability]

## Products affected: 
BRave browser for android
 * operating system, Brave version or Brave website page, etc.
Android Version Os : 4.4, App version:1.9.56
## Steps To Reproduce:
1)Open adb shell
2)ps | grep "app process id"
3)logcat *:D | grep "process id of app"

YOu will see all the url that the user is browsing 

 * List the steps needed to reproduce the vulnerability

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)
http://www.androidsecurity.guru/category/logging/


## Attachments
No attachments
