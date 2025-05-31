# Stored XSS in www.learnboost.com via ZIP codes.

## Report Details
- **Report ID**: 300812
- **URL**: https://hackerone.com/reports/300812
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-12-27T15:32:34.344Z
- **Disclosed**: 2018-04-22T20:55:04.376Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
# Summary
---

www.learnboost.com is vulnerable to stored XSS via ZIP codes stored alongside school names in the *Network* panel. 

# Browsers Verified In
---

* Mozilla Firefox 58.0b12 (64-bit)

# PoC
---

Visit https://www.learnboost.com/settings/network/search and search for `fro`. My entry will trigger the XSS payload.

```html
"><img src=x onerror=alert(document.domain)>
```

{F249746}

## Impact

I now have stored XSS that triggers whenever someone searches for `fro`. If I were to map the payload to a very common search term (e.g. `aa`) that would increase the likelihood that my payload would fire.

## Attachments
- Screenshot_from_2017-12-27_16-30-22.png
