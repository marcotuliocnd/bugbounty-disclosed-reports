# Possible SSRF in email server settings(SMTP mode)

## Report Details
- **Report ID**: 222667
- **URL**: https://hackerone.com/reports/222667
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-21T04:40:14.878Z
- **Disclosed**: 2017-05-15T14:28:12.484Z

## Reporter
- **Username**: xifengweiyu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Description:
vul address `https://demo.nextcloud.com/xxx/settings/admin/additional`,when you change `smtp server address` ,you will get some different hints.

Reproduce steps:

1.Go to `https://demo.nextcloud.com/xxx/settings/admin/additional`,choose `SMTP` mode

2.Set server address to "172.17.1.0`,then you will get screenshot(nextcloud1.png),it means not on the same network segment

3.Set server address to "172.17.0.0`,then you will get screenshot(nextcloud2.png),it means the address not exists or doesn't open any port to access

4.Set server address to "172.17.0.1` and port to empty,then the test email will send successfully!
it means this host exists and opens a smtp port

5.Set server address to "172.17.0.1` and port to `22`,then you will get screenshot(nextcloud3.png),it means the address exists,but can not access to the port


## Attachments
- nextcloud1.png
- nextcloud2.png
- nextcloud3.png
