# Cards in Deck are readable by any user

## Report Details
- **Report ID**: 1331728
- **URL**: https://hackerone.com/reports/1331728
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-09-07T11:21:19.390Z
- **Disclosed**: 2023-03-26T16:03:04.254Z

## Reporter
- **Username**: shakierbellows
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
Allows any user access to sensitive deck card contents.

## Steps To Reproduce:

  1. User creates a new "deck" and "stack".
  1. Create another user on your Nextcloud instance.
  1. curl -X GET -H "OCS-APIREQUEST: true" "http://localhost/index.php/apps/deck/api/v1.0/boards/1/stacks/1" -u hacker

As an output you get things like for example {title":"To do",,"cards":[{"title":"Example Task 3","}

## Impact

Allows any user access to sensitive deck card contents.

## Attachments
No attachments
