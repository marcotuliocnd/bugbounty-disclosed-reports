# Stored XSS on app.crowdsignal.com + your-subdomain.survey.fm via Embed Media

## Report Details
- **Report ID**: 920005
- **URL**: https://hackerone.com/reports/920005
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-09T18:51:17.320Z
- **Disclosed**: 2020-11-18T14:20:06.021Z

## Reporter
- **Username**: ali
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hello there,
I found a stored xss vulnerability.

Steps:
1. Go to `https://app.crowdsignal.com/dashboard`
2. Create a quiz.
3. Go to `https://app.crowdsignal.com/quizzes/{your-quiz-id}/question`
4. Add `Multiple Choice`
5. Put a name to answer 1.
6. Click Add media button.

{F901543}
7. Select Embed Media
8. Paste this:  `[wpvideo w0MiG12E]`
9. Insert it.
10. Open `Burp Suite` and click `Save` button.
11. Return to burp suite and paste this payload to `media[23168664]` parameter: `[wpvideo%20w0MiG12Exx1\"><svg/onload=prompt(document.domain)>]`
12. Forward the request and refresh the page. You will see xss alert.

Also go to `https://app.crowdsignal.com/sharing/quiz/{your-quiz-id}/` and copy survey.fm link. Go to it and you will see xss alert.

## Impact

Stealing cookies

Regards,
@mygf

## Attachments
- 1.png
