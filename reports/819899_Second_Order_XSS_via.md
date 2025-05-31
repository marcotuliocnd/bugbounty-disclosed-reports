# Second Order XSS via █████

## Report Details
- **Report ID**: 819899
- **URL**: https://hackerone.com/reports/819899
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-16T04:35:44.405Z
- **Disclosed**: 2021-02-18T19:02:30.690Z

## Reporter
- **Username**: un4gi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
A malicious user can use HTML injection to send a malicious chat message to an unsuspecting user, leading to a second order HTML injection/XSS via e-mail. 

**Description:**
This will send an e-mail to the user that they have received a new message, and the malicious message will be sent to the user without first being sanitized. This allows the malicious user to inject HTML via the e-mail sent from an official █████████ mail server.

## Impact
Users can be tricked into visiting a malicious website based on an e-mail they receive from the Air University Service Desk. Additionally, if a user is checking their e-mail from a web browser, malicious code could execute within the victim's browser on behalf of the attacker.

## Step-by-step Reproduction Instructions

1. Create an account on `████████` and browse to `██████`.
███
2. Create a new conversation and send a malicious message containing HTML to another account. This is unfiltered and allows many possibilities, but for this example I used the payload `<base href=//un4.gi>`. This will change any links in the e-mail to route to the domain `un4.gi/path/to/original/file`.
██████████
3. Check your e-mail address from your secondary test account. You should have an e-mail stating that you have a new message. Note that in the image above, the bottom left corner shows that the link that states `You have a new message from unagi unagi` leads to `https://un4.gi/███████sysparm_channelID=████`.
█████
4. An attacker can exploit this by hosting a malicious file at the path `██████sysparm_channelID=<channelIDhere>`. The channelID can be prepared ahead of time, as it is in the URL in the window they originally send the message from. Once visited by the user, the attacker would have endless possibilities.


## Suggested Mitigation/Remediation Actions
Sanitize e-mail messages to prevent them from containing any user generated HTML or Javascript.

## Impact

Users can be tricked into visiting a malicious website based on an e-mail they receive from the Air University Service Desk. Additionally, if a user is checking their e-mail from a web browser, malicious code could execute within the victim's browser on behalf of the attacker.

## Attachments
No attachments
