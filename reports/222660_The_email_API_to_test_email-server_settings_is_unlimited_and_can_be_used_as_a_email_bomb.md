# The email API to test email-server settings is unlimited and can be used as a email bomb

## Report Details
- **Report ID**: 222660
- **URL**: https://hackerone.com/reports/222660
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-21T03:43:39.047Z
- **Disclosed**: 2017-04-24T16:36:20.147Z

## Reporter
- **Username**: xifengweiyu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
**Description:**

The email-server settings test function in  `https://demo.nextcloud.com/xxx/settings/admin/additional` is unlimited and can be used as a email bomb.

And the test email API  is `https://demo.nextcloud.com/xxx/settings/admin/mailtest`

**Reproduce steps:**

1.Go to `https://demo.nextcloud.com/xxx/settings/personal` ,set your personal address to a email address which you want to attack .see screenshot(1)

2.Then go to `https://demo.nextcloud.com/xxx/settings/admin/additional`,`send test mail` ,then above email address will receive an test email.

3.So I can use chrome console network panel to `replay XHR` continuously,then my email box receive many email.see screenshot(2)



## Attachments
- 2.png
- 1.png
