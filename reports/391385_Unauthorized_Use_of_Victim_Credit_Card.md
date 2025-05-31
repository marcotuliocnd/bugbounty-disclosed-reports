# Unauthorized Use of Victim Credit Card

## Report Details
- **Report ID**: 391385
- **URL**: https://hackerone.com/reports/391385
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-08-07T17:02:13.729Z
- **Disclosed**: 2020-08-21T20:20:16.663Z

## Reporter
- **Username**: hk755a
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
#SUMMARY
Yelp user's credit cards are at risk of being compromised
There's a way by which a malicious attacker can make unauthorized purchases from the victim's credit card.
Just by getting the victim to some external website and clicking on it, the victim would have eventually paid for some unwanted deal unknowingly from his saved credit card on yelp. (Please see the POC which shows a $450 deal)

#DESCRIPTION:
The endpoint yelp.com/checkout/deal/****?biz_id={}&fsid={} is Framable, which means a sample deal page like this:
https://www.yelp.com/checkout/deal/16OJ1G_Ev7STx0HELIDzyA?biz_id=Ydf5dgFsGhMSP61Ht7TekA&return_url=%2Fbiz%2Fbutcher-and-the-burger-chicago
Could be embedded as an hidden iframe on some HTML page. 
Watch the video attached to see how the exploit really looks like.


#EXPLOIT SCENARIOS:
*The attacker could simply host the exploit page (attached to this report) on some webpage and use social networking sites to share it across the world. One simple way could be spreading it through Yelp's Talk section itself, so as to get valid yelp users easily.* 

I mainly envision the vulnerability to be exploited in the following ways:
==**1.) Attacker creates a deal himself and uses this vulnerability to steal money from the victim.**==
==**2.) Attacker just goes on causing monetary loss for the victim, with no personal monetary gain.**==

#POC
*You may want to watch the 1 min video attached with the report*

Step 1.) Log into your yelp account on your fresh or incognito browser window.

Step 2.) Open the attached "Yelp Credit Card Misuse by framable deals page" Webpage in another window.

Step 3.) Click on the slightly visible Purchase button. 

The vulnerability's exploitation impact is high as it causes unauthorized credit card use of the victim!
Do let me know if there are any questions.

## Impact

Yelp users credit card protection is certainly compromised. Worthy customer's bear monetary losses.  
Apart from money the faith of users on yelp for their card's security is also lost leading to customer/business loss to yelp.
Such attacks running in the wild, are heavy threat to an organization's reputation.

## Attachments
- Yelp_Credit_Card_Misuse_by_framable_deals_page.html
- Credit_card_Compromise.mp4
