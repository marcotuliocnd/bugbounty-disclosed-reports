# User-assisted RCE in Slack for macOS (from official site) due to improper quarantine meta-attribute handling for downloaded files

## Report Details
- **Report ID**: 470637
- **URL**: https://hackerone.com/reports/470637
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-12-21T16:40:13.889Z
- **Disclosed**: 2019-09-14T22:28:54.831Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
## Summary

### **GateKeeper/Quarantine bypass for downloaded files**

Lack of `com.apple.quarantine` meta-attribute for downloaded files allows a remote attacker to send an executable file that won't be checked by Gatekeeper .

### File opening **doesn't trigger native alerts** from GateKeeper/Quarantine

> Downloaded executable files lack `com.apple.quarantine` meta-attribute => no alerts about launching an executable from the web will appear.

### Code execution after opening

Opening a downloaded `.terminal` file in Slack via "Shift + Click"  (or in Finder) immediately leads to running attacker's code on a target device.

### `.terminal` file

1. Opening leads to command execution.
2. Looks safe - XML file.
3. Downloaded `.terminal` file **couldn't be opened** if application sets quarantine meta-attribute properly. However, Slack (Direct Download) doesn't do that.

## Attack scenario

1. Attacker sends `exploit.terminal` to the victim. File looks like a plaintext file in preview.
2. Victim opens `exploit.terminal` file via "Shift + Click" (or via Finder)
3. No alert from Gatekeeper about unsigned executable
4. No alert about running executable file downloaded from the web
5. Shell commands from `exploit.terminal` get executed with user-level privileges.

## Version

Decribed scenario is reproducible in Slack 3.3.3 Direct Download.
Slack from AppStore has correct quarantine rules and isn't vulnerable.

## Additional details

`exploit.terminal` attached + Screencast attached.

### Quarantine
macOS is build in such way that OS will ask user before opening any downloaded and potentially launchable (in default setup) files. This rule applies to `.terminal` files too.

### TL;DR: 
- no quarantine -> `exploit.terminal` is launchable in 1 click without warning a user with popups
- quarantine -> no immediate launch for all files (2 popups) +  no RCE is possible if GateKeeper level set to "AppStore only"

## Impact

## Impact

Attacker could send a crafted `.terminal` file to the victim, which will be executed immediately after opening this file via "Open" button or in Finder. 

The attack scenario requires a certain level of user interaction. 
But the file looks safe and the victim doesn't expect that it'll be launched immediately

### Additional Impact

GateKeeper bypass allows running arbitrary apps in environments hardened with Gatekeeper settings set to "AppStore only".

## Attachments
- exploit.terminal
- ______________2018-12-21___6.36.02___.mov
