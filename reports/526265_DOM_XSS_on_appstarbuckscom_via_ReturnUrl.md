# DOM XSS on app.starbucks.com via ReturnUrl

## Report Details
- **Report ID**: 526265
- **URL**: https://hackerone.com/reports/526265
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-04-04T09:06:56.688Z
- **Disclosed**: 2020-03-17T21:18:33.965Z

## Reporter
- **Username**: gamer7112
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
**Summary:** XSS Can be achieved via the ReturnUrl when signing in on app.starbucks.com

**Platform(s) Affected:** app.starbucks.com

## Steps To Reproduce:
1. Visit https://app.starbucks.com/account/signin?ReturnUrl=%09Jav%09ascript:alert(document.domain)
2. Sign in

## Supporting Material/References:
{F461364}


## How can the system be exploited with this bug? 
XSS could be used to steal the account of any victim that signs in via the url.
  

## How did you come across this bug ?
Retesting report #438240


## Recommendations for fix
Improve the checks on ReturnUrl such as not allowing hex characters 00-1F

## Impact

As with any xss, it could be used to steal the cookies of the victim to gain access to their account.

## Attachments
- starbucks_xss.png
