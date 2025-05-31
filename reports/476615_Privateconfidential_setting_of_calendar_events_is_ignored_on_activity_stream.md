# Private/confidential setting of calendar events is ignored on activity stream

## Report Details
- **Report ID**: 476615
- **URL**: https://hackerone.com/reports/476615
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-08T16:10:21.614Z
- **Disclosed**: 2019-06-27T08:45:58.518Z

## Reporter
- **Username**: nickvergessen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
https://github.com/nextcloud/server/pull/13331

Events that are private should not generate events for other users
Events that are confidential should not leak the name to other users

## Impact

The details are leaked to other users

## Attachments
No attachments
