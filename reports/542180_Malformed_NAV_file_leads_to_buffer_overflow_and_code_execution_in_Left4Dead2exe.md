# Malformed NAV file leads to buffer overflow and code execution in Left4Dead2.exe

## Report Details
- **Report ID**: 542180
- **URL**: https://hackerone.com/reports/542180
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-04-18T17:36:32.186Z
- **Disclosed**: 2020-03-25T22:00:16.031Z

## Reporter
- **Username**: hunterstanton
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
## Summary
In the parsing routines of NAV files (which contain the navigation mesh used by the AI for survivor bots, zombies, and the AI director spawning system) a buffer overflow exists which can be used to control the EIP register and takeover code execution. 

## Proof-of-Concept
1. Download the attached c1m1_hotel.nav
2. Place it in your *<steamapps>/Left 4 Dead 2/left4dead2/maps/* directory
3. Start up Left4Dead 2 and attach a debugger
4. Enter "map c1m1_hotel" into the developer console
5. Observe that EIP becomes 0x41414102, indicating that a buffer overflow has occurred and code execution is possible

## Operating Systems Tested
- Windows 10 1809 Build 17763.437

I have not tried this for MacOS or Linux, however I assume it would work on both of those platforms as well if they all share the same codebase as the Windows executable.

## Notes
Because Left4Dead 2 ships on Windows with a non-ASLR enabled module (binkw32.dll), it is much easier to write up a working exploit for this vulnerability as you no longer need an additional infoleak of some kind to do serious damage and can just use ROP.

## Impact

## Impact
If an attacker successfully exploits this vulnerability, the attacker can run arbitrary code on the machine of a victim.

Due to the fact that Source supports sending arbitrary files to clients when connecting to a server, it is possible that you could create a fake dedicated server that does nothing but send the malformed NAV file to clients who are connecting, creating a remote code execution scenario.

Another attack scenario would be an attacker uploading a campaign map with a malformed NAV to the Steam Workshop, and convincing other users to download it. When they download it and load the campaign in game, arbitrary code will be executed on their machines.

## Attachments
- c1m1_hotel.nav
