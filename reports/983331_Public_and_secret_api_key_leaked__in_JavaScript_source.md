# Public and secret api key leaked  in JavaScript source

## Report Details
- **Report ID**: 983331
- **URL**: https://hackerone.com/reports/983331
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-16T10:26:22.203Z
- **Disclosed**: 2020-09-29T11:31:14.110Z

## Reporter
- **Username**: lmhu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
**Summary:** [Summary the vulnerabilities]
I am surfing on the stripo website. I found a sensitive data including authentication key written in public accessible javascript file.

**URL Vulnerability**
https://staging.empleio.stripo.email/main.c1965c58f39a0f4aadc3.js

###Steps To Reproduce:
  * Open staging.empleio.stripo.email and add payloads javascript-fuzz
  * Directory sensitive is ``main.c1965c58f39a0f4aadc3.js`` parse this json files using jsonparseronline
  * and look response bytes In response you can see Sensitive ApiKey Disclosure
  * Sensitive Information has been leaked on this source page ``main.c1965c58f39a0f4aadc3.js``
  * Open your network browser , this javascript source has high files can leads to (DoS)

**Proof On Concept**
```javascript
projectId: null,
userFullName: null,
unSubscribeLink: null,
viewInBrowserLink: null,
initialTab: i.TAB_NAME_CONTENT,
aviaryApiKey: "████████",
youtubeApiKey: "███████",
onChangeFromCodeEditor: null,
onSaveEmail: null,
onSaveTemplate: null,
onUnauthorized: function(e)
```
**Screenshots Proof**
F989906
F989907

## Impact

Information Disclosure & DoS json files

## Attachments
No attachments
