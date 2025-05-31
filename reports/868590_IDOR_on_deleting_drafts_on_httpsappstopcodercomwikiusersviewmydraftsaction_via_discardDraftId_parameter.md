# IDOR on deleting drafts on https://apps.topcoder.com/wiki/users/viewmydrafts.action via discardDraftId parameter

## Report Details
- **Report ID**: 868590
- **URL**: https://hackerone.com/reports/868590
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-07T23:27:18.938Z
- **Disclosed**: 2020-05-12T14:42:17.910Z

## Reporter
- **Username**: meryem0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lab45

## Vulnerability Information
Hi :)

On https://apps.topcoder.com/wiki/users/viewmydrafts.action, you can see your drafts, edit or delete them. Users can delete their own drafts on `https://apps.topcoder.com/wiki/users/viewmydrafts.action?discardDraftId=<DRAFT_ID>`. 
But there is no check and an attacker can change `discardDraftId` and delete all drafts.

## Impact

An attacker can delete other user's drafts.

## Attachments
No attachments
