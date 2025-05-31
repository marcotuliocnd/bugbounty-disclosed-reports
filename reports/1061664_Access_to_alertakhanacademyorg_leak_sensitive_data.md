# Access to alerta.khanacademy.org leak sensitive data 

## Report Details
- **Report ID**: 1061664
- **URL**: https://hackerone.com/reports/1061664
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-18T15:05:33.301Z
- **Disclosed**: 2021-09-08T08:36:43.777Z

## Reporter
- **Username**: myominthu_sec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
Hi ,
I found to access https://alerta.khanacademy.org/ using signup bypass.That leak access to sensitive data of khanacademy.org

Step To Reproduce:

1. Go to https://alerta.khanacademy.org/#/signup
2. Inspect Q and remove ng-hide

{F1121291}

3. You got Signup Form. Signup account using anythings@khanacademy.org mail.

{F1121292}

4. When you successfully signup,You access alerta.khanacademy.org without confirm email.

{F1121297}

If you not login direct .
1. Go to alerta.khanacademy.org/#/login.
2. Inspect Q and remove ng-hide

{F1121293}

3. Login with your register info.

{F1121294}

## Impact

Attacker can access alerta dashboard

Thanks,
@nightmare_msf

## Attachments
- Screen_Shot_2020-12-18_at_21.28.31.png
- Screen_Shot_2020-12-18_at_21.28.45.png
- Screen_Shot_2020-12-18_at_21.32.39.png
- Screen_Shot_2020-12-18_at_21.32.49.png
- Screen_Shot_2020-12-18_at_21.24.56.png
