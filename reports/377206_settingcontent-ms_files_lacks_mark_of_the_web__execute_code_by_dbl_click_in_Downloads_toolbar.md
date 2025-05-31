# `settingcontent-ms` files lacks "mark of the web" => execute code by dbl click in Downloads toolbar

## Report Details
- **Report ID**: 377206
- **URL**: https://hackerone.com/reports/377206
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-07-04T19:36:14.482Z
- **Disclosed**: 2018-10-04T00:52:46.884Z

## Reporter
- **Username**: metnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

`settingcontent-ms` files allow launching any binary with any params.
Brave doesn't mark `settingcontent-ms` files with "mark of the web", so the file could be executed by double click in "Downloads" toolbar. Launched `settingcontent-ms` file could lead to code execution with user-level privileges. 

## Products affected: 
Brave: 0.23.19
Muon: 7.1.3
OS: 10.0.17134 (the image was downloaded today from the MS virtualbox images page)
Chromium: 67.0.3396

## Steps To Reproduce:

1. Download `twitter.settingcontent-ms` from attachments.
2. Dbl click on the item in "Downloads" toolbar.
3. Calculator opens (but as I said, it's possible to launch anything).

PoC/Screencast additionally leverages #375259.

## Supporting Material/References:

1. FF patched this somewhere between 60-62 version
2. This bug still works in Edge. As far as I know, that's 1-day.
3. Chrome downloads `settingcontent-ms` files only after a confirmation from the user.
4. This problem is already popular, so you could easily find more info.

PoC + screencast attached.
[Live PoC:](https://win-settingcontent-ms-uosardvltp.now.sh)  (not sure that it works, it'd be better to test it locally)

## Impact

Launched `settingcontent-ms` could lead to code execution with user-level privileges. 
Marked as "high", because it's a native OS feature, all Win users are affected.

## Attachments
- exploit.html
- twitter.settingcontent-ms
- brave-win-settingcontent-ms.mp4
