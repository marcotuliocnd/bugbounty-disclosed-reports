# Production secret key leak in config/secrets.yml

## Report Details
- **Report ID**: 456997
- **URL**: https://hackerone.com/reports/456997
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-12-06T17:46:45.164Z
- **Disclosed**: 2019-01-08T07:55:23.269Z

## Reporter
- **Username**: phreak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grab

## Vulnerability Information
**Summary:** 
Production secret key leak in config/secrets.yml

**Description:** 
In Github, http://engineering.grab.com/ secret_key_base is leaked which is present in the config/secrets.yml

## Steps To Reproduce:

  1. Go to the below GitHub URL and we can verify that secret_key_base is present.
```
https://github.com/grab/blogs/blob/master/2017-01-29-deep-dive-into-database-timeouts-in-rails/config/secrets.yml
```

Mitigation:-
```
https://medium.com/@thejasonfile/hide-your-api-keys-hide-your-skype-api-keys-884427746f9c
```

## Impact

Proper Impact is explained here:-
https://stackoverflow.com/questions/44220691/rails-what-are-the-consequences-of-a-leaked-secret-key-base

## Attachments
- poc.png
