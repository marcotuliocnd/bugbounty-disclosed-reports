# [www.stripo.email] There is no rate limit for contact-us endpoints

## Report Details
- **Report ID**: 856305
- **URL**: https://hackerone.com/reports/856305
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-04-22T14:04:06.679Z
- **Disclosed**: 2020-05-26T10:35:33.513Z

## Reporter
- **Username**: what_web
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
###Summary
The speed limit for the *https://stripo.email/es/contact-us* endpoint has not been implemented.

###Steps To Reproduce
1. Go to the *https://stripo.email/es/contact-us*
2. Turn on blocking and fill out the contact form
3. Send request to Intruder.
4. Set your payloads and start attack.
5. There is no rate-limit.

###Proof of Concept
{F799307}

###Fix
Implement 429 status code for too many requests.

## Impact

There is no rate limit for submitting an inquiry form.

## Attachments
- _____.PNG
