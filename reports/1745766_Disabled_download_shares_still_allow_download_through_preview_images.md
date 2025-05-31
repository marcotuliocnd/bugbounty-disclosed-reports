# Disabled download shares still allow download through preview images

## Report Details
- **Report ID**: 1745766
- **URL**: https://hackerone.com/reports/1745766
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-10-21T13:59:15.495Z
- **Disclosed**: 2022-12-31T09:33:06.093Z

## Reporter
- **Username**: juliushaertl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:

## Steps To Reproduce:

  1. Share a folder and disable the "Allow download" permission
  2. Now as the recipient of the file you can still download the preview of the file

This is an issue for images but also for shared documents where viewing them in Collabora would present them watermarked but the preview would leak the first page without an watermark.

## Impact

Images could be downloaded and previews of documents (first page) can be downloaded without being watermarked.

## Attachments
No attachments
