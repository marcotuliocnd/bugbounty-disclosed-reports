# Firebase Firestore insecure database

## Report Details
- **Report ID**: 731724
- **URL**: https://hackerone.com/reports/731724
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-11-07T20:16:05.642Z
- **Disclosed**: 2020-02-13T16:57:23.340Z

## Reporter
- **Username**: emmano
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mobisystems_ltd

## Vulnerability Information
## Summary:
The app is exposing a firebase database url that has no read/write protections.

## Steps To Reproduce:
  1. Decompile the Android app
  2. Do a string search for `firebase_database`
  3. Use the project name (i.e. `msdict-dev`) in combination with the Firestore REST API to modify the database.

## Supporting Material/References:
Via decompilation an attacker can get the project name for a Firebase database. Then they can use the Firestore REST API to modify the DB.
I was able to add a new document to the DB with the following script.

`curl  https://firestore.googleapis.com/v1/projects/msdict-dev/databases/%28default%29/documents/test   -H 'Content-Type: application/json'   -d '{ "fields": { "title": { "stringValue": "TEST" }} }'`

to view the document that was added just visit:

`https://firestore.googleapis.com/v1/projects/msdict-dev/databases/%28default%29/documents/test`

## Impact

An attacker has access to an insecure database.

## Attachments
No attachments
