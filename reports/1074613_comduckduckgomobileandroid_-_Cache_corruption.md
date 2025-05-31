# com.duckduckgo.mobile.android - Cache corruption

## Report Details
- **Report ID**: 1074613
- **URL**: https://hackerone.com/reports/1074613
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-08T18:52:34.392Z
- **Disclosed**: 2021-09-26T23:08:52.356Z

## Reporter
- **Username**: webklex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: duckduckgo

## Vulnerability Information
## Summary:
By opening a special url, the app cache can be corrupted which can't be resolved by the user without reinstalling the app.

## Steps To Reproduce:
1.) Download and install the DuckDuckGo App
2.) Open `https://%22t.dev/`
3.) Try to reopen the app (The app keeps crashing)

## Additional information
- Tested on Android 8.1 and 9 with the latest app release (5.73.0)
- Problematic seems to be the encoded `"` (%22)

## Mitigation
- Store the url urlencoded

## Impact

An attacker can corrupt someones app cache and prevent the user from continuing using the app.

## Attachments
No attachments
