# NextCloud is also Accepting OCTET-STREAM Type of Documents instead of jpg or Imge Files Only

## Report Details
- **Report ID**: 271253
- **URL**: https://hackerone.com/reports/271253
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-09-24T04:36:28.669Z
- **Disclosed**: 2019-04-11T19:01:57.714Z

## Reporter
- **Username**: rohit_coder
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Summary: I noticed that NextCloud is accepting  OCTET-STREAM Type of Files Where you have Background/Logo Upload Option. I Believe that NextCloud is Checking for Such Type of Files but i can upload application/octet-stream Type of Documents by Crafting a Special Type of File (In this case i created a .bat file and attached a image into it) and your system accepted that file. Please Check Snapshot for more info. 

How to Reproduce
-------
1. Go to this URL :  settings/admin/theming
2. You will get a option Upload Background PIC 
3. Now open your Chrome Console Network tab to see what type of file is it.
3. Download my attached file "background.bat" and try to upload it there
4. File will be accepted by NextCloud and you can see type of file is OCTET-STREAM in Networks tab of Chrome Console



## Attachments
- Background.bat
- Networks_Snap.PNG
