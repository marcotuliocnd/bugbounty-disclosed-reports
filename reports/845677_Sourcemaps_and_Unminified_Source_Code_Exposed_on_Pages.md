# Sourcemaps and Unminified Source Code Exposed on Pages

## Report Details
- **Report ID**: 845677
- **URL**: https://hackerone.com/reports/845677
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-09T20:17:26.203Z
- **Disclosed**: 2020-05-07T21:29:08.077Z

## Reporter
- **Username**: gennaro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: imgur

## Vulnerability Information
Hello,

I'm not sure if this was actually meant to be made public on purpose, but I was looking through some of the sources that were loaded and found out the following: 

* https://imgur.com/ - See ██████
    * s.imgur.com -> desktop-assets -> js 
        * contains multiple minified JS files as one would usually expect. 

In the following pages(But not limited too), we see: 
* https://imgur.com/upload
* https://imgur.com/account/settings/*
* https://{username}.imgur.com/all
* https://imgur.com/account/messages
    * s.imgur.com -> include -> js
        * As we can see on the following pages this contains a "minified" folder and then all the uniminified corresponding source code files.
        * See █████████

## Impact

Assuming the unminified source files were not intentionally left exposed to the public: 
* Loss of internal confidentiality 
* Source code can be stolen
* Internal documentation exposed to the public can create a target to dev environments that are traditionally not meant to be publicly facing
    * e.g. ███████ shows a link to: ████████████/████████
    * a simple scan I was able to find what seems to be multiple dev builds of the site and access to the git login, VPN login, etc: ██████████.███████/

Though these are not direct exploits to systems, it does create un-needed attention to additional points of entry to source code repos, internal documentation, and potentially other company confidential information. 

I hope this was helpful!

## Attachments
No attachments
