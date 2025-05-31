# Broken Authentication - Security token gets captured via man in the middle attack

## Report Details
- **Report ID**: 206650
- **URL**: https://hackerone.com/reports/206650
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-02-15T15:12:23.399Z
- **Disclosed**: 2019-06-22T14:15:50.376Z

## Reporter
- **Username**: saurabhb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
**Product / URL**

`http://en.instagram-brand.com/register/reset/<the security token here>?email=<email address here>`


**Description and Impact**

The password reset links issues by Instagram Brand gets delivered to users inbox with a http scheme and NOT https scheme.

This causes an attacker stealing those links and performing mass account takeovers and security compromises.

The link that gets delivered in inbox is:
`http://mandrillapp.com/track/click/30956340/instagram-brand.com?p=<the very long security token here>`

On requesting the above link in browser, it sends back the password reset token in clear text: `http://en.instagram-brand.com/register/reset/<the security token here>?email=<the email of user here>`

**Solution:**
This issues has a very easy solution. I have myself performed this and it worked !!.
Whenever the code responsible for sending password reset link makes those links, just add https as scheme instead of http. And you will observe that now all the accounts are safe and data cannot be stolen.


**Reproduction Instructions / Proof of Concept**

1. Request for you password reset link.
2. Go to inbox.
3. Right click that link and paste it on notepad and observe the scheme.
4. You can also start Wireshark to capture the traffic and observe that security token can be compromised.

I have attached the screenshot of Wireshark as a proof of concept. F161119

## Attachments
- InstagramBrandMITM.png
- InstagramBrandMITM.pcapng
