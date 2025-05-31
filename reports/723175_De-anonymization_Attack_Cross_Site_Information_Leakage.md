# De-anonymization Attack: Cross Site Information Leakage

## Report Details
- **Report ID**: 723175
- **URL**: https://hackerone.com/reports/723175
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-26T09:18:27.896Z
- **Disclosed**: 2019-12-14T07:57:42.259Z

## Reporter
- **Username**: soheil_k
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: imgur

## Vulnerability Information
Dear Imgur Security Team,

We are researchers at the IMDEA Software Institute in Madrid, Spain. We have been working on analyzing Cross-Site Browser Leaks (xsleaks) and building a tool for finding instances of it on target web sites. Recently we tested imgur.com and discovered a flaw that can affect Imgur users. We would like to responsibly disclose it and support you to mitigate the issue. The details follow.

## Attack Overview:
Events-Fired xsLeak: a cross-domain attack website, say attacker.org, could embed specific resources from imgur.com in a script Tag, and check if an error or load event is triggered in one state but not in the other. 
Based on which events are triggered for each vulnerable resource, the attacker can infer the victim state (e.g. logged in vs logged out, or owner of a specific profile). This happens because the leaky endpoint return a 2xx HTTP response in one state but a 4xx in the other.

In particular, we have found 2 vulnerable (leaky) endpoints:

1. The first one can be used for login detection (onerror =  logged out, onload = logged in):https://api.imgur.com/3/larynx/history?IMGURPLATFORM=web&IMGURUIDJAFO=9d77969d8b3a7a6ac6cb78943c96e48cd0bd74e02b29839f9f19aea827429db6&SESSIONCOUNT=3&client_id=546c25a59c58ad7

2.  The second one can be used to track and deanonymize the owner of a Imgur profile across origins. For this, the attacker leverages the resource: https://<USERNAME>.imgur.com/all  where <USERNAME> is the username of  the victim to be fingerprinted (e.g., https://user1imdea.imgur.com/all). 
If the victim visiting the attack page is the owner of the <USERNAME> profile, the "onload" event will be triggered. Otherwise, the "onerror" event is fired.

## How to reproduce the attack:
a. We have attached a PoC attack page.
b. Acting as the victim, login to imgur.com from a browser and load the attached page in a different tab of the same browser.c. Specify the profile/home page url of format:  https://<USERNAME>.imgur.com/all  for the target victim in the input field, and press the submit button.
c. After a couple of seconds, popups should appear saying whether you are logged at imgur and if you are the owner of the specified account.


## Browser/OS tested: 
We tested the PoC on windows 10 in:  Chrome Version: 77.0.3865.120 (Official Build) (64-bit) and Firefox 67.0.3  (Official Build) (64-bit). The same attack should work on other browsers and OSes too, although we haven't verified it thoroughly!

## Similarity with known attacks:
Similar attacks were reported in the past against Facebook (https://www.imperva.com/blog/facebook-privacy-bug/) and Twitter (https://hackerone.com/reports/329957) and the vendors have taken the necessary preventive measures.

For any further questions, we are available at your disposal.

## Impact

## Impact of the attack
The attack enables malicious web sites of the internet to uniquely determine if any of their visitors is logged at Imgur, and also to track and fingerprint Imgur users across origins who have shared particular images. 

## Attachments
- imgur_attack_page.html
