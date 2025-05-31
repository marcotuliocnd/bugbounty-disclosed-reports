# Login email verification bypass via `/oauth/token`.

## Report Details
- **Report ID**: 2676025
- **URL**: https://hackerone.com/reports/2676025
- **State**: Closed
- **Severity**: none
- **Submitted**: 2024-08-22T14:00:31.067Z
- **Disclosed**: 2024-09-03T17:51:10.641Z

## Reporter
- **Username**: cybxis
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
Hello team, I want to report a security issue on the GitLab authentication functionality. The email verification on login provides an additional layer of security despite 2FA not being implemented. This security measure is being triggered once the account has  three or more failed sign-in attempts in 24 hours or a user attempts to sign in from a new IP address. Reference [here](https://docs.gitlab.com/ee/security/email_verification.html#:~:text=After%20a%20successful%20sign%20in,can%20also%20reset%20your%20password.)

Gitlab also supports another basic authentication which is the [Resource Owner Password Credentials (ROPC)](https://docs.gitlab.com/ee/api/oauth2.html#resource-owner-password-credentials-flow) flow. It is where the user credentials(username and password) will be exchanged for an access token with full read and write scope on the endpoint `/oauth/token`. Just like the web authentication, there is also an implemented restriction on this endpoint to avoid any unauthorized authentication. For example, sending the token exchange request on the said endpoint from a new IP address will result to the following API error response:
```
{"error":"invalid_grant","error_description":"The provided authorization grant is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client."}
```
However, this restriction is only being implemented if there is no active session on the account.

I have discovered that it is possible to bypass this restriction. During my testing, the restriction on `/oauth/token` is being voided once the victim authenticates and completes the email verification regardless of the IP difference between the attacker and the victim.

##Exploit
```javascript
#!/usr/bin/sh

USERNAME=gitlab_username
PASSWORD=gitlab_password

while true
do
curl --data "grant_type=password&username=$USERNAME&password=$PASSWORD&scope=api" \
     --request POST "https://gitlab.com/oauth/token"

    echo ''

    sleep 1.5
done
```
The simple bash script above will serve as an event listener for the attacker. Please note that if the account has already an active session (which means it already completed the email verification) the token exchange will be successful on the first request. Otherwise, it will loop with errors until the victim authenticates and completes the verification on any device or IP.

##Current Behavior
* The server only checks whether the account has an active session that has completed an email verification on any device and IP address.

##Expected Behavior
* The server must somehow validate the authenticity of the user sending the request on `/oauth/token` . E.g. sending an email verification link(not code).

##Clarification
This bug only affects accounts with 2FA disabled / no configured.

### Steps to reproduce
For this to reproduce, your GitLab account must trigger the email verification feature on login. To do this, you can do one of the following.
* Logout all your session and restart your pc
* Logout all your session and deliberately commit 3 to 5 incorrect password attempt until you see the warning `Maximum login attempts exceeded. Wait 10 minutes and try again.`. Then wait for 10 minutes to login the correct credentials.

You need two(2) devices with different IP addresses. In my case (my VPS terminal and my local machine).

`As an attacker:`
	1. Login the account via `/oauth/token` endpoint by running the bash script on your terminal to prove the RESTRICTION (IP is flagged and the API will respond an error message mentioned earlier this report). 
    2. Keep it running and notice that there is no success on the authentication.

`As the Victim:`
	3. Login the account on victim on [web login](https://gitlab.com/users/sign_in) which will require an email verification. 
	4. Complete the verification by providing the verification code sent to the email. Sometimes it is delayed, so you might want to resend the code .

Once the victim is successfully authenticated, the attacker request on the terminal is also being authenticated and able to get access and refresh token.

##Demo and PoC
█████

##Suggested Fix
The implemented mitigation is somehow not sufficient. Relying on the active sessions simply gives the attacker the success since victims always complete this verification step on their trusted devices. There should be a more strict verification process on the vulnerable endpoint such as sending a verification link on the victim's email address notifying them that an ROPC access request is being attempted from a certain device and IP address.

## Impact

This bug makes the implemented additional layer of security ineffective. This is simply a demonstration where the victim unknowingly completes an email verification for the attacker to access his/her own compromised credentials.

## Attachments
No attachments
