# Talk Android broadcast receiver is not protected by broadcastPermission allowing malicious apps to communicate

## Report Details
- **Report ID**: 1596459
- **URL**: https://hackerone.com/reports/1596459
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-06-10T06:54:22.475Z
- **Disclosed**: 2022-12-25T11:23:57.479Z

## Reporter
- **Username**: andyscherzinger
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
Call to registerReceiver misses the broadcastPermission argument - no permissions will be checked for the broadcaster, which allows a malicious application to communicate with the broadcast receiver.

## Supporting Material/References:

  * Screenshot Snyk report
 * references to fixes in other repos

https://github.com/alvinhkh/buseta/commit/6b791de8e3622ef157b065f9c82fcfd5a0e2302a?diff=split#diff-a75527f97c6732197964c1dbf30fd385L66

https://github.com/serso/android-messengerpp/commit/1528fdc2d3561bab192dfde9a84a737a26a19fce?diff=split#diff-7ff52f2abe79bd0a68d54916fe71aef2L92

https://github.com/irccloud/android/commit/857287d6d9da443b0ff667505d5bf4a383922784?diff=split#diff-f06bf5e27b9130d322139330f7f31997L40

## Impact

Unsure, potentially interfere with call starts and audio/bluetooth setup

## Attachments
- 2022-06-10_08_41_16-talk-android___Snyk___Mozilla_Firefox.png
