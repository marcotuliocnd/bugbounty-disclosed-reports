# Password token validation in https://demo.weblate.org/

## Report Details
- **Report ID**: 229987
- **URL**: https://hackerone.com/reports/229987
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-05-19T20:01:42.397Z
- **Disclosed**: 2017-06-27T15:10:22.144Z

## Reporter
- **Username**: brdoors3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information

Hi team,

I noticed that when requesting multiple reset links at https://demo.weblate.org/ all tokens are valid and can be used.

In numerous applications the following policy is adopted as an additional security measure:

- keep valid only that token with shorter lifetime (last requested)

or

- invalidate all reset links generated after successful use of one of these tokens

Please check it.

## Attachments
No attachments
