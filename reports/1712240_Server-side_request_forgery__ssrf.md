# Server-side request forgery  (ssrf)

## Report Details
- **Report ID**: 1712240
- **URL**: https://hackerone.com/reports/1712240
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-09-26T10:01:39.113Z
- **Disclosed**: 2022-09-28T07:54:46.127Z

## Reporter
- **Username**: raja404
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
*.yelp-support.com

## Summary:

Server-side request forgery  
  
## Platform(s) Affected:

www.yelp-support.com

## Steps To Reproduce:
 
1. If you visit this site, attackers could try to steal information like your passwords, emails, or credit card details.

2. your  server has redirect to malicious website  

3. i am Referer: https://evil.com/    and  your don't  check  server properly the write website 

#Steps

 1 .  i am open  assetfinder  to subdomain enumeration on this domain : yelp-support.com

2. i am open in this subdomain in Burp suite :  www.yelp-support.com
 
3. my Browser Request: 

GET /static/111213/js/perf/stub.js HTTP/1.1
Host: www.yelp-support.com
Cookie: CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1
Sec-Ch-Ua: "Chromium";v="105", "Not)A;Brand";v="8"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Sec-Ch-Ua-Platform: "Linux"
Accept: */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: no-cors
Sec-Fetch-Dest: script
#Referer: https://evil.com/                           --------- i am  change this link ------ 
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Connection: close

4. and  your server Response:


HTTP/1.1 200 OK
Date: Mon, 26 Sep 2022 08:14:39 GMT
Content-Type: application/x-javascript
Connection: close
Strict-Transport-Security: max-age=63072000; includeSubDomains
Cache-Control: public,max-age=10368000
Expires: Tue, 24 Jan 2023 08:14:39 GMT
Last-Modified: Thu, 18 Dec 2014 19:28:42 GMT
Vary: Accept-Encoding
Server: sfdcedge
X-SFDC-Request-Id: 78779c5a3d8ac507638c3b6c783c3ce8
Content-Length: 1385

this["Perf"]&&void 0!==this["Perf"].enabled||(function(window){'use strict';var a={DEBUG:{name:"DEBUG",value:1},INTERNAL:{name:"INTERNAL",value:2},PRODUCTION:{name:"PRODUCTION",value:3},DISABLED:{name:"DISABLED",value:4}};
window.PerfConstants={PAGE_START_MARK:"PageStart",PERF_PAYLOAD_PARAM:"bulkPerf",MARK_NAME:"mark",MEASURE_NAME:"measure",MARK_START_TIME:"st",MARK_LAST_TIME:"lt",PAGE_NAME:"pn",ELAPSED_TIME:"et",REFERENCE_TIME:"rt",Perf_LOAD_DONE:"loadDone",STATS:{NAME:"stat",SERVER_ELAPSED:"internal_serverelapsed",DB_TOTAL_TIME:"internal_serverdbtotaltime",DB_CALLS:"internal_serverdbcalls",DB_FETCHES:"internal_serverdbfetches"}};window.PerfLogLevel=a;var b=window.Perf={currentLogLevel:a.DISABLED,mark:function(){return b},endMark:function(){return b},updateMarkName:function(){return b},measureToJson:function(){return""},toJson:function(){return""},setTimer:function(){return b},setServerTime:function(){return b},toPostVar:function(){return""},getMeasures:function(){return[]},getBeaconData:function(){return null},setBeaconData:function(){},clearBeaconData:function(){},removeStats:function(){},stat:function(){return b},getStat:function(){return-1},
onLoad:function(){},startTransaction:function(){return b},endTransaction:function(){return b},updateTransaction:function(){return b},isOnLoadFired:function(){return!1},util:{setCookie:function(){}},enabled:!1};})(this);

 
5. successfully redirect to your server 



## Supporting Material/References:  

1. assetfinder

2. Burp suite

## Impact

1. If you visit this site, attackers could try to steal information like your passwords, emails, or credit card details.

2.  your  server has redirect to malicious website  

3. i am continue to visit this so your server will crash  

4. your website access to malicious website

## Attachments
- Screenshot_from_2022-09-26_01-06-51.png
- Screenshot_from_2022-09-26_01-47-11.png
- Screenshot_from_2022-09-26_01-54-34.png
