# Simple CSS line-height identifies platform

## Report Details
- **Report ID**: 256647
- **URL**: https://hackerone.com/reports/256647
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-08-03T17:17:04.960Z
- **Disclosed**: 2017-10-20T14:25:52.280Z

## Reporter
- **Username**: hackerfactor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
There are lots of ways to identify the Tor Browser. (User-Agent string, limited time resolution, no media, etc.) Assume you know it is the Tor Browser. Can you tell what platform?

NOTE: This assumption is well within the scope of the Tor Browser. The Tor Browser does not hide the fact that it is the Tor Browser. Instead, the Tor Browser tries to make all instances of the browser look the same. 

CSS line-height: Different browsers on different platforms have different default line heights. (You can tell this if you have two different browsers set to the same height and showing the same long web page. Paging down will scroll at different rates.) The default value of the CSS line-height identifies the browser and platform. Sample default values:

    normal: IE, Edge, Chrome, Chromium, Opera, or Konqueror
    18px: Safari on MacOSX
    19px: Firefox on Linux or Tor Browser on Linux
    19.2px: Tor Browser on Windows
    19.5167px: Firefox on MacOSX or Tor Browser on MacOSX
    20px: Firefox on Windows or Tor Browser on Windows

For profiling: If the TOR-Browser is identified, then the CSS line-height will specify the platform.

To fix: The TOR-Browser should specify the default line-height. Since the user-agent string claims to be Windows, specifying a line-height of '20px' will appear to be Windows.

This profiling issue permits very simple JavaScript to identify the TOR-Browser platform (MacOS, Windows, Linux).

Working demonstration:
https://hackerfactor.com/private/torture-test21.html

## Attachments
No attachments
