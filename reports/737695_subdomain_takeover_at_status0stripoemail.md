# subdomain takeover at status0.stripo.email

## Report Details
- **Report ID**: 737695
- **URL**: https://hackerone.com/reports/737695
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-11-14T19:57:06.931Z
- **Disclosed**: 2019-12-23T09:03:35.899Z

## Reporter
- **Username**: haxorpunk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
Hi ,

The subdomain status0.stripo.email was pointed at uptimerobot.com
whereas it was not being used , but having Cname record as stats.uptimerobot.com .
Hence anyone can takeover it.

I have parked it with atest account on uptimerobot.com

{F634639}

{F634636}

thanks

## Impact

Anyone can use this subdomain on uptimerobot.com with a false message.

## Attachments
- sub.bmp
- cname.bmp
