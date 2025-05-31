# Information disclosure through django debug mode

## Report Details
- **Report ID**: 1434276
- **URL**: https://hackerone.com/reports/1434276
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-12-22T20:15:59.653Z
- **Disclosed**: 2022-09-05T22:56:33.593Z

## Reporter
- **Username**: aliyugombe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Your domain https://szezvzorilla.mtn.co.sz was disclosing information throught django debug mode enable.

## Steps To Reproduce:
Visit https://szezvzorilla.mtn.co.sz/NON_EXISTING_PATH/
You will the information of debugging


## Supporting Material/References:
{F1555934}
  * [attachment / reference]

## Impact

Information disclosure

## Attachments
- Screenshot_at_2021-12-22_13-14-00.png
