# Insecure Cache-Control Leading to API key Retrieval

## Report Details
- **Report ID**: 231805
- **URL**: https://hackerone.com/reports/231805
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-25T13:57:42.919Z
- **Disclosed**: 2017-07-18T19:12:51.022Z

## Reporter
- **Username**: pabster
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: thisdata

## Vulnerability Information
Description:
https://thisdata.com/customers/[user]/install/apis/[number]/reauthorize Does not have good browser cache management, allowing another user with access to the device to retrieve the API key. All of the thisdata.com pages do not have the cache management correctly configured, allowing the attacker to gain access to all of the information of the victim, but with the API key it is enough to take full control of the victim's app.

Steps To Reproduce:
1) Go to the API Settings.
2) Logout
3) Click on the back button.
The page will show the API key.

Danger:
In a PC scenario in an office or in a library or in a coffee shop or such places allow for an attacker to exploit this vulnerability (since the amount of pages visited after visiting the API settings doesn't matter). Also it is very easy to get access to a laptop, so this is a likable scenario, and once it happens the attacker has full control over the victim's app data since he/she can use the API key to add users ...

Solution:
Add the header:("Cache-Control: no-store, no-cache, must-revalidate");
You currently don't have the no-store or the no-cache, which is enough to be able to exploit this vulnerability.

Tested in Chrome latest version.

Hope it helps.
Sincerely,
Pablo

## Attachments
No attachments
