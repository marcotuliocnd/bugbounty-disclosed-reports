# Brave Android: Incorrect URL Eliding in Brave Shields Pop Up

## Report Details
- **Report ID**: 2501378
- **URL**: https://hackerone.com/reports/2501378
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-05-11T15:07:49.358Z
- **Disclosed**: 2024-09-18T16:10:44.455Z

## Reporter
- **Username**: jayateerthag
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:
Reference: https://chromium.googlesource.com/chromium/src/+/HEAD/docs/security/url_display_guidelines/url_display_guidelines.md#simplify

Urls should be elided from front when displaying anywhere in the user interface as per standard security guidelines for most browsers in order to avoid url spoofing or confusing users with actual domain name, when long domain/subdomain is used.
The desktop version(Windows) of Brave is working properly and url is elided correctly, while in android it's not. (Refer POC images for reference)


## Products affected: 

Brave for Android: 1.62.165 Chromium: M121

## Steps To Reproduce:
1. Open https://long-extended-subdomain-name-containing-many-letters-and-dashes.badssl.com/ in Brave Browser (Android)
2. Click on the Brave Icon in the URL Bar/Omnibox to enable/disable Brave Shield for the website
3. Notice that in the Brave shield UI which appears, the long subdomain is not elided from front properly in android which might lead to URL Confusion to the users.
4. Although I have reported for Brave Shields only I suspect that this might affect in places like Brave Rewards too where URL might not be properly elided. (I am currently unable to test this feature as I am located in India which does not support Uphold Wallet integration)
Incorrect URL Eliding in Brave Rewards UI might be very severe vulnerability as users might get confused when donating BAT tokens to website. [I request Brave team to test point 4 & fix if vulnerable in the same ticket]

Note: As android is affected, IOS might also be affected, Kindly check & fix the same in all Mobile OS

## Supporting Material/References:

https://chromium.googlesource.com/chromium/src/+/HEAD/docs/security/url_display_guidelines/url_display_guidelines.md#simplify

## Impact

URL confusion/spoof when user want to enable/disable Brave shields in Android

## Attachments
- URLElideVulnerabilityAndroid.jpg
- Screenshot_(41).png
