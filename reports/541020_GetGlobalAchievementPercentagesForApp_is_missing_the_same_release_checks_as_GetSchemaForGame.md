# GetGlobalAchievementPercentagesForApp is missing the same release checks as GetSchemaForGame

## Report Details
- **Report ID**: 541020
- **URL**: https://hackerone.com/reports/541020
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-04-17T08:05:52.286Z
- **Disclosed**: 2020-02-19T23:28:10.645Z

## Reporter
- **Username**: xpaw
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: valve

## Vulnerability Information
`GetGlobalAchievementPercentagesForApp` API method can be used to reveal achievement names/percentages for games that have not been released yet.

This is not a problem with `GetSchemaForGame` method, which leads me to believe the other method is missing all the relevant checks.

https://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v2/?gameid=██████
https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v1/?appid=████

`GetGlobalAchievementPercentagesForApp` should have the same release state checks as `GetSchemaForGame` as to not leak achievement names.

## Impact

This can be used to reveal and leak work-in-progress achievements for games that have not been released yet.

## Attachments
No attachments
