# RTLO char allowed in chat

## Report Details
- **Report ID**: 196222
- **URL**: https://hackerone.com/reports/196222
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-06T10:04:23.151Z
- **Disclosed**: 2017-02-28T19:44:57.677Z

## Reporter
- **Username**: kontez
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
Hey all,

There seems to be no filtering of strange unicode characters such as U+202E which is an Right-To-Left-Override.
I can send messages like "Hey check out my new song at example.com/song[rtlo]3pm.exe" and everyone would see the link as "example.com/songexe.mp3". 
Links that end with .exe are very suspicious but everyone would click on a link that ends with .mp3, filtering those characters would prevent clickjacking.
I tested this on the latest version of the Android App.

Thanks,
Marvin

## Attachments
- photo59550190166717602.jpg
