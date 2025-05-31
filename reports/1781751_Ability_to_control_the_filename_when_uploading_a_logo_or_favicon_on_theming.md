# Ability to control the filename when uploading a logo or favicon on theming

## Report Details
- **Report ID**: 1781751
- **URL**: https://hackerone.com/reports/1781751
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-11-22T20:46:30.917Z
- **Disclosed**: 2023-04-10T15:59:02.387Z

## Reporter
- **Username**: ctulhu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
Hello,

When uploading a logo or favicon the filename can be controlled by attacker since the ```key``` can be modified which serves as the  filename.


{F2044799}

{F2044800}

{F2044798}

Due to an error the path is also disclosed

{F2044802}

## Steps To Reproduce:
[add details for how we can reproduce the issue]

1. go to ```http://localhost/settings/admin/theming```
2. upload  a logo or favicon
3. intercept the request using burp
4. modify the key

## Impact

The attacker can upload any files directly in the webapp and path disclosure. Combining both information can be useful in later attacks.

## Attachments
- Screenshot_from_2022-11-23_04-36-27.png
- Screenshot_from_2022-11-23_04-34-59.png
- Screenshot_from_2022-11-23_04-19-22.png
- Screenshot_from_2022-11-23_04-40-24.png
