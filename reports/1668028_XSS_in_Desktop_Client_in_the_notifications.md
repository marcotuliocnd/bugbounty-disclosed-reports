# XSS in Desktop Client in the notifications

## Report Details
- **Report ID**: 1668028
- **URL**: https://hackerone.com/reports/1668028
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-08-12T19:00:00.628Z
- **Disclosed**: 2022-11-25T11:29:58.569Z

## Reporter
- **Username**: b911bade858ce8e6a0f50f8
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
The `Nextcloud Desktop Client` application does not properly neutralize the names of files before using them.

## Steps To Reproduce:

### Server Machine
1. Install the `Nextcloud Server` application
2. Log into your account

### Client Machine
3. Install the `Nextcloud Desktop Client` application onto a machine that is running the `Windows 10` operating system
4. Log into your account

### Server Machine
5. Upload any file to your `Nextcloud Server` instance
6. Rename the file that you uploaded to `<h1><b><i><u>MikeIsAStar`

### Client Machine
7. Wait until a notification appears exclaiming that some files could not synchronized
8. Open the main dialog window of the `Nextcloud Desktop Client` application
9. Observe that the name of the file that you uploaded is treated as `HyperText Markup Language`

## Supporting Material/References:
{F1864812}

## Impact

An attacker can inject arbitrary `HyperText Markup Language` into the `Nextcloud Desktop Client` application.

## Attachments
- Nextcloud_Desktop_Client_Cross-Site_Scripting__1.png
