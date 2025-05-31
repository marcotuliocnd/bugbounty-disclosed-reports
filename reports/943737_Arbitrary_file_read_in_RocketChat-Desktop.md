# Arbitrary file read in Rocket.Chat-Desktop

## Report Details
- **Report ID**: 943737
- **URL**: https://hackerone.com/reports/943737
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-27T12:12:21.429Z
- **Disclosed**: 2022-02-06T19:36:37.488Z

## Reporter
- **Username**: sectex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Description:** Rocket.Chat-Desktop is vulnerable to arbitrary file read.

## Releases Affected:

  * Rocket.Chat-Desktop-Client: < v3.0.0-develop

## Steps To Reproduce (by setting up a malicious server):

1. Go to `Administration » Layout » Custom Scripts » Custom Script for Logged In Users`
1. Insert the following script `window.open('file://c:/windows/system32/drivers/etc/hosts').eval('alert(document.body.innerText);');`
1. Click `Save changes`
1. Open Rocket.Chat-Desktop and connect to the server
1. A new window and an alert containing the contents of `c:/windows/system32/drivers/etc/hosts` will pop up.

## Suggested mitigation

  * Set `popups` to `false` [[`src » component » electron » WebViewComponent.js (line 16)`](https://github.com/RocketChat/Rocket.Chat.Electron/blob/develop/src/components/electron/WebViewComponent.js)].

## Impact

Arbitrary file read in Rocket.Chat-Desktop

## Attachments
No attachments
