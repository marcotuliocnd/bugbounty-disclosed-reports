# Password Reset Link Works Multiple Times

## Report Details
- **Report ID**: 772886
- **URL**: https://hackerone.com/reports/772886
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-01-13T00:05:02.929Z
- **Disclosed**: 2020-02-24T10:59:41.164Z

## Reporter
- **Username**: exag0ra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
## Background: 
Normally, a secure way to handle password reset links is to invalidate the link/token upon usage. Additionally, if multiple reset links are requested, older & unused tokens should also be invalidated (i.e., if 2 reset tokens were requested, the 2nd token should be invalid upon your usage of the 1st token, or vice versa). This appears to be working properly for NordVPN; however, there is an interesting bypass to this technique which causes some weird back-end issues for the user, not allowing them to log out of their account or send additional reset links.

## Summary:
It appears as though NordVPN uses two methods at two different endpoints (i.e., `/change-password/` and `/reset-password/`) to reset a user's password. By combining both methods, you are able to use multiple valid password reset tokens for one single account. Upon successful password change the 2nd time, the user is greeted with a `403 - Forbidden` message, disallowing them to logout or send additional reset links -- causing an inability to use the account until an IP address change and browser reset occur. That being said, here are a little more details on the methods for the reset tokens: 

**Method 1**
While _authenticated_, login to your account navigate to `Change password` and request a link. In your email, your link will be as:  
 * https://ucp.nordvpn.com/change-password/TOKEN/

**Method 2**
While unauthenticated, simply select `Forgot your password?` on https://ucp.nordvpn.com/. In your email, your link will be as: 
 * https://ucp.nordvpn.com/reset-password/DIFFERENT-TOKEN/

## Steps To Reproduce:
**Manual PoC**
  1. First, login to your account and navigate to the `Change Password` and select `Send Reset Link`. (**F682723**)
  1. Logout of your account and navigate to https://ucp.nordvpn.com/login.
  1. Select `Forgot your password?` and place in your email address. (**F682738**)
  1. You should now have two emails from NordVPN which mention to reset your password. 
  1. Follow both links, open them in two different tabs, and make special note of the difference in endpoints (i.e., one is `/reset-password/` and the other is `/change-password/`). 
  1. Enter a new password into the first link (my password was "33333333"). In my case it was this endpoint: https://ucp.nordvpn.com/change-password/TOKEN/ that I used first.
  1. Login and verify your password has changed. 
  1. Logout and navigate to the second browser tab with the https://ucp.nordvpn.com/reset-password/DIFFERENT-TOKEN/ still up.
  1. Change the password to something else. My new password was "77777777". 
  1. Make note that you will probably hit several errors:  **1** - 429 (too many requests), **2** - 403 (forbidden), and **3** - "Something went wrong".
  1. Change your IP address, in my case I was already using a VPN and just selected a new location.
  1. After my IP address changed, I was able to reset the password successfully and verified that my new password was now the one I used for my 2nd token, "77777777".

> _Note:_ After Step 6, you want to make sure that both screens have `New Password` and `Confirm Password`, rather than back at the email login screen (i.e., `Username or email address` and `Password` is what you don't want to see for either of the links you followed).

**Video PoC with timestamp descriptions**
 {F682727}
  1. 0:02 - 0:17 -- creating a new password (33333333) and logging in.
  1. 0:23 -- navigated to the second token endpoint `/reset-password/`
  1. 0:29 -- 403 error, which means you are typically forbidden from whatever action you are trying to perform
  1. 0:31 -- attempted to send the request multiple times as a Hail Mary for a potential Race Condition
  1. 0:45 -- I put "3333" at the end of my username to show this was the prior password from the 1st reset link -- which, at this point should log me in since I was greeted ever-so kindly by the 403 error.
  1. 0:50 -- logged in with password "33333333" from the 1st reset link. 
  1. 0:54 - 0:57 -- now got a 429 and 403 response. This is what I want in order to bypass the restriction.
  1. 1:20 - 1:23 -- reset my IP address and tried again with password "77777777".
  1. 1:24 -- notice I now have no errors and get redirected back to the main login page. If all went well, I should now be able to login with "77777777" and **not** "33333333". 
  1. 1:36 - 2:11 -- attempting to login with the new password of "77777777" along with the old password of "33333333" and received the **Something went wrong error**.
  1. 2:15 -- the interesting part here is that I got two hits for password resets, noted by two separate emails from NordVPN. One from the `/change-password/` token and the other from the `/reset-password/` token.
  1. 2:30 - 2:41 -- logging in with the password of "77777777", which shouldn't have worked since the token should be invalid, and I was hit with multiple error messages.

## Asset Affected:
https://ucp.nordvpn.com/login endpoints:
  * `/reset-password/`
  * `/change-password/`

## Supporting Material/References:

**Authenticated password change:**
  * {F682723}

**403 error while trying to logout**
  * {F682724}

**Unauthenticated password change**
  * {F682738}

**Unable to Logout after using both links (video):**
  * {F682726}

**Video PoC**
  * {F682727}

**Vulnerability Reference [Table](https://bugcrowd.com/vulnerability-rating-taxonomy)**

| Potential Rating  | Category  | Issue  | Description  |   |
|---|---|---|---|---|
| P4  |  Broken Authentication and Session Management |  Failure to Invalidate Session |  On Password Reset and/or Change |   |
|   |   |   |   |   |

**Similar Reports:**
https://hackerone.com/reports/283550
https://hackerone.com/reports/576510

> _Note:_  This issue seems to be rather unique, and I honestly haven't seen this behavior ever happen before -- this was a very fun find and a super interesting bug. However, I did try to find as similar reports as I could for you, which are linked above  :)

## Impact

**Main Issue:**
At attacker may be able to take over another user's account. 

**Secondary Issue:**
The application issues two valid reset tokens for one user. After the 1st token is used, the 2nd token is able to be used as well (i.e., the application is *not* properly invalidating multiple tokens). Upon successful re-login, the user is unable to logout or perform additional activities until they reset their IP address and refresh their browser. They are simply stuck in 403 Limbo Land... and who wants to hang out there?!

## Attachments
- authenticated_reset.PNG
- cannot_log_out.PNG
- 403_error.mp4
- token_invalidation.mp4
- reset_password.PNG
