# SPF Misconfiguration

## Report Details
- **Report ID**: 280408
- **URL**: https://hackerone.com/reports/280408
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-10-19T12:40:13.474Z
- **Disclosed**: 2017-11-06T09:03:07.410Z

## Reporter
- **Username**: mr_r3boot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
I am just looking at your SPF records then found following. SPF Records missing safe check which can allow me to send mail on behalf of infogram.

#PoC:
The TXT records found for your domain are:
```
"v=spf1 include:_spf.google.com include:spf.mandrillapp.com include:mailgun.org ~all"
```
Simply anyone can use ```https://emkei.cz/``` service to trigger mail to anyone on behalf of infogram.
#Fix:

```v=spf1 include:_spf.google.com include:spf.mandrillapp.com include:mailgun.org -all```

>#*If team don't wanna hear about spf related checks please let me know. i'll close this report myself.*

Regards,
Mr.R3boot.

## Attachments
- spf.png
