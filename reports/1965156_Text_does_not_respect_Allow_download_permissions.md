# Text does not respect 'Allow download' permissions

## Report Details
- **Report ID**: 1965156
- **URL**: https://hackerone.com/reports/1965156
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-04-28T09:52:06.038Z
- **Disclosed**: 2023-08-23T14:55:38.293Z

## Reporter
- **Username**: rullzer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
1. user0 shares a folder of sensitive images to user1 without the 'Allow download' permission
2. user1 just creates a new text file and inserts the images into it
3. Voilla the images appear and can be downloaded easily

These are just previews but still.
For the most common types you can even request the raw image https://github.com/nextcloud/text/blob/main/lib/Controller/AttachmentController.php#L57-L67

## Impact

A user assume that the allow download feature works can still have their sensitive photos leaked.

## Attachments
No attachments
