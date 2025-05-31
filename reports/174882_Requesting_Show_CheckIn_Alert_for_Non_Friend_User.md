# Requesting Show CheckIn Alert for Non Friend User

## Report Details
- **Report ID**: 174882
- **URL**: https://hackerone.com/reports/174882
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-10T05:54:19.898Z
- **Disclosed**: 2016-10-27T18:42:09.172Z

## Reporter
- **Username**: vinesh1989
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
During analysis it was observed that I was able to request "ShowCheck In Alert" Request for non friend user.

I performed this application from Mobile application. Below are the steps we have to carry to achieve this:

Logged in to Yelp Mobile Application
Visit any added friend and click on "ShowCheck In Alert" 
It will originate the request from the mobile application. Capture this request and Change the UserID value with any other user non-added friend value. Server sends response with OK message.

Please find attached POC for the same.


## Attachments
- Step_1.png
- Requesting_CheckIn_For_Non_Friend_User.png
- Step_2.png
- Step_3.png
