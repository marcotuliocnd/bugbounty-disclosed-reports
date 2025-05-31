# Subdomain Takeover at http://gameday.websummit.net

## Report Details
- **Report ID**: 193056
- **URL**: https://hackerone.com/reports/193056
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2016-12-21T13:10:21.742Z
- **Disclosed**: 2017-01-30T12:54:53.006Z

## Reporter
- **Username**: filedeletor1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: websummit

## Vulnerability Information
As i said in the title i found a subdomain takeover vulnerability on the url http://gameday.websummit.net
The url was trying to find a bucket that didn't exist from a probably forgotten dns entry that was at
gameday.websummit.net.s3-website-eu-west-1.amazonaws.com

So i created a bucket with the specified name and uploaded a poc.
POC in the pictures

For more infos please ask...

## Attachments
- Screen_Shot_2016-12-21_at_2.42.48_PM.png
- Screen_Shot_2016-12-21_at_2.42.35_PM.png
- Screen_Shot_2016-12-21_at_2.48.22_PM.png
