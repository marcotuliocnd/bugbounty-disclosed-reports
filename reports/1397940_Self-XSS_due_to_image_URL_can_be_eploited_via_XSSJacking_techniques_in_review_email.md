# Self-XSS due to image URL can be eploited via XSSJacking techniques in review email

## Report Details
- **Report ID**: 1397940
- **URL**: https://hackerone.com/reports/1397940
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-11-11T03:06:12.331Z
- **Disclosed**: 2023-02-01T03:38:11.707Z

## Reporter
- **Username**: penguinshelp
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: judgeme

## Vulnerability Information
## Summary:
Good day team,

I found a self-xss due to the image url of recommendations in your reviewer profile that can be exploited via XSSJacking techniques. 

This one was honestly pretty tricky, since unlike the rest of the Judge.me App that whitelisted `*.myshopify.com` in the CSP this one has a set `X-Frame-Options: SAMEORIGIN` meaning unlike the rest of my XSS reports I can use my Shopify store's frontent. Luckily though I managed to find a place that allows me to load iframes, namely the full email preview of review requests.

## Steps To Reproduce:

  1. Login to your 'reviewer' account in Judge.me

  1. Add a new recommendation for your public profile: `https://judge.me/[ID]?subtab=recommendations&tab=public_profile` -> Add recommendation

  1. Go back to the recommendation list, click the pencil icon in the image and insert this payload to trigger the Self-XSS: `https://secure.gravatar.com/avatar/█████████.png?;'onload=alert(document.domain)>`

  1. Now to exploit this, login to your Shopify account and open the Judge.me app

  1. Click 'Request' -> 'Email Templates' and edit the existing email template

  1. In the 'text block', add a link and insert this payload as the display text and url (make sure to edit the ID to targeted reviewer's ID): `https://<iframe src="https://judge.me/[ID_OF_TARGET]?tab=public_profile">`
{F1510271}

  1. Click 'Save' two times. I'm honestly not sure why but it won't display properly unless you save it twice

  1. Now to send that template, create an order in your Shopify instance and make sure to fulfill that order: `yourshop.myshopify.com/admin/draft_orders/new` -> Mark as fulfilled. Make sure that the customer you use is the one from step 1 or the email of the reviewer account

  1.  Once that is done, go back to the Judge.me app and click 'Requests' -> 'Request Dashboard'

  1. Click 'Add manual request' -> 'Send Review Request for Old Orders'

  1. The reviewer account should receive an email notification regarding a review request, click 'Trouble viewing email' to access the full email preview

  1. In there you should see that the iframe for the reviewer account is visible, now all that is needed to be done is perform XSSJacking techniques to trigger the Self-XSS
{F1510279}

Note: Getting a valid review request that you can use for the preview is pretty confusing  since the 'send me an example' doesn't work for full email preview, it took me quite a while before I successfully managed to do it so if there's anything that I haven't explained properly please let me know or you can directly ask the Judge.me team for help :)

## Supporting Material/References:
{F1510278}

As usual, if there is anything that doesn't make any sense please let me know.

Cheers,
PenguinsHelp

## Impact

XSS via XSSJacking techniques

## Attachments
- InsertLink.JPG
- Judge.me_XSS.mp4
- EmailPreview.JPG
