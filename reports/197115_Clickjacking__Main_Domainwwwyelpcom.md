# Clickjacking @ Main Domain[www.yelp.com]

## Report Details
- **Report ID**: 197115
- **URL**: https://hackerone.com/reports/197115
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-01-10T05:27:45.082Z
- **Disclosed**: 2017-11-09T20:07:07.317Z

## Reporter
- **Username**: h4ck3r0ne
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
Hello Yelp Security Team, 

I Just want to submit a report Clickjacking on your Main Domain,
I Know that this is a Low Risk But may i know if your aware of it. 

PoC:
See Atachments.

Impact:

For example, imagine an attacker who builds a web site that has a button on it that says "click here for a free iPod". However, on top of that web page, the attacker has loaded an iframe with your mail account, and lined up exactly the "delete all messages" button directly on top of the "free iPod" button. The victim tries to click on the "free iPod" button but instead actually clicked on the invisible "delete all messages" button. In essence, the attacker has "hijacked" the user's click, hence the name "Clickjacking".

One of the most notorious examples of Clickjacking was an attack against the Adobe Flash plugin settings page. By loading this page into an invisible iframe, an attacker could trick a user into altering the security settings of Flash, giving permission for any Flash animation to utilize the computer's microphone and camera.

Clickjacking also made the news in the form of a Twitter worm. This clickjacking attack convinced users to click on a button which caused them to re-tweet the location of the malicious page, and propagated massively.

There have also been clickjacking attacks abusing Facebook's "Like" functionality. Attackers can trick logged-in Facebook users to arbitrarily like fan pages, links, groups, etc.

Request: if you think the reported issues have acceptable risk and you are not going to make changes then kindly request to mark as Informative or let me close it.

## Attachments
- yelp_clickjacking.png
- clickjack.html
