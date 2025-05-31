# No Rate Limit On Reset Password

## Report Details
- **Report ID**: 1166066
- **URL**: https://hackerone.com/reports/1166066
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-04-15T22:20:15.437Z
- **Disclosed**: 2021-08-31T15:23:46.314Z

## Reporter
- **Username**: scorpion_0a0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upchieve

## Vulnerability Information
welcome all :
i found that no rate limit in reset password in ::: ==https://app.upchieve.org/resetpassword==

Summary:
No rate limit check on forgot password which can lead to mass mailing and spamming of users and possible employees
A little bit about Rate Limit:
A rate limiting algorithm is used to check if the user session (or IP-address) has to be limited based on the information in the session cache.


Steps To Reproduce The Issue
1- create account and go to reset password 
2- intercept burp and send request to intruder 
3- make payload and start attack 

attchaments ::

please follow me in this vedio ::
{F1267144}

similar reports ::::

1-https://hackerone.com/reports/751604
2-https://hackerone.com/reports/441161
3- https://hackerone.com/reports/280534


Suggested fix
Use CAPTCHA verification if many request sent.

## Impact

1- Attacker could use this vulnerability to bomb out the email inbox of the victim.
2- Attacker could send Spear-Phishing to the selected mail address.

## Attachments
- ratelimte.mp4
