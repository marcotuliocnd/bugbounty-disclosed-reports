# chrome://brave can still be navigated to, leading to RCE

## Report Details
- **Report ID**: 415178
- **URL**: https://hackerone.com/reports/415178
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-09-27T06:37:47.407Z
- **Disclosed**: 2018-10-23T19:12:42.279Z

## Reporter
- **Username**: qab
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

'chrome://brave'  can be navigated to using the middle mouse click (or normal click with CTRL held) IFF coming from a bookmark. I am also using a small bug to actually trick a user into bookmarking our crafted URL through drag and drop.

## Products affected: 
Brave: 0.24.0 
V8: 6.9.427.23 
rev: f657f15bf7e0e0c50a2b854c6b05edb59bfc556c 
Muon: 8.1.6 
OS Release: 10.0.17134 
Update Channel: Release 
OS Architecture: x64 
OS Platform: Microsoft Windows 
Node.js: 7.9.0 
Brave Sync: v1.4.2 
libchromiumcontent: 69.0.3497.100

## Steps To Reproduce:

1. Host attached PoC in any web
2. Once opened, you will be instructed to save the html file locally and open it this way
3. Open the saved PoC from local disk
4. Click anywhere to open a popup
5. Drag the anchor tag into the main window bookmark bar (if you never bookmarked anything then just right click and bookmark)
6. Hold CTRL and click on the new bookmark, or right click and press "open in new tab"

## Impact

Navigating to chrome://brave is a bad thing since it can lead to RCE ( https://hackerone.com/reports/395737 )
 
We can also use another bug I filed ( https://hackerone.com/reports/415167 ) which can detect local files. If there is a way to drop HTML files into the local disk (cache or some other possibility) we can then try to use bug 415167 to bypass having to know OS username and any potentially salted folders. If this is achievable we can skip the part where we need to download and open PoC locally. 

It would go something like:

1. Open PoC from web
2. PoC will somehow drop HTML in local disk (I have heard in other reports of possible local file XSS)
3. Using bug 415167 we try to guess OS username + folder path to dropped HTML file
4. Use the bookmark trick as described above.
5. Instruct user to open bookmark with either method described above.

## Attachments
- braveRCE.html
