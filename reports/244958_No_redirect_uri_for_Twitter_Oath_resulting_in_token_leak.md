# No redirect uri for Twitter Oath resulting in token leak

## Report Details
- **Report ID**: 244958
- **URL**: https://hackerone.com/reports/244958
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-07-01T01:01:13.790Z
- **Disclosed**: 2017-07-03T08:22:40.325Z

## Reporter
- **Username**: b3nac
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Good afternoon,

There's an opportunity to steal Oath tokens upon the return uri in the following redirect.

https://wakatime.com/oauth/twitter/authorize?reason=tweet&next=/share/embeddable/5e22456d-9aae-4267-b1a9-4315c2605d89/0ed2e4de-f479-4e03-a8db-464a0696c08f.svg/tweet

If I change the &next= to my profile for example /@5e22456d-9aae-4267-b1a9-4315c2605d89

This results in an open redirect to my main profile leaking the Oauth token: 

#POC

https://wakatime.com/oauth/twitter/authorize?reason=tweet&next=/@5e22456d-9aae-4267-b1a9-4315c2605d89

results in F199105

Here's a video demonstrating the vulnerability. F199111

#Patch
Add a redirect uri that can't be tampered with.

#References

This is almost the exact same scenario that is in this report.
https://hackerone.com/reports/140432



## Attachments
- OauthTokenLeak.png
- 2017-06-30_17-57-29.flv
