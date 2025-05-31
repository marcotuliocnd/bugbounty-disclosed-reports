# Mailgun misconfiguration 

## Report Details
- **Report ID**: 244474
- **URL**: https://hackerone.com/reports/244474
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-29T18:32:14.993Z
- **Disclosed**: 2017-07-01T21:39:45.915Z

## Reporter
- **Username**: hax0rgb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
During subdomain enumeration i found the following subdomain:
```
email.mailgun.wakatime.com
```
Looking at the cname records, it is pointing to mailgun.
```
host email.mailgun.wakatime.com
email.mailgun.wakatime.com is an alias for mailgun.org.
mailgun.org has address 34.225.110.231
mailgun.org has address 34.194.118.46
mailgun.org is an alias for mailgun.org.
mailgun.org has address 34.194.118.46
mailgun.org mail is handled by 10 mxb.mailgun.org.
mailgun.org mail is handled by 10 mxa.mailgun.org.
```
I went to my mailgun account and tried to claim email.mailgun.wakatime.com.
And success!

{F198701}

And i can now also create a mailing list.

{F198702}

It seems you have not added ``` email.mailgun.wakatime.com``` to your mailgun account.

Hence, it could be possible to snoop into the emails of wakatime.

I guess we need to add the dns records to verify the domain and it may take upto 48 hours for DNS changes to propagate
Hence, i have not gone further and decided to report this.
 


## Attachments
- Screen_Shot_2017-06-29_at_11.00.04_PM.png
- Screen_Shot_2017-06-29_at_11.06.49_PM.png
