# Tab nabbing via window.opener

## Report Details
- **Report ID**: 403891
- **URL**: https://hackerone.com/reports/403891
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-09-01T17:45:21.296Z
- **Disclosed**: 2018-09-01T20:04:50.115Z

## Reporter
- **Username**: logan47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Details:
When you open a link in a new tab ( target="_blank" ), the page that opens in a new tab can access the initial tab and change it's location using the window.opener property.

Attack scenario:
here i have provided 2 videos, in video 1 i have my editorial link set. to show that tabnapping is possible.which you can see in the video 1 .
in video 1 i have given my editorial in such a way that it will redirect me tothe malicious page which will redirect the original site to attackers site.[i am using localhost.]

In video 2nd i have shown that if a user is new and has not given his editorial link or he has not given the editorial link anyway, then in this case when he see any translation and click on the source link then he will be redirected to the attacker given link which inturn can be malicious . if it is then it will redirect the original tab to attacker site which can be used for phishing and also account takeove.
such as attacker makes a copy of your login page and when user redirects to his site he can easily display in his fake page that you session has been timedout please login again .

I hope you have  understanded  what i am trying to say.

## Impact

because the redirecting is made in the background, while the user is focused on another tab.
this Can be very dangerous if attacker is smart than he can trick the victim easily and can takeover his account easily through scam page and can also lead to several phishing attacks.

Websites that protect themselves against this kind of attack: google.com websites, twitter.com (they open links in new tabs, but the window.opener property is set to null)

Hope that all helps, let me know if you need more information

For more check:
https://hackerone.com/reports/23386
https://hackerone.com/reports/179568

## Attachments
- weblate.mp4
- weblate2.mp4
- tabnapping.html
