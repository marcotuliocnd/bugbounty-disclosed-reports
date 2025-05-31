# Cross-site scripting on api.collabs.shopify.com

## Report Details
- **Report ID**: 1672459
- **URL**: https://hackerone.com/reports/1672459
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-08-17T13:49:53.635Z
- **Disclosed**: 2022-10-13T18:12:46.766Z

## Reporter
- **Username**: kun_19
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
Shopify collabs (collabs.shopify.com) is a new platform for content creators / influencers to discover and advertise the millions of brands of Shopify. The content creators can apply for different brands on this platform and get paid (affiliate marketing).
I discovered a cross-site scripting vulnerability on this quite new domain. 

## Steps To Reproduce:

  1. Visit https://www.shopify.com/collabs/find-brands and click on "Apply for early access"
  2. Create a new Shopify ID / account
  3. You get redirected to https://collabs.shopify.com/onboarding:  
{F1871170}
  4. Connect your social media account to your profile (e.g. Instagram), edit your content, etc.
  5. You should now be successfully registered  (early bird access - waiting list):  
{F1871169}
  6. As you are logged in, open the URL `https://api.collabs.shopify.com/creator/auth/login?creator_redirect=javascript:alert(document.domain)` and you will see that the JavaScript has triggered:  
{F1871171}



## Supporting Material:
[list any additional material (e.g. screenshots, video, etc)]

  * [attachment / reference]

## Impact

* Execution of JavaScript code in the victim's browser => Execution of any future API functions of api.collabs.shopify.com in the name of the victim
* Exfiltration of confidential data
* etc.

## Attachments
- logged_in.png
- onboarding.png
- xss.png
