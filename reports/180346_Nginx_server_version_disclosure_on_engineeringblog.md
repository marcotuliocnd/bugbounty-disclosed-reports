# Nginx server version disclosure on engineeringblog

## Report Details
- **Report ID**: 180346
- **URL**: https://hackerone.com/reports/180346
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-11-05T12:23:04.505Z
- **Disclosed**: 2017-11-09T20:10:13.487Z

## Reporter
- **Username**: japz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
Hi Yelp Team,

I have found a little information disclosure on your system with regards to the version of server you are using, due to not properly handling 404 errors , whe you go to the page that i not existing, the exact nginx version was disclosed.

__PoC URL:__ engineeringblog.yelp.com/test

__PoC Screenshot:__ {F33044}

It is important to keep secret of the exact server versions.

__Mitigation:__

You may want to create a customize 404 error page, or you can just simply remove the nginx server version.

Regards
Japz

## Attachments
- Screenshot_2016-11-05-20-13-32.png
