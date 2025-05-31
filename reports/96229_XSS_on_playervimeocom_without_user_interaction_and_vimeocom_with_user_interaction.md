# XSS on player.vimeo.com without user interaction and vimeo.com with user interaction

## Report Details
- **Report ID**: 96229
- **URL**: https://hackerone.com/reports/96229
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-10-27T23:50:31.471Z
- **Disclosed**: 2017-08-31T10:24:45.611Z

## Reporter
- **Username**: stefanovettorazzi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vimeo

## Vulnerability Information
I reported this one in the report #87854, but I was asked to report it again in a separate report.

__Description__

At the end of each video appears the thumbnail of other video from the same user. This thumbnail has the title _More from [name_of_the_user]_.
The problem is that the name of the user is not escaped, which allows to execute Javascript code. 
There is a limit for the length of characters that you can use for the name of the user, but it's enough to exploit it. The way I used for the proof of concept is setting the `window.name` to the Javascript code, and then put `<svg onload=eval(name)></svg>` as the name of the user.

__Proof of concept__
1. Download the file _name_xss_iframe.html_ that I attached.
2. Wait 10 seconds.
3. `prompt(document.domain,document.cookie)` is executed on https://player.vimeo.com.
4. Download the file _name_xss.html_ that I attached.
5. Click on _Watch video_.
6. Click on the button to play the video.
6. Wait 10 seconds.
7. `prompt(document.domain, document.cookie)` is executed on https://vimeo.com.

## Attachments
- name_xss_iframe.html
- name_xss.html
