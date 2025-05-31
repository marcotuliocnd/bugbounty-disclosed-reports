# Public and secret api key leaked in JavaScript source

## Report Details
- **Report ID**: 1051029
- **URL**: https://hackerone.com/reports/1051029
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-05T06:38:02.571Z
- **Disclosed**: 2021-01-19T20:14:30.923Z

## Reporter
- **Username**: lmhu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: top_echelon_software

## Vulnerability Information
**Summary: [Summary the vulnerabilities]**
I am surfing on the bb3jobboard.topechelon.com website. I found a sensitive data including authentication key written in public accessible javascript file.

**URL Vulnerability**
  * https://bb3jobboard.topechelon.com/#!/search?page=1

###Steps To Reproduce:
  * Open bb3jobboard.topechelon.com and add payloads javascript-fuzz
  * Directory sensitive is ``//job_board.js//`` parse this json files using jsonparseronline
  * and look response bytes In response you can see Sensitive ApiKey Disclosure
  * Sensitive Information has been leaked on this source page job_board.js
  * Open your network browser , this javascript source has high files can leads to (DoS)

**Proof On Concept**
```javascript
}]), angular.module("jb").config(["lkGoogleSettingsProvider", function(e) {
    e.configure({
        apiKey: "██████████",
        clientId: "██████t.apps.googleusercontent.com",
        scopes: ["https://www.googleapis.com/auth/drive.readonly"],
        features: ["MULTISELECT_DISABLED"]
    })
}]), angular.module("jb.factories").factory("BoardSettingsFactory", ["railsResourceFactory", "PathToResourceRoute", function(e, t) {
    var n = e({
        url: t.convert(JBRoutes.jobBoardBoardSettingsPath),
        name: "boardSettings"
    });
```
**Screenshots Proof**
████

## Impact

Information disclosure

## Attachments
No attachments
