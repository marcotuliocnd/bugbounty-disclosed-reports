# Link obfuscation bug

## Report Details
- **Report ID**: 669440
- **URL**: https://hackerone.com/reports/669440
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-08-08T02:43:11.226Z
- **Disclosed**: 2019-08-12T17:20:24.212Z

## Reporter
- **Username**: l000g1c
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:
Link preview in the left bottom of Brave Browser will show the link where the user will be redirected after clicking it, but after clicking the link, the affected user will be redirected to other website.

## Products affected: 
Latest Version of Brave browser

## Steps To Reproduce:
1. Open poc.html
2. Hover your mouse to a hyperlink named https://brave.com
3. You will see in the link preview in the bottom of the browser that the user should be redirected.
4. Click the hyperlink and you will be redirected to another domain.

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

The attacker can trick a user to go to an evil domain.

## Attachments
- Screen_Shot_2019-08-08_at_10.38.39_AM.png
- brave.html
