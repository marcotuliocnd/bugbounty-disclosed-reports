# the domain is truck-admin.eu-east-1.indriverapp.com and Enter the management system of the blasting mobile phone verification code

## Report Details
- **Report ID**: 1991376
- **URL**: https://hackerone.com/reports/1991376
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-05-18T06:55:26.478Z
- **Disclosed**: 2023-09-11T07:22:56.605Z

## Reporter
- **Username**: trustworthy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: indrive

## Vulnerability Information
## Summary:
Find the mobile phone number of the administrator through the WHOIS information, and then send the verification code. Assuming that the verification code expires for 30 seconds or 1 minute, we can only explode the correct verification code in a short time to log in to the management system, so I choose to blast The verification code between 6000 and 7000, and sends the verification code every time it blasts, knows that the correct verification code is found, and I only exploded 8 times to find the correct verification code

## Steps To Reproduce:
  1. Find the management address through the directory scanning:https://truck-admin.eu-east-1.indriverapp.com/admin/auth
  2. Find the administrator's mobile phone number through WHOIS information:████████
  3. Send the verification code through the mobile phone number, you will receive a four -digit verification code
  4. Enter the four-digit verification code to log in and use Burpsuite to grab the package, blast the verification code and set the range of the verification code to 6000-7000, and the thread is set to 20 to ensure that the correct verification code can be blasting within 30 seconds within 30 seconds
██████████

request:
```
POST /proxy/truck/api/admin/login HTTP/2
Host: truck-admin.eu-east-1.indriverapp.com
Cookie: _gcl_au=1.1.354145541.1684380001; _ga=GA1.1.1412822094.1684380001; _ga_YBFM6LW448=GS1.1.1684382089.2.1.1684382341.58.0.0
Content-Length: 37
Sec-Ch-Ua: "Chromium";v="21", " Not;A Brand";v="99"
Accept: application/json, text/plain, */*
Content-Type: application/json
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://truck-admin.eu-east-1.indriverapp.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://truck-admin.eu-east-1.indriverapp.com/admin/auth
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9

{"phone":"██████","code":"1234"}
 ```
Burp  Settings:
█████████████
  5. Repeat 3,4 steps until the correct verification code is exploded
██████
6. Add the cookie obtained in the fifth step to the request header and access https://truck-admin.eu-east-1.indriverapp.com/admin/order,and then enter the management system
██████████
█████████

## Supporting Material/References:

  * [attachment / reference]

████
████
███

## Impact

Can get detailed information from all drivers and customers of the entire platform, including the driver's model license plate number, and customer taxi order records, taxi records include license plates/taxi position/reaching location, etc.

## Attachments
No attachments
