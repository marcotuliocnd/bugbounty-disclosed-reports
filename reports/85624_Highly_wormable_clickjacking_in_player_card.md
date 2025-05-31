# Highly wormable clickjacking in player card

## Report Details
- **Report ID**: 85624
- **URL**: https://hackerone.com/reports/85624
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-08-30T06:43:37.878Z
- **Disclosed**: 2018-05-17T23:11:28.495Z

## Reporter
- **Username**: filedescriptor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi,
I would like to report an issue where player card is vulnerable to clickjacking in certain browsers. This may result in something similar to XSS worm and many other critical damages.

##Details
Twitter Player Card allows a website to embed a custom player(html) into an iframe in a tweet. There are currently 2-3 security features in place to defend clickjacking on Twitter:
1. ```X-Frame-Options: SAMEORIGIN``` covering the whole twitter.com domain
2. ```Content-Security-Policy: frame-ancestors 'self'``` ditto
3. JS-based frame-buster in some pages (but not all)

For (1), SAMEORIGIN only checks if the embedded frame is on the same origin of the top window. For example, attacker can do something like twitter.com -> attacker.com -> twitter.com to evade it. More details can been seen from here: https://bugzilla.mozilla.org/show_bug.cgi?id=725490 
For (2), this is the only way to correctly prevent framing from other websites (it performs the check against the ancestor list). However this is a CSP2 directive so not all browsers support it. For example, Safari and IE do not support it.
For (3), using the sandbox attribute of iframe can disable JS of a frame, hence anti-frame-buster

Since Player Card is shown on a Tweet (on twitter.com), attacker can embed an iframe which embeds a Twitter page so that attacker can overlay it with "bait" content to lure victims to click on it.

The impact is huge because of the following facts:
* The card displays directly on the user's timeline, making the attack less suspicious to normal clickjacking
* The click is very subtle that victims cannot notice what's happened behind the scene
* Wormable because attacker can make victims tweet arbitrary content to spread it
* Can perform click-based critical actions, like follow, retweet, favorite... etc
* If sent as promoted tweet, it can target even more victims, also player is directly expanded

##Repo step
1. Clone the Player Card started bundle here: https://github.com/twitterdev/cards
2. Change the card's property *twitter:player* to a custom HTML file
3. In the HTML file, embed iframe to a Twitter page, e.g. ```<iframe src="//twitter.com"></iframe>```
4. Post the link in a Tweet (make sure the domain is white-listed)
5. Expand the tweet in Safari or IE, it will show that a Twitter page is embedded

Documentation of Player Card: https://dev.twitter.com/cards/types/player

##PoC

https://twitter.com/AttackerCanvas/status/637859735501279232 (**Open with Safari or IE**)

Video demo: https://vimeo.com/137725491 (password: click)

The PoC demonstrates how the attack can be conducted. There will be a fake video to lure victims to click to play it. After clicking the victim will automatically post a tweet with content "Pwn3d!".

## Attachments
No attachments
