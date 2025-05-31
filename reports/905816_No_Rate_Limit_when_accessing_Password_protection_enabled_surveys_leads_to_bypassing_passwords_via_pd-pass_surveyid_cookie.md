# No Rate Limit when accessing "Password protection" enabled surveys leads to bypassing passwords via "pd-pass_surveyid" cookie

## Report Details
- **Report ID**: 905816
- **URL**: https://hackerone.com/reports/905816
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-06-23T04:36:24.923Z
- **Disclosed**: 2020-11-18T14:23:45.121Z

## Reporter
- **Username**: bugra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hi team,
If you write the right password on any password protected survey, you will see this request :
{F878934}

This request is protected with rate limit, that's great. But if you look to response, you will see a cookie. The password protection feature is cookie-based system.
In my survey, if you write the right password, system will set this cookie : `pd-pass_DA0C46C4EAECF2BA=81dc9bdb52d04dc20036dbd8313ed055`
And basically this is `pd-pass_SURVEYID=md5(password)`, it encrypts the right password with MD5 and if you visit the survey page with this cookie, you can see the survey.
So, I tried to brute force this cookie with Burp Suite's `Payload Processing` feature. (it encrypts your value with any hash type). And it worked, there is no rate limit when directly accessing to the survey page with password cookie.

Actually, I didn't any way to find the survey IDs. But when you go to a survey without password protection, the survey ID will be inside the source code. And if you enable the password protection after that, the survey ID won't be changed.
So, attacker can save the survey ID before the survey creator enable the password protection feature.

Also, the  `WordPress.com Shortcode` on `Sharing` page leaks the survey ID too. (but I don't know how it works, maybe this code turns to iframe etc. whne you paste it to any wordpress.com website)
{F878946}

## Steps To Reproduce:

  1. Go to your survey's `Sharing` page and copy the  survey ID from `WordPress.com Shortcode` 
  1. Turn on intercept on Burp Suite and go to your password protected survey.
  1. And send the GET request to Intruder
  1. Add `pd-pass_YOURSURVEYIDHERE=test` to cookie and set payload position to `test` value.
  1. Now go to `Payloads` tab on Intruder and set the `Payload Processing` feature like that :
       {F878947}
  1. Set the payload type to `Brute forcer` and you can change the other options like threads etc.
  1. Start the attack.

You can watch the video :
{F878959}

Probably, this issue works on quizzes too, I didn't test it.

## Impact

Bypassing the password protected surveys with brute force

## Attachments
- request.PNG
- surveyid.PNG
- payloadprocessing.PNG
- crowdsignalpoc.mp4
