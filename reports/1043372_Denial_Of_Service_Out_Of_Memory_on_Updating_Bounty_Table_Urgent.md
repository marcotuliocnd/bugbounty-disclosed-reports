# Denial Of Service (Out Of Memory) on Updating Bounty Table [Urgent]

## Report Details
- **Report ID**: 1043372
- **URL**: https://hackerone.com/reports/1043372
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-11-25T11:25:38.715Z
- **Disclosed**: 2021-02-02T20:06:13.293Z

## Reporter
- **Username**: ahmd_halabi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello,

**Summary:**
There is a bug in Updating Bounty Table section causing Denial Of Service , specifically loading up the memory usage (Out Of Memory). This happens when you visit a corrupted bounty table of a target program.

I didn't figure out yet how this issue happened but I am reporting it now immediately because it affects all hackers who view the bounty table of  the target affected program.

**Description:**
The issue happened with me when I was clicking on a notification telling that `Clario has updated their bounty table`.
So I clicked on it to see the updated bounty table and suddenly my browser tab crashed and a message showed telling `Error code: Out Of Memory`.
I tried it from two hackerone accounts and they results with the same issue.

### Steps To Reproduce

1. Navigate to the notification: https://hackerone.com/clario/bounty_table_versions?nid=115515717&utm_campaign=user_652675&utm_content=team_url&utm_medium=email&utm_source=bounty_table_update
2. You will not be able to click on any button (Ex: profile or Inbox).
3.  After short while, Browser will crash.

### Optional: Your Environment (Browser version, Device, etc)
Google Chrome.

### Optional: Supporting Material/References (Screenshots)
Please see the attached image and quick video PoC

██████████

{F1093466}

### Optional: Did you use [recon data made available by HackerOne](https://github.com/Hacker0x01/helpful-recon-data) to find this vulnerability?

no

## Impact

Denial Of Service (Out Of Memory) - Crashing whole Browser (happened with me) and loading up computer resources (CPU and RAM).

Kind Regards.

## Attachments
- 2.PNG
