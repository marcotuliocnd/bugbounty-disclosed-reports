# GPS metadata preserved when converting HEIF to PNG

## Report Details
- **Report ID**: 1069039
- **URL**: https://hackerone.com/reports/1069039
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-30T23:35:39.575Z
- **Disclosed**: 2021-10-21T19:57:10.465Z

## Reporter
- **Username**: ianonavy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
Users who upload HEIC/HEIF files (sometimes called "Live Photos")  to reddit.com or old.reddit.com expect their GPS metadata to be stripped before being displayed publicly. Uploaded HEIC files are converted to PNG, but GPS metadata is incorrectly preserved, in violation of user privacy. The problem is likely device- and browser-agnostic, and mostly affects Safari users on Mac since other devices and browsers either automatically convert to a different format or do not permit HEIC files to be uploaded through the usual user flow.

## Impact:
All users who have submitted HEIC files have their GPS locations exposed publicly, which can be scraped with little detection and no authorization.

## Steps To Reproduce:

1. Take a Live photo on an iPhone 11 Pro with GPS location tagging enabled
2. Sync the photo to iCloud Photos
3. Upload HEIF/HEIC file to Reddit.com via Safari on macOS Big Sur (Example F1138749)
4. Submit post to any community
5. Visit the post and click the link to get to the https://i.redd.it/FILENAME.png file
6. Download the file

## Supporting Material/References:

Expected behavior is no GPS metadata, but you can see that **the metadata is present in these examples**:
* https://i.redd.it/s7vjzg05w6861.png (Safari)
* https://i.redd.it/6wnf9cf637861.png (Safari)
* https://i.redd.it/d1zqv32297861.png (Safari)
* https://i.redd.it/8ytwrr5re7861.png (IE)

{F1138750}

I was also able to reproduce this flow through Internet Explorer on Windows 10 (but not Edge), which means the issue is **likely device- and browser-agnostic.**

However, when I tested the following flows, I found that **GPS metadata was correctly removed for**:
* Reddit iOS app on iPhone
* Safari on iPad (local testing shows iOS converts it to a JPEG before uploading)

For some tests, **I wasn't able to upload HEIC photos at all**:

* Chrome and Firefox on Mac (HEIC not supported by image/* MIME filter on accept attribute)
* Chrome, Firefox, and Edge on Windows (Windows does not recognize HEIC as an image file)
* Safari on iPhone (no option to upload photos on mobile view)
* Safari on Mac after having changed the file extension from .HEIC to .PNG (not actually changing the file otherwise)

It seems likely that **only Safari for Mac and Internet Explorer** allow HEIC files to be uploaded directly to Reddit. All other methods I've tried seem to result in normal metadata scrubbing.

**I was able to find location data for at least one other user in the wild:** https://i.redd.it/1hn2uafmwu661.png ([post](https://www.reddit.com/r/BotanicalPorn/comments/kil6om/prunus_mume_buds_encased_in_ice_oc/)). Downloading this image, I can see their GPS location:

{F1138751}

**I originally discovered this when spot-checking an image** that I uploaded yesterday. The post can be found [here](https://www.reddit.com/r/flying/comments/kmm32s/i_made_a_checklist_for_my_car_can_you_tell_it_was/), and the image was [here](https://i.redd.it/5oe2cj40q6861.png). I have since deleted the image.

## Impact

All users who have submitted HEIC files have their GPS locations exposed publicly, which can be scraped with little detection and no authorization.

## Attachments
- Screen_Shot_2020-12-29_at_5.00.34_PM.png
- Screen_Shot_2020-12-29_at_6.53.02_PM.png
- Screen_Shot_2020-12-29_at_6.53.24_PM.png
