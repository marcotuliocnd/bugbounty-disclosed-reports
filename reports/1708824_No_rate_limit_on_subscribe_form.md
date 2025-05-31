# No rate limit on subscribe form 

## Report Details
- **Report ID**: 1708824
- **URL**: https://hackerone.com/reports/1708824
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-09-22T13:10:37.052Z
- **Disclosed**: 2022-10-05T20:55:39.542Z

## Reporter
- **Username**: happykira0x1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
## Summary:
Hi team, I found that you missing a rate limit protection for subscribe form 

## Platform(s) Affected:
https://business.yelp.com/?source=consumer_site_header&utm_content=header&utm_medium=www&utm_source=cons_home

## Steps To Reproduce:


  1. go to https://business.yelp.com/?source=consumer_site_header&utm_content=header&utm_medium=www&utm_source=cons_home
  1. find a form with just email input (emailsub.png)
  1. fill it with email click on submit then intercept the request 
  1.  send to burp intruder  go to  -> positions
  1. clear `§`
  1. add `§` in email like `youremail§1§@gmail.com`
  1. go to -> payloads,  add numbers type paylaod like ( from : 2 , to : 100, step: 1)
  1. start attack you will see all response with 200 ok and contain msg `Thanks for subscribing!` so no rate limit implemented

##Fix:
add a recaptcha or 429 error (many requests)
## Supporting Material/References:
see screenshots

## Impact

No rate limit in form.

## Attachments
- Capture_d__cran_(31).png
