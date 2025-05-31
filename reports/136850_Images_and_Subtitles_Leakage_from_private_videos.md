# Images and Subtitles Leakage from private videos

## Report Details
- **Report ID**: 136850
- **URL**: https://hackerone.com/reports/136850
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-06T18:59:47.839Z
- **Disclosed**: 2017-10-18T09:39:08.738Z

## Reporter
- **Username**: opnsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vimeo

## Vulnerability Information
Hello,

There is a Vulnerability in https://player.vimeo.com/video/[VIDEO_ID]

When a Video is private but embedable, there are some information about the video on the source code of the webpage, even if the user is not connected to Vimeo or doesn't have right to access the video.
The following info are leaked on a regular request to https://player.vimeo.com/video/[VIDEO ID] :
-Thumbs_preview : a large "sprite" image contaning between 1 and 120 thumbail captures from the video.
-Link to the subtitles tracks, which can be download by anybody.

In addition, when the request is done via php without "user agent" header, the response is a different, and this time it is the cover image of the video that is leaked in HD.

Non embedable video are not vulnerable. Some private videos that are embedable are not vulnerable but most of them are vulnerable, including "only me", "people I follow", "people I choose" and "password" videos.

------
Proof of Concept 

POC link : http://opnsec.com/vimeo/sprite.php?video=[VIDEO_ID]

I made a program that assemble the leaked info and displays the thumbail as a video with the subtitles if there are active subtitles.

POC requirements :
- POC works better with Chrome, alternatively it works with Internet Explorer, with Firefox the POC will not play video.
- You must replace [VIDEO_ID] by the Vimeo Video Id of a private but embedable video of your choice

POC instruction :
1. Open the POC link after replacing [VIDEO_ID] 
2. If the video is not vulnerable, the webpage will tell you and you have to try another private but embedable video id.
3. If the video is vulnerable, the POC webpage will show the leaked infos.

Example with my private videos :
http://opnsec.com/vimeo/sprite.php?video=165611985
(password video with subtitles)

http://opnsec.com/vimeo/sprite.php?video=164583453
(Only me video with subtitles)

http://opnsec.com/vimeo/sprite.php?video=164547953
("Only people I choose" video)


You can also look at the source code of https://player.vimeo.com/video/[VIDEO ID] and look for :
Thumbail image :
```
"thumb_preview":{"url":"https://i.vimeocdn.com/1462563898-0x460a87ad7791195a99cad7e8d90cc27884cc4d9d/sprite/165611985/120?q=48&h=126&ver=1&w=224&n=4","frame_width":224.0,"height":3780.0,"width":896.0,"frame_height":126,"frames":120,"columns":4.0
```

Subtitles files :
```
text_tracks":[{"lang":"en","url":"/texttrack/4448008.vtt?token=572cf43a_0x73110f8c34c181b72c78140a21768dad684874e4","kind":"subtitles","id":4448008,"label":"English"}]
```

HD Cover Image (only if no user agent in header of request) (strip the image size at the end of the file url to have the highest definition image) :
```
background:url('https://i.vimeocdn.com/video/569517416_640.jpg')
```


-------

If you need more info like POC source code or if the POC doesn't work feel free to contact me.

Regards,

Enguerran Gillier
&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;
&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;

## Attachments
- Vimeo_Leak.png
