# Error in Deleting Deck cards attachment reveals the full path of the website

## Report Details
- **Report ID**: 1354334
- **URL**: https://hackerone.com/reports/1354334
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-09-29T07:58:44.946Z
- **Disclosed**: 2022-05-20T14:04:08.967Z

## Reporter
- **Username**: ctulhu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:

An error in deck cards when deleting an attachment reveals the full path of the website.

```
DELETE /apps/deck/cards/11/attachment/file:1 HTTP/2
Host: ctulhu.me/nc
Sec-Ch-Ua: "Chromium";v="93", " Not;A Brand";v="99"
Accept: application/json, text/plain, */*
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36
Sec-Ch-Ua-Platform: "macOS"
Origin: https://ctulhu.me/nc
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
```

### Response

```
HTTP/2 500 Internal Server Error
Date: Wed, 29 Sep 2021 07:42:43 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 2057
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Pragma: no-cache
Cache-Control: no-cache, no-store, must-revalidate
Content-Security-Policy: default-src 'none';base-uri 'none';manifest-src 'self';frame-ancestors 'none'
Feature-Policy: autoplay 'none';camera 'none';fullscreen 'none';geolocation 'none';microphone 'none';payment 'none'
X-Robots-Tag: none
Referrer-Policy: no-referrer
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: SAMEORIGIN
X-Permitted-Cross-Domain-Policies: none
X-Robots-Tag: none
X-Xss-Protection: 1; mode=block
Cf-Cache-Status: DYNAMIC
Server: cloudflare
Cf-Ray: 69639391d9741f21-FRA
Alt-Svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400

{"status":500,"message":"There was an error retrieving the share. Maybe the link is wrong, it was unshared, or it was deleted.","exception":{"\u0000OC\\HintException\u0000hint":"","\u0000*\u0000message":"There was an error retrieving the share. Maybe the link is wrong, it was unshared, or it was deleted.","\u0000Exception\u0000string":"","\u0000*\u0000code":0,"\u0000*\u0000file":"\/var\/www\/██████████\/custom_apps\/deck\/lib\/Sharing\/DeckShareProvider.php","\u0000*\u0000line":586,"\u0000Exception\u0000trace":[{"file":"\/var\/www\/████████\/custom_apps\/deck\/lib\/Service\/FilesAppService.php","line":140,"function":"getShareById","class":"OCA\\Deck\\Sharing\\DeckShareProvider","type":"-\u003E"},{"file":"\/var\/www\/█████\/custom_apps\/deck\/lib\/Service\/AttachmentService.php","line":339,"function":"extendData","class":"OCA\\Deck\\Service\\FilesAppService","type":"-\u003E"},{"file":"\/var\/www\/██████████\/custom_apps\/deck\/lib\/Controller\/AttachmentController.php","line":96,"function":"delete","class":"OCA\\Deck\\Service\\AttachmentService","type":"-\u003E"},{"file":"\/var\/www\/███████\/lib\/private\/AppFramework\/Http\/Dispatcher.php","line":217,"function":"delete","class":"OCA\\Deck\\Controller\\AttachmentController","type":"-\u003E"},{"file":"\/var\/www\/███████\/lib\/private\/AppFramework\/Http\/Dispatcher.php","line":126,"function":"executeController","class":"OC\\AppFramework\\Http\\Dispatcher","type":"-\u003E"},{"file":"\/var\/www\/█████\/lib\/private\/AppFramework\/App.php","line":156,"function":"dispatch","class":"OC\\AppFramework\\Http\\Dispatcher","type":"-\u003E"},{"file":"\/var\/www\/██████████\/lib\/private\/Route\/Router.php","line":301,"function":"main","class":"OC\\AppFramework\\App","type":"::"},{"file":"\/var\/www\/██████\/lib\/base.php","line":1000,"function":"match","class":"OC\\Route\\Router","type":"-\u003E"},{"file":"\/var\/www\/█████████\/index.php","line":36,"function":"handleRequest","class":"OC","type":"::"}],"\u0000Exception\u0000previous":null}}
```

## Steps To Reproduce:
[add details for how we can reproduce the issue]

* 0.) setup burpsuite
* 1.) go to $website/apps/deck and pick any cards
* 2.)  attach a file to the card and delete it
* 3.) On burp suite go to proxy > http history > find the request
* 4.) send the request to repeater and run the request again

## Impact

Full path disclosure

## Attachments
No attachments
