# IDOR while uploading ████ attachments at [█████████]

## Report Details
- **Report ID**: 1196976
- **URL**: https://hackerone.com/reports/1196976
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-05-14T04:39:24.572Z
- **Disclosed**: 2021-06-30T20:47:06.093Z

## Reporter
- **Username**: rook1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
There is an IDOR vulnerability in uploading attachments to the ████ section where an attacker can upload attachments in other user's █████████ if there is no attachment uploaded by a user. If this vulnerability will be used with a Race condition, it can allow an attacker to upload attachments in all-new █████████ created by users.

## Impact

A user can upload attachments to other users ███.

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Go to ██████
2. Login
3. Go to https://███/█████
4. Add a new █████████ and upload an attachment with that and submit it.
5. Send the request to the repeater.

████
6. Change the `███Id` parameter value to the victim user's ██████████ id.

█████████
7. Click on the send button and you will see `success` in response.
8. It will be uploaded in the victim user █████ section.

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
