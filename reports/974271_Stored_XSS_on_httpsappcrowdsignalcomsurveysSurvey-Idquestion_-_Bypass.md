# Stored XSS on https://app.crowdsignal.com/surveys/[Survey-Id]/question - Bypass

## Report Details
- **Report ID**: 974271
- **URL**: https://hackerone.com/reports/974271
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-09-03T18:53:46.589Z
- **Disclosed**: 2020-11-18T14:20:21.496Z

## Reporter
- **Username**: ali
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hello there,
I hope all is well!

I found a stored xss on https://app.crowdsignal.com/

Steps:
* Go to `https://app.crowdsignal.com/dashboard`
* Create a survey.
* Go to `https://app.crowdsignal.com/quizzes/{survey-id}/question`
* Add `Multiple Choice`
* Click `Add media` button.
* Select `Embed Media`
* Paste this: `[dailymotion id=x8oma9]`
* Insert it.
* Open Burp Suite and click `Save` button.
* Return to burp suite and paste xss payload to `media[11111111]` parameter: `[dailymotion id=x8oma9"><svg/onload=prompt(document.domain)>]`
* Forward the request and refresh the page. You will see xss alert.

This isn't self xss because I saw users who Team plan can invite other users to their dashboards. So attacker can steal victim's cookies.

Also I recorded a poc video for you:   
{F975177}

## Impact

Stealing cookies.

Best Regards,
@mygf

## Attachments
- bandicam_2020-09-03_21-49-20-444.mp4
