# Insecure Local Data Storage  : Application stores data using a binary sqlite database

## Report Details
- **Report ID**: 57918
- **URL**: https://hackerone.com/reports/57918
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-04-23T18:13:42.951Z
- **Disclosed**: 2017-03-03T14:20:31.819Z

## Reporter
- **Username**: bugwrangler
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: whisper

## Vulnerability Information
Android provides several options for developers to save persistent application data. The local DB should store data depending on whether the data should be private to your application or accessible to other applications and users. In any case, sensible data always have to be encrypted to avoid privacy violation. Linkedin App keeps user data  in  a  SQLite  database

 w.db

OWASP:  Insecure Storage

OWASP:  Insecure Data Storage


## Attachments
- SQLite_-_PlainText.png
