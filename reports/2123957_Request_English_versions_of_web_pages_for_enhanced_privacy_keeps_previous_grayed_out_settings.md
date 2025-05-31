# 'Request English versions of web pages for enhanced privacy' keeps previous (grayed out) settings 

## Report Details
- **Report ID**: 2123957
- **URL**: https://hackerone.com/reports/2123957
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2023-08-25T21:40:59.621Z
- **Disclosed**: 2023-09-13T08:36:02.806Z

## Reporter
- **Username**: andreien
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
## Summary:
Enabling 'Request English versions of web pages for enhanced privacy' in 'Choose your preferred language for displaying pages' continues to use the grayed out settings for JS and HTTP language preferences. This affects navigator.language, navigator.languages, but also Accept-Language.

## Steps To Reproduce:

  1. Change the list of languages in the browser preference 'Choose your preferred language for displaying pages', for example add a new language or reorder the list of languages.
  2. From the same menu, enable  'Request English versions of web pages for enhanced privacy'. This will gray out the reconfiguration in step 1.
  3. Verify if the setting in step 2 took place by checking navigator.language, navigator.languages and Accept-Language.

## Supporting Material/References:
Accept-Language: ab,en-US;q=0.7,en;q=0.3 is included HTTP Header output with the configuration attached.

## Impact

Users that have previously changed language settings (or language settings were changed by the browser previously, such as from a locale-specific installation) may make use of this setting expecting to improve their privacy when using Tor Browser. For example, users might find few websites dynamically change their language, or change their threat model. The settings they changed gray out, which gives confidence that they are overwritten.

However, an attacker can make use of both JavaScript fingerprinting (malicious scripts reading navigator.languages) and HTTP fingerprinting (malicious server reading Accept-Language) to identify users that have changed these settings. This affects users on a Strict security level (disabled JS) through the headers passed.

To resolve this, enabling the setting should enforce the language settings of an English default installation of Tor Browser globally, also maintaining the order of this configuration (that is, "en-US,en" and not "en,en-US"). Currently, I think the best workaround is to manually add, remove and reorder the language preferences or reset about:config's intl.accept_languages.

## Attachments
- img.png
