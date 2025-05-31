# Subdomain Takeover Via unclaimed Heroku Instance tim-exclusive.shopify.com

## Report Details
- **Report ID**: 424669
- **URL**: https://hackerone.com/reports/424669
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-10-16T15:32:20.195Z
- **Disclosed**: 2021-02-24T01:59:51.189Z

## Reporter
- **Username**: todayisnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Good day, I truly hope it treats you great on your side of the screen :)

I have found that your website tim-exclusive.shopify.com is pointed via a cname to an unclaimed Heroku Instance

This was not registered on Heroku.

I was able to take over the domain:

See my POC (Pug of Concept)
http://tim-exclusive.shopify.com/

POC Video:
https://www.dropbox.com/s/0p6dqz3rwbx2wxn/Screenshot%202018-10-16%2011.30.52.png?dl=0

Options How to fix:

1) Remove the Cname record on tim-exclusive.shopify.com to not point to Heroku

2) Ask me to remove my registered tim-exclusive.shopify.com on Heroku, and you can re register yours :)

May you be well on your side of the screen :)

-Eric

## Impact

control over domain :)

## Attachments
No attachments
