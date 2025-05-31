# Manipulate hacker profile and private program hacktivity to expose your name as researchers who is actively submitting reports with resolve status

## Report Details
- **Report ID**: 654198
- **URL**: https://hackerone.com/reports/654198
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-23T02:36:53.233Z
- **Disclosed**: 2019-09-29T08:39:58.916Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi Team,

**Summary:**

First of all, the issue that i have found have multiple steps, so please make sure to follow the steps accordingly.

I was able to put my hacker name on private program hacktivity profile showing that i have report that was resolved, this will also reflect to my hacker profile.

## Requirements:

- The program should have a security forwarding feature
- The hacker/researcher will use the hackerone publishing feature

For PoC purposes, I have tested it in [███████](https://hackerone.com/███████) private program because they have `security@` email forwarding: `hackerone@█████████.com`.

### Steps To Reproduce

1. Assume that you are not invited to [███████](https://hackerone.com/██████████) private program private program, first step, use the publish feature, go here: https://hackerone.com/hacktivity/publish
2. Submit a publish report, put ████████ (███████) in Program (see below), put any test details and hit `Publish Vulnerability`.
████
3. Now the vulnerability is under `Pending review` by a moderator
4. Send a test mail to `hackerone@████.com` to get an invitation to submit a report, accept the invitation and you will become a participant of the said private program.
5. After that you will observed after how many hours, it will show on the private program hacktivity page your publish report will show as `resolved` ███████ and displayed on their hacktivity timeline, this will also show on your hacker profile time line ███. 

## Additional PoC below:

████

The report number of that publish report is https://hackerone.com/reports/652941 , __please note that this test publish report is still under pending review by the moderator.

## Impact

Hacker can manipulate the private program hacktivity page to show his/her hackerone name to look like there is so many report that was submitted and resolved.

This will also manipulate the hacker profile to show that he/she have many report that was submitted and resolved to a particular private program.

Audience for that hacker will be tricked.

Let me know if you need additional information.

Regards
Japz

## Attachments
No attachments
