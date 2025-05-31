# Information disclosure

## Report Details
- **Report ID**: 1347249
- **URL**: https://hackerone.com/reports/1347249
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-09-21T18:56:44.410Z
- **Disclosed**: 2021-09-21T23:35:38.889Z

## Reporter
- **Username**: kkarfalcon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
Vulnerability tested on:- Brave	1.29.81 Chromium: 93.0.4577.82 (Official Build) (64-bit)
Vulnerability description:- For security measures and for privacy purposes, Brave has the ability to open a normal tab of the Brave when we navigate to: `chrome://wallet`, `chrome://history` etc. due to the reason that Tor should be blocking privileged URIs like `file:///`, `chrome://` etc. When we open local storage URIs or the Data URIs, it is blocking. So, we can say that TOR in Brave protects users from opening anything privileged in the browser.
But there is some weird case for: `chrome://downloads` and `brave://inspect/#devices`. Both can be dangerous when there is a UXSS present there because it can get to know about the data. The `brave://device-log/` looks interesting too, why do we see the device log of brave in the TOR Network in the Brave? 

Steps to reproduce:
1. Open Brave with TOR
2. Navigate to `brave://inspect/#devices`

Expected behavior?
--> When we are doing device debugging, it should have opened normal Brave and shouldn't open the privileged URI in the TOR session itself. Open `chrome://bookmarks` and `chrome://history`

Actual behavior?
--> It opens the debugging session inside the protected tor session.

Suggestions?
--> We should block `chrome://downloads`,  `brave://inspect/#devices`, `brave://device-log/` etc. and when somebody tries to navigate to those URIs, a normal Brave session should be started like we do for `chrome://history` as it keeps TOR away from personal information inside the brave URIs.

## Impact

Information disclosure.

## Attachments
No attachments
