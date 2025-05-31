# Account takeover w/o interaction for a user that doesn't have 2fa enabled via 2fa linking and improper auth at /api/2fa/verify

## Report Details
- **Report ID**: 810880
- **URL**: https://hackerone.com/reports/810880
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-04T16:47:58.615Z
- **Disclosed**: 2020-07-26T16:39:15.750Z

## Reporter
- **Username**: w2w
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: helium

## Vulnerability Information
##Description:
Hello, team! I found 2 vulnerabilities in your 2FA implementation:
1) There is a possibility to link 2FA to any other account if it wasn't set up before and user ID is known on the request /api/2fa. In order to do this, after performing a request for 2FA linking, substitute the ID to the victim's ID, organization could be any.

{F737177}

{F737178}

{F737179}

2) We can log in to the account without knowing login and password, using 2FA only, ID should be known. As you can see, in this request, we. don't use tokens/cookie that could be related to the user's ID, we are using only ID a561a2de-b8fe-49f8-8943-fb42229b7b08 and valid code.

Thus, using these 2 bugs we can fully takeover an account that doesn't have 2FA enabled (it was skipped after the first login).

##Steps to reproduce:
1. As a `user1`, register at https://console.helium.com, skip 2FA, copy the ID.
2. Register an account `user2`, register at https://console.helium.com, perform a 2FA request but with ID from `user1`. 2FA is enabled now on the account `user1`!
3. Perform a request /api/2fa/verify with valid code and ID of `user1`.

Result: You've successfully achieved an account takeover. In the future, you'll be able to log in again with this technique in the future, but a victim will have trouble logging in because of 2FA.

## Impact

If a victim's account ID is known, we can fully takeover an account without user interaction. User ID could be disclosed at https://console.helium.com/users (if our user role has access to this directory) or by using other techniques.

## Attachments
- x0ul4.png
