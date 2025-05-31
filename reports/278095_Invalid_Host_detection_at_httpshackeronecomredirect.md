# Invalid Host detection at https://hackerone.com/redirect

## Report Details
- **Report ID**: 278095
- **URL**: https://hackerone.com/reports/278095
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-10-17T04:35:07.837Z
- **Disclosed**: 2017-12-03T19:19:50.707Z

## Reporter
- **Username**: shailesh4594
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello,99

**Summary:** Host detection at https://hackerone.com/redirect is invalid and insecure.

**Description :** On redirection page, host is detected and highlighted to prevent phishing attacks. But that protection is weak and can be bypassed. So an attacker can redirect victim on another host instead of highlighted host. Also, it possible to redirect victim on a IDN homograph website.

Host filtration can be bypassed using whitespace characters like `%0D`,`%0A`,`%00`,`%09` etc.

### Steps To Reproduce

1. Use this markdown code `[Go to yelp.com](https://yelp.com%0A.evil.com%5C@x)` in a comment 
2. Click on `Go to yelp.com` link.
3. External link warning page will be shown 
4. `yelp.com` will be highlighted as targeted Host.
5. Click on Proceed button.
6. You will be redirected on https://yelp.com.evi.com (a subdomain of evil.com)
7. Done

####Using IDN homograph : 

1. Try `[Yelp.com](https://yelp.com%0A.уelp.com%5C@x)`
2. Click on `Yelp.com` 
3. `yelp.com` will be highlighted
4. You will be redirected on https://yelp.com.xn--elp-cfd.com/@x after clicking on **Proceed** button
5. Done

Thanks,
Shailesh

## Attachments
No attachments
