# Limited Open redirection using SSO-SAML

## Report Details
- **Report ID**: 178345
- **URL**: https://hackerone.com/reports/178345
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-27T06:44:35.351Z
- **Disclosed**: 2017-03-26T08:34:22.061Z

## Reporter
- **Username**: shailesh4594
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello,

**Endpoint:** https://hackerone.com/users//saml/sign_in?email=teste@snapchat.com&remember_me=true

Recently, you have patched an open redirection issue which was reported as #171398. 
I found a bypass of that patch. 

**Steps to reproduce:** 
1. Add following in comment/report : 
```https://hackerone.com/users//saml/sign_in?email=teste@snapchat.com&remember_me=true``` 
2. Click on link. 
3. You will redirected on SSO URL without going through **External Link Warning** page. 
4. Done.

PoC  : 
https://hackerone.com/users/saml/sign_in?email=teste@snapchat.com&remember_me=true (Through external warning page)
https://hackerone.com/users//saml/sign_in?email=teste@snapchat.com&remember_me=true (Without external warning page)

**Suggested Fix:** Use more stronger regular expression and filtration at this endpoint.

Best regards,
Shailesh


## Attachments
No attachments
