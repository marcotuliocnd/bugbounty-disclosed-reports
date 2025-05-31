# Shopify GitHub Login and Password exposed all private source code might be available.

## Report Details
- **Report ID**: 124100
- **URL**: https://hackerone.com/reports/124100
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-03-17T21:00:21.865Z
- **Disclosed**: 2017-06-08T21:11:07.953Z

## Reporter
- **Username**: todayisnew
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Sello (com.shopify.Sello)
https://itunes.apple.com/us/app/sello/id947038847?mt=8

ios Mobile Application

Versions 1.0.1, 1.1, 1.1.2, 1.1.3, 1.2, 

Podfile left inside application exposes GitHub Password for Shopify.

username: shopify-dep
password: 1910c92631a81a4c41dafbf96d537e3f24506b11


Impact: Access to all source code of all programs Shopify makes, which would not be good :)

source of file:


source "https://github.com/CocoaPods/Specs.git"
platform :ios, "8.0"

# ignore all warnings from all pods
inhibit_all_warnings!

target "Sello" do
  pod "SHPShareKit", git: "https://shopify-dep:1910c92631a81a4c41dafbf96d537e3f24506b11@github.com/Shopify/ios-share-kit"
  pod "HockeySDK"
  pod "Reachability", "~> 3.2"
  pod "PureLayout", "~> 2.0.6"
  pod "pop", "~> 1.0"
  pod "Intercom"
  pod "GoogleAnalytics"
  pod "Mixpanel"
  pod "Branch"
end

target "SelloTests", exclusive: true do
  pod "OCMock", "3.1.2"
end



Sello Also Exposes a series of other private credentials.


ApnsApplication:SELLO_IOS
branch_key:key_live_cgmRq1Cqi0GTaTZt6ugtkghaCwjEkH8N
FacebookAppID:825102250879029
FacebookDisplayName:Sello
GoogleAnalyticsID:UA-49226624-4
GooglePlusClientID:833666260708-pd79q7hfldjboqnsdkjep0c09lbusg8s.apps.googleusercontent.com
HockeyAppID:e220ee56ef6c7c0f9313dec065ab14d4
IntercomApiKey:ios_sdk-6c8980b1b197f9a4b741d8a99ea30eeb5eb7447c
IntercomAppID:ztfy5avc
MixpanelToken:b076cfff7bf5a6b04bb332efb07d339e
MixpanelTokenDev:d2c21feef224fbb03b48e1e1acc3d0f5
ShopifyAppHost:https://app.shopify.com/


Please let me know how I can help with more details, good luck on your side of the screen :)

-Eric

## Attachments
No attachments
