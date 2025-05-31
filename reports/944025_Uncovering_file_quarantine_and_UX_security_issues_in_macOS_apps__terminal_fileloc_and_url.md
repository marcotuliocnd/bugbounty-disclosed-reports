# Uncovering file quarantine and UX security issues in macOS apps ( .terminal, .fileloc and .url) 

## Report Details
- **Report ID**: 944025
- **URL**: https://hackerone.com/reports/944025
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-07-27T14:43:49.811Z
- **Disclosed**: 2021-07-23T12:07:08.190Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Slides : https://docs.google.com/presentation/d/19WeQbqc_OKnrSv1I3Z4sm-oNAf6IVzHwRyQP4i9Bv_Y/edit#slide=id.g758ad3e042_23_231
See Blogpost for more details - https://medium.com/@metnew/exploiting-popular-macos-apps-with-a-single-terminal-file-f6c2efdfedaa

# Summary
Popular macOS apps with a file-sharing functionality didn't delegate file quarantine to OS leading to File Quarantine bypass (Windows MOTW analogue) for downloaded files. The vulnerability has low/moderate impact, but it can be combined with other custom behaviours, and UX features to increase the severity.

During the research, I also discovered two "insecure features" in macOS: dangerous handling of .fileloc and .url shortcut files, those allow executing arbitrary local files by the full path at shortcut file opening. This behaviour allowed me to discover two Chrome and Firefox bugs: CVE-2020–6797, CVE-2020–6402

# Affected Apps
More than 20 apps, some of these products are on H1, some not and they deny disclosing the report.
- Keybase - https://hackerone.com/reports/430463
- Telegram - valid, fixed, bounty
- Slack  - https://hackerone.com/reports/470637
- Skype - decided not to track as a vulnerability, fixed
- WhatsApp - valid, fixed, bounty
- Wickr - valid, bounty
- Signal - fixed, https://github.com/signalapp/Signal-Desktop/issues/3590
- Brave - https://hackerone.com/reports/374106
- OneDrive - decided not to track as a vulnerability - the case is shady, because Apple granted MS a privileged entitlement 
- Dropbox - decided not to track as a vulnerability - https://hackerone.com/reports/430733
- Google Drive - triaged, but later decided not to track as a vulnerability
- ICQ - https://hackerone.com/reports/484664
- https://hackerone.com/bugs?report_id=737576
- https://hackerone.com/bugs?report_id=691890
- https://hackerone.com/bugs?report_id=702608
- https://hackerone.com/reports/719175 (macos vector)
- https://hackerone.com/reports/725356
- https://www.zoho.com/mail/desktop/ - HoF
- viber desktop - valid, fixed, no bounty (25$ for Viber stickers)
- mega - backlog + decided to fix later based on decisions of other apps developers.
-  etc. (not sure whether reports inspired my research also counts)

`.fileloc`:
- Firefox - CVE-2020-6797
- Chrome - CVE-2020-6402

`.url` file handling was fixed in macOS Catalina beta.

## Impact

Please, refer to the blogpost and slides.

## Attachments
No attachments
