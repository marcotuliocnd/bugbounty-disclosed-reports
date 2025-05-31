# Posting to Twitter CSRF on php/post_twitter_authenticate.php

## Report Details
- **Report ID**: 249234
- **URL**: https://hackerone.com/reports/249234
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-07-13T11:58:49.259Z
- **Disclosed**: 2017-08-19T08:17:00.859Z

## Reporter
- **Username**: kuromatae
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Hi !

This time, i found a CSRF who can lead to arbitrary writing on twitter account of victim if they have added it to zomato :)

Coupled with a stored XSS, it could be very troublesome to you.

In the page, it seems there is no token check at all.

You can see in the video the CSRF working and here is the POC i used:

`https://www.zomato.com/php/post_twitter_authenticate.php?type=posttweet&message=Hello Zomato Team :)`

Cordially,

Kuromatae.

## Attachments
- Poc_CSRF.mp4
