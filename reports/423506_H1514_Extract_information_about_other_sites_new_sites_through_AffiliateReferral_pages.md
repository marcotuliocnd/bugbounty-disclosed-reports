# H1514 Extract information about other sites (new sites) through Affiliate/Referral pages

## Report Details
- **Report ID**: 423506
- **URL**: https://hackerone.com/reports/423506
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-13T20:49:37.196Z
- **Disclosed**: 2019-11-04T18:26:55.685Z

## Reporter
- **Username**: rijalrojan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** 

This bug is based on a really interesting behavior that I noticed when testing the referral pages. More information on this is in the Description section.

**Description:**

Shopify provides its user base with `Shopify Affiliate` feature. This allows company/users to share their referral link and gain bonuses/commission if websites sign up with this. I noticed that this can be easily exploited to get mass information. 

Shopify referral links look like this:  https://shopify.com/?ref=nsa. After a user visits that page, a cookie is created with the name `source` and the value `nsa`. This helps to identify the referee. All this process is done through a GET request which makes the attack really easy. The only think an attacker now has to do is embed the link as an image on their page. Once that is done, a cookie will be set on victim's Shopify page. 

After that, at any time if the victim decides to sign up for Shopify, their store will be added as a referral store. Once the store is added as a referral store, the attacker can see the following information: Status of the store, information (name, email and phone number) as well as any events that happen on the store (store events). Additionally because the attacker is a referee, they also get the 200% bonus.

Initially, I thought this was hard to exploit but considering the fact that all you need to do is embed your referral link as an image to set the cookie, I don't think exploiting this will be hard. You can specifically use these attacks at locations that are more prone to use Shopify. For example, Shopify recently opened a space in LA that allows new and experienced Shopify store managers to come together and help each other. These places will likely have high number of registration. 

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. If you go https://api.securify.network/shopify.html and then register a Store, I should be able to see the store detail on my Referral page.

## Impact

DIsclosure of store events and store information.

## Attachments
No attachments
