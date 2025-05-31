# Improper santization of edit in list feature at twitter leads to delete any twitter user's list cover photo.

## Report Details
- **Report ID**: 1437004
- **URL**: https://hackerone.com/reports/1437004
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-12-28T03:31:20.621Z
- **Disclosed**: 2023-09-18T19:38:53.356Z

## Reporter
- **Username**: greytesla
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Summary:
Improper santization of edit list feature at twitter leads to delete any twitter user's list cover photo.
from this bug attacker can delete any twitter users list's cover photo.

Description:
Improper santization of edit in list feature at twitter leads to delete any twitter user's list cover photo.
from this bug attacker can delete any twitter users list's cover photo.
as changing a media id in attackers  request makes two entity referring to single photo so when attacker deletes his cover photo automatically the media related to that gets deleted so victims cover photo also gets deleted

## Steps To Reproduce:

Step 1: gain media-id(for cover photo of list) of victim easily accessible by visiting list on victims profile.

Step 2: now from attackers account create a list and change cover photo, intercept the request and change the media id to victims cover photo id. 

Step 3 : after that delete list's cover photo from attackers account it will automatically delete victim list's cover photo .

## Impact:
Security Impact : attacker can delete any twitter users list's cover photo.

## Supporting Material/References:
POC Attached Below

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

Security Impact : attacker can delete any twitter users list's cover photo.

## Attachments
No attachments
