# DOM based reflected XSS in rockstargames.com/newswire/tags through cross domain ajax request

## Report Details
- **Report ID**: 172843
- **URL**: https://hackerone.com/reports/172843
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-09-29T08:28:52.602Z
- **Disclosed**: 2017-03-17T15:06:23.980Z

## Reporter
- **Username**: zombiehelp54
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rockstargames

## Vulnerability Information
Hi,
I have found a reflected XSS issue in `http://www.rockstargames.com/newswire/tags` which is , IMO , somekinda tricky. 

#PoC:
- **URL:** `http://www.rockstargames.com/newswire/tags#/?tags=\%2e%2e\%2e%2e\%2e%2e\comments_dal\users\getGlobalLoginSettings%2ejson?callback=alert(%2fxss%2f);%2f%2f` 
- **Vulnerable Parameter:** `#/?tags=` 
- **Payload:** `\%2e%2e\%2e%2e\%2e%2e\comments_dal\users\getGlobalLoginSettings%2ejson?callback=alert(%2fxss%2f);%2f%2f`  

{F123778}

The value of the `tags` parameter is sent as an XHR request to `/newswire/tagContent/[tags_param]/1` and the response gets printed in the page , also I have found that if the `content-type` of the response is `application/javascript` , it gets executed as javascript. 
After digging for a while I found this endpoint `www.rockstargames.com/comments_dal/users/getGlobalLoginSettings.json` which returns a callback function in the response if the request is XHR. so I used the callback function to execute javascript through `?callback=alert(/xss/);//` 

Thanks!

## Attachments
- xss_rockstargames.png
