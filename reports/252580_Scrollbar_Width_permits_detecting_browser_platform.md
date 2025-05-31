# Scrollbar Width permits detecting browser platform

## Report Details
- **Report ID**: 252580
- **URL**: https://hackerone.com/reports/252580
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-07-22T17:06:37.415Z
- **Disclosed**: 2017-10-20T14:26:22.617Z

## Reporter
- **Username**: hackerfactor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
In April 2017 (shortly before this bug bounty program went live), I repeatedly attempted to report this information disclosure vulnerability. However, my emails to the Tor Project's official vulnerability disclosure address went unanswered. It was not until I posted a public blog entry -- with a working exploit -- that someone at the Tor Project opened a bug about this issue. Shortly after that bug, the Tor Project opened this bug bounty system to the public.

The blog entry about the bug: http://www.hackerfactor.com/blog/index.php?/archives/761-Exploiting-the-TOR-Browser.html

The bug that was submitted to the Tor Project by  Georg Koppen: https://trac.torproject.org/projects/tor/ticket/22137

I believe the Tor Project opened this bug bounty system to the public BECAUSE of my bug and my identification of no method to report vulnerabilities to the Tor Project. As such, I'm hoping that this bug can be accepted into the now-public bug bounty system.

The bug:
The Tor Browser is based on Firefox. Firefox defaults to different scrollbar widths depending on the platform (Windows, Mac, and various Linux desktops). Javascript can easily calculate the scrollbar width, permitting the web page to identify the platform.

Even though the Tor Browser is designed to look the same on all platforms, this bug allows a hostile web site to distinguish "Tor on Windows" from "Tor on Mac" from "Tor on Ubuntu with Unity desktop" from "Tor on Debian with Gnome desktop" etc.  Even two people using the same Tor Browser version on two different Linux systems may appear distinct.

For a low-volume web site, this distinction is enough to track users uniquely. For a high-volume web site, it permits tracking users uniquely over a short timeframe -- at least until other people with similar profiles show up.

This one attribute can be combined with other browser attributes in order to develop a unique-enough profile for tracking users over Tor.

## Attachments
No attachments
