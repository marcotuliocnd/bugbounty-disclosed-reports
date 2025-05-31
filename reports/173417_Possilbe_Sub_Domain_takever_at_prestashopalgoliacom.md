# Possilbe Sub Domain takever at prestashop.algolia.com

## Report Details
- **Report ID**: 173417
- **URL**: https://hackerone.com/reports/173417
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-10-01T20:06:49.357Z
- **Disclosed**: 2016-11-04T18:58:06.298Z

## Reporter
- **Username**: punkrock
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: algolia

## Vulnerability Information
Hey Sir

It looks like `prestashop.algolia.com` has a A record pointing to `178.62.8.144`

But when you visit `prestashop.algolia.com` you see a page hosted by "BC WebSolution" and I couldn't find any relation with Algolia

Now what's suspicious here is http://178.62.8.144/ also serves the content of  "BC WebSolution"

Maybe the IP is in no more control of Algolia and has been allocated someone else while the DNS record at Algolia.com still point to the old IP

If I am correct any vulnerability like XSS, File upload affecting the IP can be used in scope of `prestashop.algolia.com`

## Attachments
No attachments
