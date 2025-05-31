# No Rate Limit  On Add new word

## Report Details
- **Report ID**: 479021
- **URL**: https://hackerone.com/reports/479021
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-13T22:57:47.318Z
- **Disclosed**: 2019-01-14T19:24:41.313Z

## Reporter
- **Username**: elmahdi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
####Hello I found in that there is no limit in the place of adding a new word which allows the attacker to add an infinite number of words which may cause a problem in the site and the server

####Steps To Reproduce : 
##### 1. Go To https://hosted.weblate.org/dictionaries/andors-trail/en/#add And Fill in fields
##### 2.Click On Add
##### 3.And interceptThe Request With Proxy ( Burp )
##### 4.And Send The Request To Inturder
##### 5.And Go to Payloads and Select In The Payload type > Numbers ...
##### 6.Click On Start Attack

####POC : 
{F405705}
{F405706}

## Impact

#####An attacker could cause a problem for the server

## Attachments
- Capture.PNG
- Capture.PNG
