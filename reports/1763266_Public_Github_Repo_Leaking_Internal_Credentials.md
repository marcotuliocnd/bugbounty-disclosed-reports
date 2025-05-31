# Public Github Repo Leaking Internal Credentials 

## Report Details
- **Report ID**: 1763266
- **URL**: https://hackerone.com/reports/1763266
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-11-05T19:16:51.906Z
- **Disclosed**: 2022-11-07T23:45:12.278Z

## Reporter
- **Username**: xinfohuggerx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
## Summary:
In Github I found some credentials to use in a mesos.apache.org 
Github:
https://github.com/Yelp/Tron/blob/master/yelp_package/itest_dockerfiles/mesos/mesos-secrets
https://github.com/Yelp/Tron/blob/master/yelp_package/itest_dockerfiles/mesos/mesos-slave-secret

## POC ss

{F2021070}
{F2021071}

Login documentation https://mesos.apache.org
https://mesos.apache.org/documentation/latest/authentication/

## Impact

Unauthorized account access  /information disclosure

## Attachments
- Screenshot_2022-11-06-00-32-06-00_40deb401b9ffe8e1df2f1cc5ba480b12.jpg
- Screenshot_2022-11-06-00-32-11-29_40deb401b9ffe8e1df2f1cc5ba480b12.jpg
