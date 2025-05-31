# Reflective Cross-site Scripting via Newsletter Form

## Report Details
- **Report ID**: 709336
- **URL**: https://hackerone.com/reports/709336
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-10-08T02:36:01.197Z
- **Disclosed**: 2019-10-11T17:38:59.054Z

## Reporter
- **Username**: dostoevskylabs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
*.myshopify.com is vulnerable to a reflective cross-site scripting attack in the newsletter form. This can be crafted to trigger on a page load without any further user interaction.

The following example url shows this vulnerability:
```
https://testbuguser.myshopify.com/?contact[email]%20onfocus%3djavascript:alert(%27xss%27)%20autofocus%20a=a&form_type[a]aaa
```

This was tested on a newly registered store "testbuguser.myshopify.com"

If you require any additional details, please do not hesitate to bump.

## Impact

This attack could be leveraged to compromise administrative sessions or perform actions on behalf of users with the same level of privilege as the user.

## Attachments
- proof.png
