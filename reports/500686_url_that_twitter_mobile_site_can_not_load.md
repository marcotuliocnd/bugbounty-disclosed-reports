# url that twitter mobile site can not load

## Report Details
- **Report ID**: 500686
- **URL**: https://hackerone.com/reports/500686
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-02-25T09:22:42.338Z
- **Disclosed**: 2019-03-19T21:44:36.317Z

## Reporter
- **Username**: seifelsallamy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** 
A url that twitter mobile site can not load, crushes any page containing this url

**Description:** 
Invalid hex characters crushes twitter mobile site as example go to ```https://mobile.twitter.com/?%xx``` 
twitter won't load.

1) Sending such url on a direct message, twitter will no longer be able to load the conversation,
F429765
2) Tweet such url, anyone following you won't be able to load any tweets
F429766

I think Twitter on the client side trying to find a value for %xx which is not possible so it raises an error

## Steps To Reproduce:

  1. Go to https://mobile.twitter.com/
  2. Send or tweet this url ```https://mobile.twitter.com/?%xx```
  3. You and your followers won't be able to see any tweets on the mobile site

## Impact

This issue works only on https://mobile.twitter.com/
(not working on IOS, Android and https://twitter.com/ )
however, all twitter mobile users with no twitter app should be affected

## Attachments
- tw1.png
- tw2.png
