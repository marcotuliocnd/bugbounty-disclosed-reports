# Memory Corruption via Large Pixels

## Report Details
- **Report ID**: 282518
- **URL**: https://hackerone.com/reports/282518
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-10-24T15:04:24.266Z
- **Disclosed**: 2024-02-01T15:41:38.853Z

## Reporter
- **Username**: mr_r3boot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
I would like to report a memory corruption issue.

#PoC:
The exploit is really simple. I have an image of 5kb, 260x260 pixels. In the image itself I exchange the 260x260 values with 0xfafa x 0xfafa (so 64250x64250 pixels). Now from what I remember your service tries to convert the image once uploaded. By loading the 'whole image' into memory, it tries to allocate 4128062500 pixels into memory. which may cause some backend processing memory corruption issues.

Please have a look on attached video.

#Fix:
Proper resolution checks on image uploads.

Regards,
Mr.R3boot.

## Attachments
- ResolutionCheck.mp4
