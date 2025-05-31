# Security token and handler name leak from window.braveBlockRequests

## Report Details
- **Report ID**: 1668723
- **URL**: https://hackerone.com/reports/1668723
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-08-14T05:32:52.278Z
- **Disclosed**: 2023-06-22T05:51:03.326Z

## Reporter
- **Username**: nishimunea
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

Brave for iOS protects privileged JS to native bridges by using random JavaScript handler names and security tokens.
However, by altering [window.braveBlockRequests](https://github.com/brave/brave-ios/blob/08fb4b0ca43625d706b96158267f0b8da6f63250/Client/Frontend/UserContent/UserScripts/RequestBlocking.js#L6) property from scripts on the web page, these secret values can be stolen.

To be specific, `braveBlockRequests` property is set after the execution of the script on the page. Thus, by setting the malicious property as an immutable property from the page beforehand as shown below, it is possible to prevent overwriting by the legitimate property.
```
Object.defineProperty(window, "braveBlockRequests", {
    enumerable: false,
    configurable: false,
    writable: false,
    value: function(args) { window.args = args } // Steal handler name and token here
});
```

## Products affected: 

* Brave for iOS Version 1.41.1 (22.7.27.20) with the default settings

## Steps To Reproduce:

* Open https://csrf.jp/2022/brave_token_leak.php
* Push "Attack" button in the page
* Secret handler name and security token is shown on the page

## Supporting Material/References:

* Attached is a movie file that demonstrate the above steps to reproduce.

## Impact

The impact depends on which bridge is abused. As further features are implemented in the Brave, its potential risk tends to be increased.

## Attachments
- brave_token_leak.mp4
