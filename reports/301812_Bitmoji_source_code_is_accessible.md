# Bitmoji source code is accessible

## Report Details
- **Report ID**: 301812
- **URL**: https://hackerone.com/reports/301812
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-01-02T17:02:30.560Z
- **Disclosed**: 2021-07-31T00:20:32.738Z

## Reporter
- **Username**: rms
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
hi team,

I'm starting my research on snapchat by scanning all sub-domains on all the domains in-scope: snapchat.com, bitmoji.com, etc.

Let's look at one of the urls, [https://rendering-service.prod.us-east.bitstrips.com/](https://rendering-service.prod.us-east.bitstrips.com/)

When I request `GET https://rendering-service.prod.us-east.bitstrips.com/`
The response is  `403 Forbidden`

After searching, I've found [/WEB-INF/](https://rendering-service.prod.us-east.bitstrips.com/WEB-INF/) & [/META-INF/](https://rendering-service.prod.us-east.bitstrips.com/META-INF/) directories, which are accessibles and allow directory listing. 

Inside `/WEB-INF/` we have all the .class files of bitmoji, we can download all the files.

Then by using a java decompiler such as `procyon-decompiler` we reverse the .class files to make those readable. 

best,
hermès.

## Impact

Source code leaked

## Attachments
- Screen_Shot_2018-01-02_at_17.51.06.png
- Screen_Shot_2018-01-02_at_17.51.21.png
- Screen_Shot_2018-01-02_at_17.48.45.png
