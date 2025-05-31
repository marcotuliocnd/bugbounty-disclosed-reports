# Can link to websites from profile

## Report Details
- **Report ID**: 275245
- **URL**: https://hackerone.com/reports/275245
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-10-06T21:32:10.914Z
- **Disclosed**: 2017-10-07T18:24:44.033Z

## Reporter
- **Username**: flex0geek
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
when I input a website to my profile it creates tag link:
<code><a href="http://test.org" rel="nofollow me">test.org</a></code>
this is a flaw, how? if the owner of the profile and a malicious link it is possible to redirect the user to a phishing page of wakatime.

Here's the scenario of this attack:

1) Attacker put a malicious link on his profile.
2) Once the victim clicks the link, it will be redirected to the malicious link but the malicious link has a malicious code inside that makes an action that it should do something to referral(where it came from before redirection) then the referral is wakatime. Using the malicious code, the malicious code will refresh the wakatime site to a fake wakatime site that will ask for sign in details like that.

you can fix it with:
<a href="http://google.com" rel="noreferrer">google.com</a>

Setting this on user provided links provides protection against this kind of attack. The cost of this solution is that the referring site won't show up as a referrer in analytics on the referred sites.

Thanks.

## Attachments
No attachments
