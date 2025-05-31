# Dashboard sharing enables code injection into ████ emails

## Report Details
- **Report ID**: 904064
- **URL**: https://hackerone.com/reports/904064
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-06-21T02:32:24.925Z
- **Disclosed**: 2021-02-18T19:08:13.432Z

## Reporter
- **Username**: un4gi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
An attacker is able to share their dashboard with other █████████ users. When sharing their dashboard, the message is not fully sanitized for HTML characters before sending to the recipient. This allows the attacker to craft a believable spearphishing e-mail coming from an e-mail address owned by the ███████.

## Step-by-step Reproduction Instructions

1. Create an account or sign into ██████.
2. Browse to ███████/█████
3. Create a dashboard by clicking the dropdown menu and selecting `New Dashboard`.
████
4. Once you create the dashboard, go back to ███/██████ and select the dashboard you created.
5. You should see a `share` icon in the top right. Click this and click `Add groups and users`.
███
6. If you start typing in the `To:` field, a list of names should populate. Select the name of an account you own.
█████████
7. Check the `Send an email invitation box`. Populate the `Message` field with your spearphishing attempt (this can contain various HTML elements) and click `Share`.
██████
8. The victim will receive an e-mail from ██████████ with the injected HTML. As you can see below, the `<img>` tag did not work correctly but the other formatting seemed to work fine. This allows the adversary to get very creative..
██████████
*Note: the message above says "...shared with you by unagi unagi.", however an attacker could simply sign up with a first/last name of "████████" or something similar to make this more believable.*

## Suggested Mitigation/Remediation Actions
Sanitize all HTML tags prior to sending the e-mail to the recipient.

## Impact

An adversary could conduct a spearphishing campaign from an ██████ mail server - the scale of effects would be dependent on the creativity of the attacker and the gullibility of the victim.

## Attachments
No attachments
