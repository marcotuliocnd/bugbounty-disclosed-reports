# DoD workstation exposed to internet via TinyPilot KVM with no authentication

## Report Details
- **Report ID**: 2633988
- **URL**: https://hackerone.com/reports/2633988
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-08-01T00:00:18.667Z
- **Disclosed**: 2024-08-16T16:07:16.879Z

## Reporter
- **Username**: socpuppet
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
There appears to be a workstation belonging to ███████ (███) that is completely exposed to the internet via IP web interface by way of a TinyPilot KVM device.

TinyPilot KVMs are hardware devices that enable you to remotely access computers via IP address. This device in question is available over the internet without authentication and is connected to a workstation that appears to belong to ███. There is an "UNCLASSIFIED" green banner at the top. In the top right corner appears to be the initials "SA", which may identify the user.

Please see attached screenshot. Of note: I did **not** interact with the device at all. I immediately closed the connection after taking the screenshot attached to file this report. I do not know how long this device has been exposed like this. There appears to be no notification the user when this happens.

## References
Read more about TinyPilot devices here: https://tinypilotkvm.com/

## Impact
Simply by visiting the IP address in question, anyone on the internet can see the users screen and have full mouse/keyboard control over the workstation. An attacker could also sit and watch the user's screen to gain information.

Confidentiality: The user's entire session is exposed. Anything that appears on screen could be seen/watched by an attacker.
Integrity: An attacker could take control of the mouse/keyboard and modify the system in any way.
Availability: An attacker could take control of the mouse/keyboard and destroy files, inhibit the use of the system, etc.

## System Host(s)
████████ (Comcast Cable Communications, LLC - Houston, TX)

## Steps to Reproduce
Visiting https://█████ loads into the TinyPilot KVM service with no authentication and connects you to what appears to be a ███████ workstation.

## Suggested Mitigation/Remediation Actions
Disconnect the workstation from TinyPilot KVM, or insure proper authentication mechanism is in place.



## Attachments
No attachments
