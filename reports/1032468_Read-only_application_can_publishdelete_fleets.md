# Read-only application can publish/delete fleets

## Report Details
- **Report ID**: 1032468
- **URL**: https://hackerone.com/reports/1032468
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-12T12:32:59.749Z
- **Disclosed**: 2021-01-04T17:05:39.356Z

## Reporter
- **Username**: ryotak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
## Summary:
Twitter released [Fleet](https://blog.twitter.com/ja_jp/topics/product/2020/ntroducing-fleets-new-way-to-join-the-conversation-jp.html) yesterday. This feature is working with few APIs, and these APIs are missing permission checks.

## Description:
In `/fleets/v1/create` of `https://api.twitter.com`, there is no check to whether if the application has permission to write to the account. `/fleets/v1/delete` has also this issue.


## Steps To Reproduce:

  1. Install [twurl](https://github.com/twitter/twurl).
  1. Authenticate as a read-only application.
  1. Execute following command: `twurl /fleets/v1/create -X POST --header 'Content-Type: application/json' -d '{"text":"Hey yo"}'`
  1. A fleet with `Hey yo` text will be created.

## Supporting Material/References:
{F1075380}

## Impact

The read-only application can publish fleets without getting Write permission. This issue has a similar impact to #434763

## Attachments
- 2020-11-12_21-28-47.mp4
