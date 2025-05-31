# Deprecated owners.query API bypasses object view policy

## Report Details
- **Report ID**: 1584409
- **URL**: https://hackerone.com/reports/1584409
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-05-28T18:39:07.653Z
- **Disclosed**: 2022-05-31T19:14:20.187Z

## Reporter
- **Username**: dyls
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
The deprecated owners.query API does not check object view policy. A user is able to view some information about an owner package which they do not have permission to see by calling this API. Since the API is deprecated, it could just be removed.

## Impact

An attacker is able to view some information about an owner package that they should not be able to see. Including, name, description, owner PHIDs, and repository PHIDs, and a path (which may be a path that belongs to a restricted repository).

## Attachments
No attachments
