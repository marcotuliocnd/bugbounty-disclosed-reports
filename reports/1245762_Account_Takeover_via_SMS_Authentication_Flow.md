# Account Takeover via SMS Authentication Flow 

## Report Details
- **Report ID**: 1245762
- **URL**: https://hackerone.com/reports/1245762
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-06-27T15:45:27.780Z
- **Disclosed**: 2022-01-12T10:08:30.046Z

## Reporter
- **Username**: yetanotherhacker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zenly

## Vulnerability Information
## Summary:
During the **authentication** flow, an SMS is sent to the user in order to validate the session and proceed to the user account. The way Zenly API handles this flow is by:
1. Calling the `/SessionCreate` endpoint with the mobile phone number of the user.
2. A session for the user is created and a session token is returned, but no operations with this session are possible until the verification is complete.
3. An SMS message is sent to the user, containing a verification code.
4. Calling the `/SessionVerify` endpoint with both the session token and the verification code received by SMS.
5. Once this request is successfully completed, the session token becomes valid and the user is now logged in.
After the first call to `/SessionCreate`, subsequent calls will return ==the same session token==, until a call to `/SessionVerify` is made with a valid verification code. 

## Steps To Reproduce:
To reproduce this issue, an environment that enables intercepting and decoding network requests is required. Once this environment is set up, we are able to gain visibility over network activity.
By following a typical login flow, we can gain knowledge of the network requests that are involved. The flow starts by requesting the mobile phone number from the user. Once the user inputs their phone number, they will be prompted for a verification code that is sent through SMS.
{F1355357}
At this moment, before entering the verification code, a request to `/SessionCreate` is launched. Note that this request (on the left) contains the mobile phone number of the user, and the response (on the right) to this request contains a **session token**, as shown below.
███████
Now, if an attacker also sends a request to `/SessionCreate` with the mobile phone number of the legitimate user, they will obtain the same session token. The response to this request, initiated by the attacker, is shown below:
█████████
**Note:** In this example, the attacker called `/SessionCreate` after the legitimate user. However, the attacker could also have called `/SessionCreate` before the legitimate user. This would have caused Zenly (on the side of the legitimate user) to obtain **the same session token that the attacker obtained**.
At this moment, the legitimate user will receive an SMS message containing a verification code. The authentication flow is finished (meaning the session token will become valid) once the user inputs this code in their Zenly application. However, once the user does this, the attacker will also end up with a valid session token in their hands (**since it is the same token**).
The attacker can then use this token to impersonate the legitimate user, executing any request to the Zenly API with it. The attacker can also, at any time, check if the session token is valid by launching a request to `/Me`, an endpoint that returns information about the current session. If the verification code has not yet been entered by the legitimate user, requests to `/Me` will return a 401 Unauthorized response. Once the code is entered, requests to `/Me` will return session information (such as phone number and user identifier), as shown below:
████
Once the attacker knows the session is valid, they can launch requests to `███████`, `██████` or `████` instead, thus **gaining access to notifications, geolocation, and conversations** of the legitimate user and their friends. 

## Suggested Mitigation:
In order to mitigate this issue, the following steps could be taken:
-	Session tokens should be unique for each call to `/SessionCreate`.
-	A new SMS code should be sent on every call to `/SessionCreate`.
-	Previous SMS codes should be invalidated once a new one is sent.
-	Apply rate-limiting to both `/SessionCreate` and `/SessionVerify` endpoints.

## Impact

An attacker can take over a user account by abusing the `/SessionCreate endpoint`, which will consistently return the same session token (although not yet valid) for the same user. Once the legitimate user validates the SMS code for that session token, the session will become valid for both the legitimate user and the attacker.
The main point of this issue is that the attacker needs to obtain a session token before the legitimate user calls the `/SessionVerify` endpoint. This can be done either before or after the legitimate user calls the `/SessionCreate endpoint`. 
Allowing both the legitimate user and an attacker to have the same session token will give an advantage to the attacker. The verification code sent through SMS will remain valid for the same amount of time that the session token is valid, and it will not be regenerated within that time period, meaning that if the legitimate user inputs this code in the application (triggering a call to `/SessionVerify`), the session token that both the legitimate user and the attacker hold will become valid. This means that the attacker now has a valid session for the account of the legitimate user, even though the attacker never knew the verification code.
On the other hand, even if the attacker wasn’t able to obtain the session token (through a call to `/SessionCreate`) before the legitimate user, this attack is still possible while the legitimate user doesn’t input the correct verification code in the application, although this scenario would be less likely since the time window for carrying out this attack can be rather short.
**Once the attacker has a valid session for the account of the legitimate user, they can access their location, notifications, conversations, and friends’ information just like the legitimate user could.**

## Attachments
- Picture7.png
