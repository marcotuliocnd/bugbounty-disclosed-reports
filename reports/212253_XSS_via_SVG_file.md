# XSS via SVG file

## Report Details
- **Report ID**: 212253
- **URL**: https://hackerone.com/reports/212253
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-10T12:27:56.852Z
- **Disclosed**: 2017-05-01T12:30:45.062Z

## Reporter
- **Username**: 0xspade
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
# Hello Ubuquiti,

# Details
I was able to upload an svg file to [here](https://community.ubnt.com/t5/media/gallerypage/user-id/559584). so i uploaded an SVG file with XSS on its code and if the attacker give the link to his victim he can grab it's victim's cookie.
and regarding to the your Upload image svg file it uploaded even it has an error..

# PoC
[link](https://community.ubnt.com/t5/image/serverpage/image-id/0i9D3EF39FC6246359/image-size/thumb/is-preview/true?v=1.0&px=100)
{F167791}

# Fix

Dont allow to upload an svg file because attacker can put his payload to a SVG files.

## Attachments
- xss.png
- evilsvgfile_(1).svg
