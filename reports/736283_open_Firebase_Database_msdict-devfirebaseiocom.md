# open Firebase Database: msdict-dev.firebaseio.com

## Report Details
- **Report ID**: 736283
- **URL**: https://hackerone.com/reports/736283
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-11-12T15:49:57.190Z
- **Disclosed**: 2020-01-20T11:47:59.039Z

## Reporter
- **Username**: kickino
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mobisystems_ltd

## Vulnerability Information
## Summary:
publicly available Firebase Database (msdict-dev.firebaseio.com)

## Steps To Reproduce:
Version: `Oxford Dictionary of English Free_v11.1.511`
in `res/values/strings.xml`
```
<string name="firebase_database_url">https://msdict-dev.firebaseio.com</string>
```

Accessing your Firebase Database via https://msdict-dev.firebaseio.com/.json returns
`null` instead of the usual `{ "error" : "Permission denied" }`

## Supporting Material/References:

https://medium.com/@danangtriatmaja/firebase-database-takover-b7929bbb62e1 describes how a firebase database can be taken over with similar conditions.

## Impact

```The above application doesn’t need any acces_token to insert data to the firebase database it’s completely open and anybody can access it without any access credentials.```

There are guidelines available by Firebase to resolve the insecurities and misconfiguration, please follow this link:
https://firebase.google.com/docs/database/security/resolve-insecurities

## Attachments
No attachments
