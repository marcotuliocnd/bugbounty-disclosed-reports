# Default Nextcloud allows http federated shares

## Report Details
- **Report ID**: 1183302
- **URL**: https://hackerone.com/reports/1183302
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-03T21:13:30.101Z
- **Disclosed**: 2021-05-11T11:38:49.919Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
1. userA on serverA runs on http only
2. userA sends a federated share to userB on serverB
3. userB is a normal user so he has no clue that there is no secure transport used and accepts the share
4. all the data written to and read from is now no longer protected by TLS

## Impact

While maybe a bit far fetched. But this would allow for man in the middle attacks. Nextcloud just seems to allow plain http communication by default.
It is in my opinion not sensible at all to expect end users to know the difference here.

I propose:

1. Allow only https by default (certificates are easy and cheap these days)
2. If it is for local debugging then only allow http when debugging
3. If really needed for some edge case make this explicit opt in in config.php

## Attachments
No attachments
