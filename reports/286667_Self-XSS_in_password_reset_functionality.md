# Self-XSS in password reset functionality

## Report Details
- **Report ID**: 286667
- **URL**: https://hackerone.com/reports/286667
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-11-02T19:56:43.657Z
- **Disclosed**: 2017-11-10T14:26:02.755Z

## Reporter
- **Username**: zeesek
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,
When I opened this domain of yours,
https://accounts.shopify.com/password-reset/new

I just put the following text into email address box,
<h1 style="color:blue;">█████</h1>
it change the colour of the text.

Well my point here is that if you could inject HTML, you might be able to add a <form> tag
to the page.
I also upload the picture as a proof.

Peace.

## Attachments
No attachments
