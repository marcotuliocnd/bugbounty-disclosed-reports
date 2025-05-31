# IDOR in backup recovery functionality

## Report Details
- **Report ID**: 1901713
- **URL**: https://hackerone.com/reports/1901713
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-03-12T01:02:24.410Z
- **Disclosed**: 2024-11-13T13:51:35.445Z

## Reporter
- **Username**: theelgo64
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
Hi team I hope you are well, there is an issue let me to takeover any backup via recover it to my machine.

## Steps To Reproduce
1. Login https://mc-beta-cloud.acronis.com
2. Visit the DEVICES section [you must have 2 devices]
3. Click on any device has a backup [device_1]
4. Click on recovery > select machine > select the second machine [device_2]
5. follow the steps to recover the backup to [device_2]
6. In the burp search for this endpoint ```/bc/api/ams/recovery/plan_operations/run```
7. Send the request again via ==X-Apigw-Session== session from another organization.


## POC

{F2222128}

## Impact

- Backup Takeover via recovery function.

## Attachments
- backupTakeover.mp4
