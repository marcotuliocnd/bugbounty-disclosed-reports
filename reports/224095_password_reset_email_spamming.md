# password reset email spamming

## Report Details
- **Report ID**: 224095
- **URL**: https://hackerone.com/reports/224095
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-26T16:30:09.856Z
- **Disclosed**: 2017-05-17T06:46:44.939Z

## Reporter
- **Username**: xifengweiyu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owncloud

## Vulnerability Information
**Description:**

The email API `https://yoursite/index.php/login?user=admin` to reset password is unlimited and can be used as a email bomb

vuln address:`https://yoursite/index.php/lostpassword/email`

**Reproduce steps:(use demo.owncloud.org as example)**

1.`https://demo.owncloud.org/index.php/login` has a default user `admin`

2.then I try to visit `https://demo.owncloud.org/index.php/login`,then I try to login it using `username:admin || password:xxxxx`(password can be any wrong passwords)

3.Then owncloud will prompt you to reset password,if you click it,admin's email box will receive an email.

4.So I can use chrome console network panel to `replay XHR` continuously,then `admin's email box` receive many email.

## Attachments
- Screen_Shot_2017-04-27_at_12.26.14_AM.png
