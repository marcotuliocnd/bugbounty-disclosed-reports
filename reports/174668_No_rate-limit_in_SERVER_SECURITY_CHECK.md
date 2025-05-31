# No rate-limit in SERVER_SECURITY_CHECK

## Report Details
- **Report ID**: 174668
- **URL**: https://hackerone.com/reports/174668
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-08T14:57:33.337Z
- **Disclosed**: 2016-11-10T15:03:30.459Z

## Reporter
- **Username**: c0rte
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bumble

## Vulnerability Information
Hi,

When you login in another Ip address Badoo will ask to confirm mobile number to authenticate.
The problem is that there is no limit of tries.

This make this feature useless since it can be brute forced.
In the video you can see at request 56 we found the right number which lead to authentication.

Response when found right number:

```
HTTP/1.1 200 OK
Server: nginx
Date: Sat, 08 Oct 2016 14:29:46 GMT
Content-Type: application/json
Connection: close
X-BMA-Server: www33
X-User-id: 471337266
X-Session-id: meba0dcc7466641ca981034c8c2df3090
X-Static-Version: 10735
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Timing-Allow-Origin: https://eu1.badoo.com
Content-Length: 494

{"$gpb":"badoo.bma.BadooMessage","message_type":6004,"version":1,"message_id":13,"body":[{"$gpb":"badoo.bma.MessageBody","client_security_check_result":{"$gpb":"badoo.bma.ClientSecurityCheckResult","complete":true,"success":true},"message_type":528},{"$gpb":"badoo.bma.MessageBody","server_error_message":{"$gpb":"badoo.bma.ServerErrorMessage","error_code":"15","error_message":"Security check required","error_id":"captcha_10","error_eta":394,"type":15},"message_type":1}],"responses_count":2}
```

Wrong number:
```
HTTP/1.1 200 OK
Server: nginx
Date: Sat, 08 Oct 2016 14:29:42 GMT
Content-Type: application/json
Connection: close
X-BMA-Server: www88
X-User-id: 471337266
X-Session-id: meba0dcc7466641ca981034c8c2df3090
X-Static-Version: 10735
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Timing-Allow-Origin: https://eu1.badoo.com
Content-Length: 528

{"$gpb":"badoo.bma.BadooMessage","message_type":6004,"version":1,"message_id":13,"body":[{"$gpb":"badoo.bma.MessageBody","client_security_check_result":{"$gpb":"badoo.bma.ClientSecurityCheckResult","complete":true,"success":false,"error_text":"DÃgitos errados."},"message_type":528},{"$gpb":"badoo.bma.MessageBody","server_error_message":{"$gpb":"badoo.bma.ServerErrorMessage","error_code":"15","error_message":"Security check required","error_id":"captcha_10","error_eta":394,"type":15},"message_type":1}],"responses_count":2}
```

Thanks,
Diogo Real



 

## Attachments
- Screenshot_from_2016-10-08_15-16-37.png
- Bruteforce.mp4
