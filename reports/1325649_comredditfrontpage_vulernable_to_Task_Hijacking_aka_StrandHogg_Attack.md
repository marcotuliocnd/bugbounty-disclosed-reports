# com.reddit.frontpage vulernable to Task Hijacking (aka StrandHogg Attack)

## Report Details
- **Report ID**: 1325649
- **URL**: https://hackerone.com/reports/1325649
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-08-31T11:32:38.715Z
- **Disclosed**: 2021-12-13T22:48:14.542Z

## Reporter
- **Username**: nexus2k
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
The app com.reddit.frontpage is vulnerable to Task Hijacking used by widespread Android trojans. Task hijacking allows malicious apps to inherit permissions of vulnerable apps and is usually used for phishing login credentials of victims.

## Impact:
Assuming a malicious actor want's to grab the login credentials of an app user they can hijack the main tasks by overriding the taskAffinity to the vulnerable android package. When the victim then tries to open the legitimate app the malicious app can inject their own activities and phish credentials of the victim.

## Steps To Reproduce:
  1. Victim installs malicious app
  1. Victim starts malicious app (could also be a background service)
  1. Victim opens legitimate app which the malicious app can intercept.

This does NOT require root nor any permissions in the malicious app.
To prevent this attack you will need to set taskAffinity property of the application activities to ""(empty string) in the <activity> tag of
the AndroidManifest.xml to force the activities to use a randomly generated task affinity, or set it at the <application> tag to enforce on all activities in the application.

This vulnerability applies to all Android Versions before Android 11.

## Supporting Material/References:
* https://promon.co/security-news/strandhogg/
* https://arstechnica.com/information-technology/2019/12/vulnerability-in-fully-patched-android-phones-under-active-attack-by-bank-thieves/
* Found by: https://ostorlab.co/ Mobile App scanner

## Impact

An attacker could phish the victims user credentials or get additional permissions in the name of the legitimate app which then again could be abused for eavesdropping etc.

## Attachments
- standhogg.apk
- Reddit-POC.webm
