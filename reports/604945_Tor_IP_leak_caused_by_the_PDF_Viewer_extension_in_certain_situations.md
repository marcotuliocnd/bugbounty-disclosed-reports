# Tor IP leak caused by the PDF Viewer extension in certain situations

## Report Details
- **Report ID**: 604945
- **URL**: https://hackerone.com/reports/604945
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-06-09T23:40:55.402Z
- **Disclosed**: 2023-08-02T19:27:18.358Z

## Reporter
- **Username**: world_languages
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:
Web requests made by browser extensions in the Tor profile aren't proxied if the user didn't load any HTTP/HTTPS website in a Tor window since the browser first launched.

This wouldn't really be a problem because extensions can't be used in Tor windows. However, Brave has some built-in extensions (Brave, Brave Rewards, Brave WebTorrent, PDF viewer) that also run in Tor mode. This last one can cause problems.

If:
- The user didn't visit any HTTP/HTTPS page with Tor in that browser session.
- The user goes to `chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/pdf-url` in a Tor window.

Then the server hosting `pdf-url` will get the real IP address of the user, even tho the PDF was loaded in a Tor window.

This happens because the PDF viewer extension requests the PDF as an AJAX request, and as mentioned before, requests aren't proxied until an HTTP/HTTPS address is loaded with the address bar in a Tor window (or you "duckduckgo" something).

## Products affected: 
This was tested in the most recent versions of Brave Stable & Dev, in a Windows 10 PC.
Stable: 0.65.118 Chromium: 75.0.3770.80 (Official Build) (64-bit) 
Dev: 0.67.77 Chromium: 75.0.3770.80 (Official Build) dev (64-bit)

## Steps To Reproduce:
1. Close Brave normally.
2. Make sure Brave is actually closed (if the Brave icon is in the Windows toolbar, right click it and press exit. You can also use task manager to kill the processes).
3. Open Brave again.
4. Open a Tor window. Don't open any website in the Tor window before step 5.
5. Go to this URL:  `chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/http://ip-pdf.glitch.me/ `. The request to glitch.me won't be proxied with Tor - you'll see the PDF returned by it will include your real IP address.
6. (optional) Load a website in the Tor window as a new tab (e.g. duckduckgo.com).
7. (optional) Refresh the PDF. You'll see the request to get the PDF is now proxied, because an HTTP website has been loaded.

## Supporting Material/References:

Node JS server for ip-pdf (source): https://glitch.com/~ip-pdf

## Impact

All HTTP/HTTPS requests, AJAX or not, are supposed to be proxied in Tor windows. This doesn't happen in this situation, leading to an IP leak.
However, the severity isn't high because certain conditions must be met for this to happen.

## Attachments
No attachments
