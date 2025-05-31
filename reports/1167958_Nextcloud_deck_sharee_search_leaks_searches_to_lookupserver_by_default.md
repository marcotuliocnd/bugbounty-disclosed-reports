# Nextcloud deck sharee search leaks searches to lookupserver by default

## Report Details
- **Report ID**: 1167958
- **URL**: https://hackerone.com/reports/1167958
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-04-18T20:17:32.143Z
- **Disclosed**: 2021-05-26T10:01:52.352Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
So, in short this is related to the other 2 reports https://hackerone.com/reports/1167916 and https://hackerone.com/reports/1167919

While I could not find deck on your h1 page. I kind of assume it is in scope as well as this is something you sell with the 'groupware' subscription (
https://nextcloud.com/groupware/ ).

In short. In the default setup if you search for people to share a deck board with the query will be send to the lookup server. Which the user is not told about.

## Impact

See the other reports.

## Attachments
No attachments
