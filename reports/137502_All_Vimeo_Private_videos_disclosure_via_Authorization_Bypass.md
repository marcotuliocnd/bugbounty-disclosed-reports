# All Vimeo Private videos disclosure via Authorization Bypass

## Report Details
- **Report ID**: 137502
- **URL**: https://hackerone.com/reports/137502
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-10T14:50:25.496Z
- **Disclosed**: 2016-07-29T12:03:07.183Z

## Reporter
- **Username**: opnsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vimeo

## Vulnerability Information
Hello,

There is a vulnerability in `https://vimeo.com/[VIDEO_ID]?action=share` that makes all Vimeo private videos available to anybody.

POC link :
http://opnsec.com/vimeo/vl/videoLeak.php?video=[VIDEO_ID]

POC requirements :
- No need to be logged in Vimeo
- Because of sensitivity of this, I put a password on the POC :
username : vimeo
password : aS3cr3tP4$$wrD7854123

POC instructions :
1. Open the POC link replacing `[VIDEO_ID]` by any Vimeo private video id (I believe all type of private videos are vulnerable)
2. Enter the username and password as per requirements 
3. If the Vimeo video id is correct, no matter the status of the video, the video should start playing.

---------

Technical description :

`https://vimeo.com/[VIDEO_ID]?action=share` is an Ajax link used to ask Vimeo for the "Share" code to embed the video
Because it is Ajax, the server is only replying if the `Header X-Requested-With is set to XMLHttpRequest`.

If the Attacker send this request with a [VIDEO_ID] of a private video that he don't have access to, the server reply with an error message. However, this message contains the link to the `config` file of the private video including a `token parameter s=[SECRET]` which will grant the attacker access to the config file.
The config file contains all the info about the video including the actual video file links, video title, owner vimeo account, ... which means that the attacker has complete access to the video.

Example of config file with `token parameter s=[SECRET] `
```
https://player.vimeo.com/video/165266592/config?autoplay=0&byline=0&bypass_privacy=1&context=Vimeo%5CController%5CClipController.main&default_to_hd=1&portrait=0&title=0&s=bb016a22af815053eb54XXXXXXX019d8_1462989197
```
------
Vulnerability Mitigation 

To resolve this issue, the `https://vimeo.com/[VIDEO_ID]?action=share` server should not include the token parameter `s=[SECRET]` of the config file in the error response of `https://vimeo.com/[VIDEO_ID]?action=share`if the user doesn't have right to access the video.
There is a good chance this vulnerability is present in other links, especially other Ajax links.

In addition, if that is possible, the `https://player.vimeo.com/video/[VIDEO_ID]/config` config file server should also check that the user has valid right to access the video even if he has a correct `s=[SECRET]` token

-------------

Here is the source code of `http://opnsec.com/vimeo/vl/videoLeak.php`

If you need more info or if the POC doesn't work feel free to contact me.

Regards,

Enguerran Gillier
&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;
&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;

## Attachments
- videoLeak.php
