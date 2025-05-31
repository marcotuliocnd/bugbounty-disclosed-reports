# Error page Text Injection.

## Report Details
- **Report ID**: 156196
- **URL**: https://hackerone.com/reports/156196
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-03T04:09:01.607Z
- **Disclosed**: 2016-08-25T14:17:42.313Z

## Reporter
- **Username**: akshay_raj
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
AS we can see in report an user or attacker is able to inject his text into error page and can trap to user to visit other site by adding following link /test/%2f../It%20has%20been%20changed%20by%20a%20new%20one%20https://www.malicious.com%20so%20go%20to%20the%20new%20one%20since%20this%20one

A text injection and a missconfiguration of the 404 page which can be used in phishing.

POC URL: blog.trello.com/test/%2f../It%20has%20been%20changed%20by%20a%20new%20one%20https:

URl:-https://www.phacility.com//test/%2f../It%20has%20been%20changed%20by%20a%20new%20one%20https://www.malicious.com%20so%20go%20to%20the%20new%20one%20since%20this%20one

## Attachments
- error.png
