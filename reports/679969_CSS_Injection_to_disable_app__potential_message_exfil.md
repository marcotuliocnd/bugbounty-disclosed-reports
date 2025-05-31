# CSS Injection to disable app & potential message exfil

## Report Details
- **Report ID**: 679969
- **URL**: https://hackerone.com/reports/679969
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-08-22T20:11:41.820Z
- **Disclosed**: 2019-11-09T17:09:35.512Z

## Reporter
- **Username**: fletchto99
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
Tested on Slack for MacOS v4.0.2 - I've marked this as code injection since there was no "css injection"

1. In the app go to Preferences -> Sidebar
2. Enable custom theming 
3. Set the column BG to `#FFFFFF;} html {display:none;}`
4. The app will no-longer render (this survives re-installs)

If this theme were to be shared to someone unsuspecting they would be unable to use slack, even surviving a reinstall (on mac, untested on other platforms).

Furthermore it _might_ be possible to exfil message data using CSS only. As seen here it is _possible_ to keylog via CSS only https://github.com/maxchehab/CSS-Keylogging/ however I have not been able to come up with a proper PoC of this.

I've marked this as low for now as I don't have a PoC exiling data however I have shown that it is possible to inject to completely disable the app.

## Impact

The app is no longer able to render - there might be the possibility of data exfil but I didn't get a PoC working.

## Attachments
No attachments
