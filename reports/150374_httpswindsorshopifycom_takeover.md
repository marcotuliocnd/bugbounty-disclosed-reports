# https://windsor.shopify.com/ takeover

## Report Details
- **Report ID**: 150374
- **URL**: https://hackerone.com/reports/150374
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-10T16:32:35.797Z
- **Disclosed**: 2016-07-18T23:36:07.183Z

## Reporter
- **Username**: zseano
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi Shopify,

So I was doing some scanning for another client and saw a ton of *.shopify.com appear and thought to myself "Huh? I thought shopify.com hosted shops on myshopify.com.. weird, lets check this out".

An example is this: http://khanbot.shopify.com/password - as you can see it's a store opening soon, but it's on *.shopify.com. However when I try my own store: http://imjusttesting8.shopify.com/password then it will give me the generic, "Did you mean etc etc". Very weird. I tried looking around and playing as much as possible, but I wasn't unable to actually get a *.shopify.com url. (If this is actually possible could you let me know how?)

I found these via this BTW: https://crt.sh/?q=%25.shopify.com (there's quite a few more).

One that caught my eye was windsor.shopify.com. It's set to auto redirect to another domain (aislingofwindsor.com) which had actually expired. I purchased it and now when you visit windsor.shopify.com your redirected to a site I control. (yay for owning a shopify.com sub domain)

PoC: https://windsor.shopify.com/ (can even use https to make it even more 'trustworthy')

An attack idea would be saying to users "New product released by shopify! Increase your sales by using Windsor. Read more: https://windsor.shopify.com" (users will see shopify.com and trust. Plus the fact it's a cool name like 'Windsor', may get users attention). 

We could then in theory create a domain similar to shopify and redirect aislingofwindsor.com straight to another domain. Add all the HTTPS stuff to make it look even more real, and we have a pretty good attack surface!

Note: I've done a lot of internal phishing for clients and had a 100% success rate every time, hence why i'm reporting this as I feel this url could be used to easily phish users.


## Attachments
No attachments
