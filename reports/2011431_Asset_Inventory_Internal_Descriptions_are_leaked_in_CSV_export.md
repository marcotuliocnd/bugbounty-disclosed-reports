# Asset Inventory Internal Descriptions are leaked in CSV export

## Report Details
- **Report ID**: 2011431
- **URL**: https://hackerone.com/reports/2011431
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-06-02T20:51:17.607Z
- **Disclosed**: 2023-07-12T06:50:57.834Z

## Reporter
- **Username**: archangel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

Hey team,

I was looking at the new Asset Inventory functionality and it looks like as a program I can set an Internal asset description

███

This internal description is meant to be private and can't be seen on the scope page: (https://hackerone.com/█████). 

However, if you export the CSV then it leaks this internal description information

**Description:**

### Steps To Reproduce

1. Navigate to https://hackerone.com/██████████
2. Click the Export to CSV button
3. In the CSV you should see `Internal Description For ES` next to the █████████████ scope item

## Impact

Programs are assuming this asset information is indeed internal and may be storing sensitive information such as internal paths/credentials/etc in this description.

## Attachments
No attachments
