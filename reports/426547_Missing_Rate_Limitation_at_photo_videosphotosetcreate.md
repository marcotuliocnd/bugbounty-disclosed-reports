# Missing Rate Limitation at /photo_videos/photoset/create

## Report Details
- **Report ID**: 426547
- **URL**: https://hackerone.com/reports/426547
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-10-21T20:00:27.961Z
- **Disclosed**: 2018-11-24T23:09:33.537Z

## Reporter
- **Username**: m00hdi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
Hello,I discovered that one is able to create an unlimited number of albums Via /photo_videos/photoset/create/
Steps To Reproduce:
1.Login And Go to http://fr.chaturbate.co /photo_videos/photoset/create/
2.Fill the form
3.Enable a proxy interception tool (e.g Burp Suite)
4.Click Save
5.Send the POST request made to /photo_videos/photoset/create to intruder
6.Set 500 or more custom inputs and Start attack

I've been able to create many albums without restrictions

Reference:
F364058

## Impact

Create an unlimited number of albums

## Attachments
- Sans_titre.JPG
