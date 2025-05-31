# Users contents on AWS  is cacheable 

## Report Details
- **Report ID**: 163131
- **URL**: https://hackerone.com/reports/163131
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-24T17:52:28.978Z
- **Disclosed**: 2016-09-06T19:35:00.098Z

## Reporter
- **Username**: abdullah
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi , 

Background 
=============================
As I know you are using AWS S3 for saving and serving files . 
The AWS  S3 on https://hackerone-attachments.s3.amazonaws.com are been called every time to show images on hackerone.com . 

For example view this report #145392 
You will see a request for Frans screenshot like this 

**Request**

```
https://hackerone-attachments.s3.amazonaws.com/production/000/099/965/94e13ba212b589eca016a39b56ac71ad5a058f1c/Screen_Shot_2016-06-17_at_15.18.36.png?AWSAccessKeyId=AKIAJFXIS7KJADBA4QQA&Expires=1472061826&Signature=CYZi6ZdC2xc4C8G4OpMhmccbKvs%3D

Host: hackerone-attachments.s3.amazonaws.com
User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://hackerone.com/
Connection: keep-alive
If-Modified-Since: *

```

**Response** 


```
HTTP/1.1 200 OK
x-amz-id-2: h01s331e54/8lHWaUmHtduvLcIDoriZs9c2dwmfd3kcWxNM9EsqUogYMZYSIa1js84RUtiLifaI=
x-amz-request-id: D8B3214210BC4461
Date: Wed, 24 Aug 2016 17:03:49 GMT
Last-Modified: Fri, 17 Jun 2016 13:18:46 GMT
Etag: "ccae076033025b6bdcfdc5df6aed64cd"
x-amz-server-side-encryption: AES256
Content-Disposition: attachment; filename=""
Accept-Ranges: bytes
Content-Type: image/png
Content-Length: 9710
Server: AmazonS3

```

----------  


The response doesn't give any header to control **cache**  and when no cache header is set the browsers behavior will automatically store a local cached copy of file received from AWS . So this content could be retrieved by other users who have access to the same computer . 

There are two affected uses : 

* Photos : because when you use {} to include image or you upload it and open it from attachments you will make the request and local copy of it will be stored without user knowledge . 

* Other files (e.g:video,xml,txt...etc.) : when you download  file a copy of it will be stored in cache without user knowledge too. Now this isn't an **usability** event why you cache a file that you will download ?! 
 
The cache files can be found here :

* Mozilla Firefox:
Unix/Linux: ~/.mozilla/firefox/<profile-id>/Cache/
Windows: C:\Documents and Settings<user_name>\Local Settings\Application
Data\Mozilla\Firefox\Profiles<profile-id>\Cache

* Internet Explorer:
C:\Documents and Settings<user_name>\Local Settings\Temporary Internet Files

--------------------
Tools 
=============

* Tools for view cache files :
   * FF : http://www.nirsoft.net/utils/mozilla_cache_viewer.html 
   * Chrome : http://www.nirsoft.net/utils/chrome_cache_view.html 
   * FF plugin (not recommended ): https://addons.mozilla.org/en-US/firefox/addon/cacheviewer2/?src=api
 

I viewed Frans report using Firefox and the cache viewer got the image I can view it and see the HTTP header 

{F114668}

Conclusion 
==================
The Images stored just by view it .  It is n't a secure practice . 


Scenario 
==================
**1-** User view his report in public,friend,company computer will store screen shots and the files he will download and delete it will be stored in cache and can be viewed . 
**2-** Member in a team views reports  in public,friend,company computer will store screen shots and the files he will download and delete it will be stored in cache and can be viewed . 


Fix 
=============
You should set :

* Cache-Control: no-cache, no-store
* Expires: 0
* Pragma: no-cache

Or minimize cache time because it will be stored there forever . 

Ref
============

1- https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9
2- https://www.owasp.org/index.php/Testing_for_Browser_cache_weakness_(OTG-AUTHN-006) 
 


Thanks for read all of this I am waiting your replay

BR  

## Attachments
- 8-24-2016_8-37-03_PM.jpg
