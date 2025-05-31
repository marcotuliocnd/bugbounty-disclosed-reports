# SSLv3 Poodle Attack on Ip Of semrush

## Report Details
- **Report ID**: 318594
- **URL**: https://hackerone.com/reports/318594
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-02-22T16:43:36.402Z
- **Disclosed**: 2018-03-13T14:31:05.938Z

## Reporter
- **Username**: apapedulimu-
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
**Summary:** 
POODLE SSLv3 bug on multiple servers

**Description:** 
 CVE-2014-3566: The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and other products, uses nondeterministic CBC padding, which makes it easier for man-in-the-middle attackers to obtain cleartext data via a padding-oracle attack, aka the "POODLE" issue.

## Steps To Reproduce:

1. Create .txt file include this ip : ( 54.230.149.17 & 54.230.149.158 ) ex: ip.txt
2. nmap -sV --version-light -Pn --script ssl-poodle -p 443 -iL ip.txt

## Supporting Material/References:

```
root@jancok:~# nmap -sV --version-light -Pn --script ssl-poodle -p 443 -iL ip.txt

Starting Nmap 7.25BETA1 ( https://nmap.org ) at 2018-02-22 23:40 EST
Nmap scan report for server-54-230-149-17.sin2.r.cloudfront.net (54.230.149.17)
Host is up (0.029s latency).
PORT    STATE SERVICE    VERSION
443/tcp open  ssl/https?
| ssl-poodle: 
|   VULNERABLE:
|   SSL POODLE information leak
|     State: LIKELY VULNERABLE
|     IDs:  OSVDB:113251  CVE:CVE-2014-3566
|           The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and
|           other products, uses nondeterministic CBC padding, which makes it easier
|           for man-in-the-middle attackers to obtain cleartext data via a
|           padding-oracle attack, aka the "POODLE" issue.
|     Disclosure date: 2014-10-14
|     Check results:
|       TLS_RSA_WITH_AES_128_CBC_SHA
|       TLS_FALLBACK_SCSV properly implemented
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-3566
|       https://www.imperialviolet.org/2014/10/14/poodle.html
|       https://www.openssl.org/~bodo/ssl-poodle.pdf
|_      http://osvdb.org/113251
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port443-TCP:V=7.25BETA1%T=SSL%I=2%D=2/22%Time=5A8F9B45%P=x86_64-pc-linu
SF:x-gnu%r(GetRequest,36B,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nServer:\x
SF:20CloudFront\r\nDate:\x20Thu,\x2022\x20Feb\x202018\x2016:40:40\x20GMT\r
SF:\nContent-Type:\x20text/html\r\nContent-Length:\x20551\r\nConnection:\x
SF:20close\r\nX-Cache:\x20Error\x20from\x20cloudfront\r\nVia:\x201\.1\x209
SF:f6b01a312a31ea74b95b305e8d62497\.cloudfront\.net\x20\(CloudFront\)\r\nX
SF:-Amz-Cf-Id:\x20wTZjtVmAWgTRJcBZoY1eKmML1MIGDjqyL8HHIbcopGOT3RptvM0oAw==
SF:\r\n\r\n<!DOCTYPE\x20HTML\x20PUBLIC\x20\"-//W3C//DTD\x20HTML\x204\.01\x
SF:20Transitional//EN\"\x20\"http://www\.w3\.org/TR/html4/loose\.dtd\">\n<
SF:HTML><HEAD><META\x20HTTP-EQUIV=\"Content-Type\"\x20CONTENT=\"text/html;
SF:\x20charset=iso-8859-1\">\n<TITLE>ERROR:\x20The\x20request\x20could\x20
SF:not\x20be\x20satisfied</TITLE>\n</HEAD><BODY>\n<H1>ERROR</H1>\n<H2>The\
SF:x20request\x20could\x20not\x20be\x20satisfied\.</H2>\n<HR\x20noshade\x2
SF:0size=\"1px\">\nBad\x20request\.\n<BR\x20clear=\"all\">\n<HR\x20noshade
SF:\x20size=\"1px\">\n<PRE>\nGenerated\x20by\x20cloudfront\x20\(CloudFront
SF:\)\nRequest\x20ID:\x20wTZjtVmAWgTRJcBZoY1eKmML1MIGDjqyL8HHIbcopGOT3Rptv
SF:M0oAw==\n</PRE>\n<ADDRESS>\n</ADDRESS>\n</BODY></HTML>")%r(HTTPOptions,
SF:36B,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nServer:\x20CloudFront\r\nDat
SF:e:\x20Thu,\x2022\x20Feb\x202018\x2016:40:40\x20GMT\r\nContent-Type:\x20
SF:text/html\r\nContent-Length:\x20551\r\nConnection:\x20close\r\nX-Cache:
SF:\x20Error\x20from\x20cloudfront\r\nVia:\x201\.1\x20c811a11df2d0d24d49e3
SF:cdf48257de21\.cloudfront\.net\x20\(CloudFront\)\r\nX-Amz-Cf-Id:\x20dUUs
SF:gtWLhorBbOSJMk6AESCL5MYIhEXtXdoSrTQ5pa0vKwxzKOa_0Q==\r\n\r\n<!DOCTYPE\x
SF:20HTML\x20PUBLIC\x20\"-//W3C//DTD\x20HTML\x204\.01\x20Transitional//EN\
SF:"\x20\"http://www\.w3\.org/TR/html4/loose\.dtd\">\n<HTML><HEAD><META\x2
SF:0HTTP-EQUIV=\"Content-Type\"\x20CONTENT=\"text/html;\x20charset=iso-885
SF:9-1\">\n<TITLE>ERROR:\x20The\x20request\x20could\x20not\x20be\x20satisf
SF:ied</TITLE>\n</HEAD><BODY>\n<H1>ERROR</H1>\n<H2>The\x20request\x20could
SF:\x20not\x20be\x20satisfied\.</H2>\n<HR\x20noshade\x20size=\"1px\">\nBad
SF:\x20request\.\n<BR\x20clear=\"all\">\n<HR\x20noshade\x20size=\"1px\">\n
SF:<PRE>\nGenerated\x20by\x20cloudfront\x20\(CloudFront\)\nRequest\x20ID:\
SF:x20dUUsgtWLhorBbOSJMk6AESCL5MYIhEXtXdoSrTQ5pa0vKwxzKOa_0Q==\n</PRE>\n<A
SF:DDRESS>\n</ADDRESS>\n</BODY></HTML>");

Nmap scan report for server-54-230-149-158.sin2.r.cloudfront.net (54.230.149.158)
Host is up (0.028s latency).
PORT    STATE SERVICE    VERSION
443/tcp open  ssl/https?
| ssl-poodle: 
|   VULNERABLE:
|   SSL POODLE information leak
|     State: LIKELY VULNERABLE
|     IDs:  OSVDB:113251  CVE:CVE-2014-3566
|           The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and
|           other products, uses nondeterministic CBC padding, which makes it easier
|           for man-in-the-middle attackers to obtain cleartext data via a
|           padding-oracle attack, aka the "POODLE" issue.
|     Disclosure date: 2014-10-14
|     Check results:
|       TLS_RSA_WITH_AES_128_CBC_SHA
|       TLS_FALLBACK_SCSV properly implemented
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-3566
|       https://www.imperialviolet.org/2014/10/14/poodle.html
|       https://www.openssl.org/~bodo/ssl-poodle.pdf
|_      http://osvdb.org/113251
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port443-TCP:V=7.25BETA1%T=SSL%I=2%D=2/22%Time=5A8F9B45%P=x86_64-pc-linu
SF:x-gnu%r(GetRequest,36B,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nServer:\x
SF:20CloudFront\r\nDate:\x20Thu,\x2022\x20Feb\x202018\x2016:40:40\x20GMT\r
SF:\nContent-Type:\x20text/html\r\nContent-Length:\x20551\r\nConnection:\x
SF:20close\r\nX-Cache:\x20Error\x20from\x20cloudfront\r\nVia:\x201\.1\x209
SF:80b603eea89acb9f5bc806e2efdf82c\.cloudfront\.net\x20\(CloudFront\)\r\nX
SF:-Amz-Cf-Id:\x200GA88OFJqyG4qDARfjyQ1jGVyWfzjEnIf0PKUOQI1r6-AuHswKbacw==
SF:\r\n\r\n<!DOCTYPE\x20HTML\x20PUBLIC\x20\"-//W3C//DTD\x20HTML\x204\.01\x
SF:20Transitional//EN\"\x20\"http://www\.w3\.org/TR/html4/loose\.dtd\">\n<
SF:HTML><HEAD><META\x20HTTP-EQUIV=\"Content-Type\"\x20CONTENT=\"text/html;
SF:\x20charset=iso-8859-1\">\n<TITLE>ERROR:\x20The\x20request\x20could\x20
SF:not\x20be\x20satisfied</TITLE>\n</HEAD><BODY>\n<H1>ERROR</H1>\n<H2>The\
SF:x20request\x20could\x20not\x20be\x20satisfied\.</H2>\n<HR\x20noshade\x2
SF:0size=\"1px\">\nBad\x20request\.\n<BR\x20clear=\"all\">\n<HR\x20noshade
SF:\x20size=\"1px\">\n<PRE>\nGenerated\x20by\x20cloudfront\x20\(CloudFront
SF:\)\nRequest\x20ID:\x200GA88OFJqyG4qDARfjyQ1jGVyWfzjEnIf0PKUOQI1r6-AuHsw
SF:Kbacw==\n</PRE>\n<ADDRESS>\n</ADDRESS>\n</BODY></HTML>")%r(HTTPOptions,
SF:36B,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nServer:\x20CloudFront\r\nDat
SF:e:\x20Thu,\x2022\x20Feb\x202018\x2016:40:40\x20GMT\r\nContent-Type:\x20
SF:text/html\r\nContent-Length:\x20551\r\nConnection:\x20close\r\nX-Cache:
SF:\x20Error\x20from\x20cloudfront\r\nVia:\x201\.1\x20e14935429e8b5cfb258b
SF:503fe0233feb\.cloudfront\.net\x20\(CloudFront\)\r\nX-Amz-Cf-Id:\x20s4YG
SF:LwviLFSBvGk8WD5Z0N2LIqbeVPqlxi2Y6JXysX-6zPgTxSvnSg==\r\n\r\n<!DOCTYPE\x
SF:20HTML\x20PUBLIC\x20\"-//W3C//DTD\x20HTML\x204\.01\x20Transitional//EN\
SF:"\x20\"http://www\.w3\.org/TR/html4/loose\.dtd\">\n<HTML><HEAD><META\x2
SF:0HTTP-EQUIV=\"Content-Type\"\x20CONTENT=\"text/html;\x20charset=iso-885
SF:9-1\">\n<TITLE>ERROR:\x20The\x20request\x20could\x20not\x20be\x20satisf
SF:ied</TITLE>\n</HEAD><BODY>\n<H1>ERROR</H1>\n<H2>The\x20request\x20could
SF:\x20not\x20be\x20satisfied\.</H2>\n<HR\x20noshade\x20size=\"1px\">\nBad
SF:\x20request\.\n<BR\x20clear=\"all\">\n<HR\x20noshade\x20size=\"1px\">\n
SF:<PRE>\nGenerated\x20by\x20cloudfront\x20\(CloudFront\)\nRequest\x20ID:\
SF:x20s4YGLwviLFSBvGk8WD5Z0N2LIqbeVPqlxi2Y6JXysX-6zPgTxSvnSg==\n</PRE>\n<A
SF:DDRESS>\n</ADDRESS>\n</BODY></HTML>");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 2 IP addresses (2 hosts up) scanned in 27.51 seconds

```

## Impact

its vulnerable  CVE-2014-3566

## Attachments
No attachments
