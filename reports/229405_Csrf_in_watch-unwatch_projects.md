# Csrf in watch-unwatch projects

## Report Details
- **Report ID**: 229405
- **URL**: https://hackerone.com/reports/229405
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-17T20:13:14.805Z
- **Disclosed**: 2017-08-17T16:18:23.597Z

## Reporter
- **Username**: ashish_r_padelkar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hello,

When you visit any projects from `https://hosted.weblate.org/` , there is a button provided on top-right called `Watch` / `Unwatch` for each projects. when you click on that button, a POST request is sent which contains csrf token.  But this request also works without that token.

Just hit the urls in your browser and you will be able to `Watch` or `Unwatch` the projects

`https://hosted.weblate.org/accounts/watch/androbd/`
https://hosted.weblate.org/accounts/unwatch/androbd/

where androbd is a project name!

Regrads
Ashish



## Attachments
No attachments
