# XSS when using captions/subtitles on video player based on Flash (requires user interaction)

## Report Details
- **Report ID**: 88508
- **URL**: https://hackerone.com/reports/88508
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-09-11T16:55:43.845Z
- **Disclosed**: 2017-08-31T10:27:29.285Z

## Reporter
- **Username**: stefanovettorazzi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vimeo

## Vulnerability Information
__Description__

The video player based on Flash (not the HTML5 one), shows the captions/subtitles without escaping. This allows to upload a file with captions/subtitles with HTML code, because the content of the file is not escaped when it's stored.
The way to force the use of the Flash player is using the widget Hubnut, because on Chrome for example the default player is the HTML5 one.

__Proof of concept__

1. For easy reproduction of the proof of concept, create a new account or delete every video in your account or make every video private.
2. Upload a video or use an existing video.
3. Go to the Settings of the video.
4. Click on the tab _Advanced_.
5. Download the file _English.vtt_ that I attached to the report.
6. In the section "Add Captions & Subtitles", click on _Choose file_.
7. Select the file you downloaded in step 5.
8. When the file is uploaded, click on _OFF_ in the column _Status_. The value should change to _ON_.
9. Select _English_ in the column _Language_.
10. Select _Captions_ in the column _Type_.
11. Click on _Save Changes_.
12. Using other account, go to https://player.vimeo.com/hubnut/user/[user_url] (like https://player.vimeo.com/hubnut/user/user36690798).
13. Click on _Play_.
14. Click on _CC_ (at the right bottom of the player) and click on _English_,  to activate the captions.
15. `alert(document.domain)` is executed.

You can reproduce the issue using this link https://player.vimeo.com/hubnut/user/user36690798.

## Attachments
- English.vtt
