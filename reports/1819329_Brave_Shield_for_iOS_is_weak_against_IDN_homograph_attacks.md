# Brave Shield for iOS is weak against IDN homograph attacks

## Report Details
- **Report ID**: 1819329
- **URL**: https://hackerone.com/reports/1819329
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-12-31T07:51:20.106Z
- **Disclosed**: 2023-06-22T05:50:27.405Z

## Reporter
- **Username**: nishimunea
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

In most parts of Brave for iOS, including the address bar, protection against IDN attacks are implemented.
However, Brave Shield has no countermeasures.
For example, when you visit https://www.xn--80ak6aa92e.com , Brave Shield panel in the address bar shows the domain of this site is "apple.com".
This may lead users to be deceived into believing that the site is legitimate.

## Products affected: 

 * Brave for iOS (Version 1.45.2)

## Steps To Reproduce:

 * Visit https://www.xn--80ak6aa92e.com
 * Open Brave Shield panel from the address bar
 * "apple.com" is shown in the panel

## Supporting Material/References:

  * See the screenshot I attached.

## Impact

This may lead users to be deceived into believing that the site is legitimate.

## Attachments
- brave_shield_idn_homographic_attack.png
