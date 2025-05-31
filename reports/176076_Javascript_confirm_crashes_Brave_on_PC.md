# Javascript confirm() crashes Brave on PC

## Report Details
- **Report ID**: 176076
- **URL**: https://hackerone.com/reports/176076
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-10-16T01:31:53.695Z
- **Disclosed**: 2016-10-19T01:32:26.931Z

## Reporter
- **Username**: jackb898
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
Hello Brave, https://hackerone.com/smelt and I found a glitch for Brave on Windows.
## Summary:

If you run the javascript code confirm(), Brave will crash. This is major for a glitch, because people may be visiting
websites that have confirm messages and Brave will suddenly and unexpectedly crash for them.

## Products affected: 

Doesn't effect Mobile
Tested and crashed Windows Brave browser

## Steps To Reproduce:

1. Open Brave
2. Run the JS code confirm() somehow (Ex. go to my website I made that runs it: pentesting.x10host.com)
3. Brave will crash

If you have questions or comments please reply here.



Thanks,
kicker and smelt




## Attachments
No attachments
