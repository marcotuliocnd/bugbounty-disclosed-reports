# AppLovin API Key hardcoded in a Github repo

## Report Details
- **Report ID**: 674774
- **URL**: https://hackerone.com/reports/674774
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-08-16T00:26:53.604Z
- **Disclosed**: 2019-09-18T22:01:53.543Z

## Reporter
- **Username**: hackbotone_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hello,
I found a Sensitive Data Exposure in github/mopub-android-mediation project, the AppLovin UI API key is hardcoded in source code. 

And in the comment it's mentioned that 
##"This is a unique SDK Key from AppLovin. Get yours from the AppLovin UI".

Github Link:- https://github.com/mopub/mopub-android-mediation/blob/72804166ec9f3b79cc0dcfa96bd8c813f3252794/Testing/src/main/AndroidManifest.xml#L60

Google Ads SDK reference link:- https://developers.google.com/admob/android/mediation/applovin

Thanks
Anshuman Pattnaik

## Impact

So if it's a production API key then it shouldn't be shown publicly in Github repo otherwise it can be used by other developers as it's a company property the API key should be secure as it's a monetize API key.

## Attachments
- APPLOVIN_API_KEY_SCREENSHOT.PNG
