# HTML injection in https://interviewing.shopify.com/index.php?candidate=

## Report Details
- **Report ID**: 601192
- **URL**: https://hackerone.com/reports/601192
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-06-05T20:40:02.405Z
- **Disclosed**: 2019-07-04T17:23:00.874Z

## Reporter
- **Username**: pklfpklf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
`https://interviewing.shopify.com/index.php?candidate=` is inserting the value of `candidate` into the DOM without any filtering (except that the equal sign can't appear in the payload), this allows attacker to injection any html in the DOM. Of course reflected XSS payloads like `<script>[...something...]</script>` will be blocked by browsers' protection, but we can still play with CSS injection:

`https://interviewing.shopify.com/index.php?candidate=z%3Cstyle%3E%20*%20{%20background:%20url(https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png);%20}`

{F503108}

## Impact

HTML injection, mostly CSS injection.

## Attachments
- css.png
