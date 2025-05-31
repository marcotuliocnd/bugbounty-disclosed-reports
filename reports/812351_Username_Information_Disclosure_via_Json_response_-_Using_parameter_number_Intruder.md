# Username Information Disclosure via Json response - Using parameter number Intruder

## Report Details
- **Report ID**: 812351
- **URL**: https://hackerone.com/reports/812351
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-03-06T19:27:48.065Z
- **Disclosed**: 2020-06-04T00:52:38.484Z

## Reporter
- **Username**: 0xrobot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:
Hi , Brave Team we found vulnerability's in your websites , I Found  all username disclosed using Json Response ``{parameter-number}``.

Platform(s) Affected: [website]
*. https://community.brave.com/c/brave-feature-requests.json
*. https://community.brave.com/c/beta-builds/38.json

## Steps To Reproduce:
  - Repreat URL ``.json`` to Burp Suite
  - Sent to Parameter **Burp-Intruder**
  - Set parameter , ``§random-number§`` , and start request
  - You can see **Sensitive Information** in Responsive Header ``Number-Parameter``

**Request**
```
GET /c/beta-builds/§38§.json HTTP/1.1
Host: community.brave.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
```
  - You can see Information Disclosure in Responsive Header ```200 OK.```

##POC Supporting Material/References (Screenshots)
  - F739659
  - F739660
  - F739661
  - F739658

## Impact

Information Disclousure

## Attachments
- ScreenshotsPOC.png
- ScreenshotsPOC1.png
- ScreenshotsPOC2.png
- Responsive.png
