# Stored XSS in merge request creation page through payload in approval rule name

## Report Details
- **Report ID**: 1342009
- **URL**: https://hackerone.com/reports/1342009
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-09-16T20:13:04.198Z
- **Disclosed**: 2022-03-31T19:24:58.216Z

## Reporter
- **Username**: joaxcar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

Hi GitLab team, I found a stored XSS in merge request creation page caused by a payload in the name of an "approval rule".

Adding approval rules is a feature that is unlocked for premium subscriptions or above. This does not seem to block it from being used against regular users on for example Gitlab.com by inviting them into the "infected project".

This occurs when adding an "Approval rule" to a project and giving it a javascript/html payload as the name and attaching the rule to an approver. When a user tries to create a merge request in the project and opens the "Reviewers" dropdown, information about the user with the attached rule will be shown and the rule name will be injected underneath.

With the payload
```
<iframe/srcdoc='<script/src=/joaxcar_group/first/-/jobs/1415515489/artifacts/raw/data/alert.js></script>'></iframe>
```
this XSS bypasses the current CSP on Gitlab.com (tried it with an Ultimate trial and inviting a user without a trial to the project)

As I got the impression that all XSS are treated equal when reporting a similar issue, I have not made any deeper analysis of the reason for this firing. Thought I just report it right away. Please reach back to me if you need me to research the impact deeper! As an example, it does not fire when one "edits" a MR which is a bit odd...

### Steps to reproduce

1. Create two user accounts, `attacker_user` and `victim_user` (`attacker_user` must have at least premium features enabled)
2. Log in as `attacker_user`
3. Create a project `xss_project` by going to https://gitlab.com/projects/new#blank_project
4. Go to projects settings on https://gitlab.com/attacker_user/xss_project/edit and scroll down to and expand "Merge request approvals"

{F1450906}

5. Click "Add approval rule"
6. Put the payload as the name, If on Gitlab.com use
```
<iframe/srcdoc='<script/src=/joaxcar_group/first/-/jobs/1415515489/artifacts/raw/data/alert.js></script>'></iframe>
```
if this is tested on a server without CSP feel free to use the payload
```
<script>alert(document.domain)</script>
```
7. Search for and select `attacker_user` as approver and click create rule.

{F1450905}

8. Invite `victim_user` to the project as `Developer` on https://gitlab.com/attacker_user/xss_project/-/project_members
9. Log out and log back in as `victim_user`
10. Go to https://██████████/user_01/pub/-/branches/new and create a branch `new`
11. Directly click on "Create merge request" (which will appear on the screen)

{F1450903}

12. Click on the dropdown at "Reviewers"
13. Payload will trigger

{F1450904}


### Impact

Stored XSS with CSP bypass. Full Javascript functionality without restrictions, so everything from stealing data to generating and exfiltrating access tokens.

### Examples

If you access my private project at Gitlab.com (https://gitlab.com/ultimate-joaxcar-test3/xss) as an admin, you should be able to create an MR and trigger payload. (Just an alert box)

### What is the current *bug* behavior?

Approver rule name is injected in the user information without proper sanitization.

### What is the expected *correct* behavior?

The name should be sanitized


### Output of checks

This bug happens on GitLab.com

## Impact

Stored XSS with CSP bypass. Full Javascript functionality without restrictions, so everything from stealing data to generating and exfiltrating access tokens.

## Attachments
- newMR.png
- fire.png
- create.png
- approvals.png
