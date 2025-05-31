# Widespread failure of certificate validation in Android apps

## Report Details
- **Report ID**: 2293
- **URL**: https://hackerone.com/reports/2293
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2014-02-25T07:08:24.808Z
- **Disclosed**: 2019-11-12T23:47:52.177Z

## Reporter
- **Username**: secbro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I have identified approximately 75 Android applications (and some iPad) that fail to validate SSL certificates, either failing to validate valid certificate authorities, correct hostnames or both.

I have made attempts to responsibly disclose all of these vulns to the responsible parties. A few have been omitted from this list for various reasons.

Almost all of these could have lead to credit card and/or password disclosure.

Capital One Spark Pay 0.9.50
Authy 16.3 - fixed
Uber 2.7.13 - fixed
Outlook.com 7.8.2.12.49.2176
Kindle 4.3.0.67
US Bank 1.14.19
ADP Mobile 1.68
Piwik Mobile 1.9.6
Piwik Mobile 2 2.0.1
ClubLocal 1.4
SafeNetMobile Pass 8.3.4.5
TWC TV 3.4.4 #78
BestBuy 7.3.1
Bing 4.2.1.20140123
Walgreens 4.2
SouthWest 2.1.0
CNNMoney 1.01
StumbleUpon 3.2.4
SplashID 7.08 bld 734
Pocket 5.12
Kayako (unsure of version)
Hootsuite 2.5.4.34
Sylphone 5.3.3
Citizen's Bank Champaign Bank
Honeywell TC 2.0 2.2.0
OfficeDepot 2.3.1
Sears 6.1.8
NewEgg 3.2.3
OfficeDepot for Business "BSD" 1.4
Macy's 1.4.1
CostCo 1.5.2
Kmart 6.1.7
SonicWall Mobile Connect 2.0.11
Staples Advantage 1.1
Cisco Technical Support 3.5
Zappos ( iPad)
iTunes Connect (iPad)
Cisco WebEx 4.5.0 (current version)
Oracle Now app v.1.5.1
Lync 2010 4.0.6509.3001
Lync 2013 (v?)
Cisco OnPlus Mobile app 1.1.1001
CA DMV (current version)
Ask.com app v. 2.2.5
WordPress (current version)
GoDaddy v.3.3.2
WD My Cloud v. 3.1.1
Weibo 4.2.6
Huntington Mobile v. 1.6.21
Medscape 3.0.1
My Bluebird v. 2.1.0.0
Dominos
Pizza Hut
Citrix Receiver v. 3.4.13
Orbitz
Kayak Android v. 5.8
Solarwinds Mobile Admin v. 8.1.319643 
Western Union v. 4.2.5
Groupon v. 2.10.3166
Serve (American Express - Fixed)





## Attachments
No attachments
