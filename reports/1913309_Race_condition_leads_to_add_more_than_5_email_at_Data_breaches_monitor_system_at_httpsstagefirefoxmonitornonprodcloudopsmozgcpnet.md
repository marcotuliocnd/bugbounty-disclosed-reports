# Race condition leads to add more than 5 email at Data breaches monitor system at https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net

## Report Details
- **Report ID**: 1913309
- **URL**: https://hackerone.com/reports/1913309
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-03-20T18:36:23.801Z
- **Disclosed**: 2024-10-18T08:16:07.286Z

## Reporter
- **Username**: sushantd19
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Summary:
Hii

at https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net we can add  emails for the monitor to check this are in data breach or not 
here have add email for the monitor limit a 5 we can't add more than 5 email 

█████

## Steps To Reproduce:

* Visit https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/user/settings -> add email and see you can add only 5 email 

* now capture the add email request 

```javascript
POST /api/v1/user/email HTTP/2
Host: stage.firefoxmonitor.nonprod.cloudops.mozgcp.net
Cookie: connect.sid=█████; _ga_CXG8K4KW4P=GS1.1.1679333065.1.1.1679336292.0.0.0; _ga=GA1.1.518394987.1679333065
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0
Accept: text/html
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/user/settings
Content-Type: application/json
X-Csrf-Token: 0787d9f55701a244aa8f68401f2dc6aebb55a1b83ee2930743ba1324314b5c2cb87fafa7bac74afd8d4660feff2ce33d5b38fb949478c5b9f32430e863ced6b4
Content-Length: 33
Origin: https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: same-origin
Sec-Fetch-Site: same-origin
X-Pwnfox-Color: blue
Te: trailers

{"email":"████████"}
```

* send this to intruder -> add email list and start the attack

* at the end you will able to add more than 5 emails 

███

## Impact

Race condition leads to add more than 5 email at Data breaches monitor system at https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net

thanks
@sushantdh0pat

## Attachments
No attachments
