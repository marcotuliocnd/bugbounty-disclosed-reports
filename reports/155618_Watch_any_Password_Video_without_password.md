# Watch any Password Video without password

## Report Details
- **Report ID**: 155618
- **URL**: https://hackerone.com/reports/155618
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-31T15:41:44.639Z
- **Disclosed**: 2017-10-18T09:41:06.126Z

## Reporter
- **Username**: opnsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vimeo

## Vulnerability Information
Hello Jeremy and Vimeo Security Team,

There is a vulnerability in Vimeo which allows any user to watch password video without the password.
A user can like a passworded video without password, then the user can watch the video on Couchmode without the password.

POC link : http://opnsec.com/vimeo/PasswordBypass.html

Description : 
This POC demonstrates how to watch my passworded Vimeo Video without password
Password Video : https://vimeo.com/176931370

Instructions : 
1. You must be logged in Vimeo
2. Open the POC link and follow instructions.
3. You should be able to watch my "Ski Movie" video without password

-----
Technical description :

There are 2 steps in this vulnerabilty :
First, it is possible to like a password video without password. There is no need of password to open `https://player.vimeo.com/video/[VIDEO_ID]/config` which contains the tokens (session, signature, timestamp) required to like the video. Sending these tokens via a POST request to `https://player.vimeo.com/video/[VIDEO_ID]/like`
(megaloop.swf uses this request to like a video) will make the video like in user profile. Note that there is the same vulnerability with "watch_later" (`https://player.vimeo.com/video/[VIDEO_ID]/like`)

After that, the Couchmode allows to watch a "liked"/"watch later" video without asking for password.

----
Mitigation :

For the "liked"/"watch later" vulnerability, the server should reject the like request until a valid password is provided. This could easily be done by asking the password automatically each time the video is liked for example.

Regarding the Couchmode, it might be better to ask for password or not include any password video.

---

If you need more info feel free to ask,

Enguerran @opnsec

## Attachments
No attachments
