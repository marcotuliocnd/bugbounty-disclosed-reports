# File-drop content is visible through the gallery app

## Report Details
- **Report ID**: 719426
- **URL**: https://hackerone.com/reports/719426
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-21T22:54:00.915Z
- **Disclosed**: 2020-01-31T10:36:24.922Z

## Reporter
- **Username**: nursoda
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
I set up a file-drop on NC 17 (btw, according to https://nextcloud.com/security/ NC17 is not covered - but it should be once it's released!): created folder, set share as upload-only. I access that folder as https://cloud.domain.com/s/randompath - fine: I get the upload interface and cannot see what's in the folder. I (or anyone else) upload(s) something. Still fine. Now I use https://cloud.domain.com/apps/gallery/s/randompath and see everything that gallery can display. In my case, it was an upload folder for pictures, so everything is displayed (and can be downloaded, even if I set "hide download"!).

## Impact

Access all media files uploaded to a (not so secure) file-drop (https://nextcloud.com/file-drop/) folder. Could be critical in, say, a hospital, police, etc.

## Attachments
No attachments
