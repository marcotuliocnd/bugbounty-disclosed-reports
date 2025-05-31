# Insecure Storage and Overly Permissive  API Keys in Android App

## Report Details
- **Report ID**: 753868
- **URL**: https://hackerone.com/reports/753868
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-08T06:22:37.354Z
- **Disclosed**: 2020-04-12T18:32:21.784Z

## Reporter
- **Username**: ticzox
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zenly

## Vulnerability Information
#Description:
Most often Developers for their ease of use,leave API keys and some sensitive keys ,Tokens as hardcoded strings,which isn't really a good ideas as it can result in Leaks of sensitive information getting in Wrong Hands which indeed can results in Data theft and Tampering with how the application deals with the data, and API requests the application Makes.

==I found a bunch of API keys,Tokens.==

#To Check API keys leaks Sensitive Information or not
https://github.com/streaak/keyhacks

#Steps to reproduce.
1.Decomiple the app.
2.Look for sensitive information


#Proof of Concept:
Screenshots has been attached as a proof of concept.

## Impact

If an attacker decompiles your apk, and extracts your token, they can indeed maliciously send traffic on your behalf.
This is the case with pretty much every single one of the web  companies out there (google included).
The main thing to know however, is that it is rarely useful for people to do this. Polluting someone else's data  while possible, isn't exactly a profitable thing to do. You can also create server-side filters to help prevent this thing from happening.

## Attachments
No attachments
