# The email API to reset password is unlimited and can be used as a email bomb

## Report Details
- **Report ID**: 222080
- **URL**: https://hackerone.com/reports/222080
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-19T07:58:27.332Z
- **Disclosed**: 2017-04-20T15:34:21.403Z

## Reporter
- **Username**: xifengweiyu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
**Description:**

The email API `https://demo.nextcloud.com/qazxsw/lostpassword/email` to reset password is unlimited and can be used as a email bomb

**Reproduce steps:**

1.Every `Instant trial`'s link is `https://demo.nextcloud.com/yourname`,and it always has a default user `admin`

2.then I try to visit one `https://demo.nextcloud.com/qazxsw/login?user=admin`,then I try to login it using `username:admin || password:xxxxx`(password can be any wrong password)  .see screenshot(1)

3.Then nextcloud will prompt you to reset password,if you click it,admin's email box will receive an email.see screenshot(2)

4.So I can use chrome console network panel to `replay XHR` continuously,then my email box receive many email.see screenshot(3)

**How to harm other people:**

1.visit any project which you don't own,for example `https://demo.nextcloud.com/test`
2.If this people has set email address for his `admin`,then you can try the above reproduce steps.

## Attachments
- 2.png
- 3.png
- 1.png
