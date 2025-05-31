# Arbitrary file read via ffmpeg HLS parser at https://www.flickr.com/photos/upload

## Report Details
- **Report ID**: 487008
- **URL**: https://hackerone.com/reports/487008
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-01-27T21:25:51.237Z
- **Disclosed**: 2020-01-25T00:03:06.058Z

## Reporter
- **Username**: asad0x01_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: flickr

## Vulnerability Information
Summary: FFmpeg is a video and audio software that is used for generating previews and for converting videos. Your current installation allows HLS playlists that contain references to external files, which leads to local file disclosure.


Steps to Reproduce:
1.Download the attached file. {F413554}

2.Go to https://www.flickr.com/photos/upload/ and upload the attached file.

3.Now go to https://www.flickr.com/cameraroll and you should be able to see contents of /etc/passwd. {F413555}
For clear view open the video from **Photostream** section.

Please let me know if you need any help :)

## Impact

An attacker can read files of etc/passwd or other contents.Also what I've seen it is possible to escalate this vulnerability to SSRF(https://www.blackhat.com/docs/us-16/materials/us-16-Ermishkin-Viral-Video-Exploiting-Ssrf-In-Video-Converters.pdf).Since I don't have any server I couldn't test :(

## Attachments
- READ__etc_passwd.avi
- Screenshot_2019-01-28_at_3.24.17_AM.png
