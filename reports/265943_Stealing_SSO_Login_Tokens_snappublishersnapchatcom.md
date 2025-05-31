# Stealing SSO Login Tokens (snappublisher.snapchat.com)

## Report Details
- **Report ID**: 265943
- **URL**: https://hackerone.com/reports/265943
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-09-05T07:03:06.903Z
- **Disclosed**: 2021-07-29T22:37:09.907Z

## Reporter
- **Username**: coolboss
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
# Description
Attacker can steal SSO login tokens for snappublisher.snapchat.com by chaining different flaws in SSO and Snapchat’s Snappublisher tool. Detailed attack flow is as follows.

# Attack Flow
1.. Snapchat fetches a `SSO LOGIN TOKEN` from `accounts.snapchat.com` to login into different products of Snapchat i.e. SnapPublisher, Ads Manager, Business Manager, etc. provided that user is logged into `accounts.snapchat.com`.
eg. To login into SnapPublisher following requests are made …
1] https://accounts.snapchat.com/accounts/login?client_id=creativesuite-prod&referrer=https://snappublisher.snapchat.com/sso_continue
2] 302 redirect to
https://accounts.snapchat.com/accounts/sso?client_id=creativesuite-prod&referrer=https%3A%2F%2Fsnappublisher.snapchat.com%2Fsso_continue
3] again 302 redirect to 
https://snappublisher.snapchat.com/sso_continue?ticket=redacted

So, a SSO login token `ticket` is sent from `accounts.snapchat.com` to `snappublisher.snapchat.com` which is used to login the user. And is also used in `Authorization header` when making requests to API.

Now, we are going to steal this SSO login token `ticket` which will allow us to login and control victim’s account.

2.. On `snappublisher.snapchat.com`, I was able to upload a `svg` image to google cloud storage, using which I run my javascript code.
Note: Use `import from site` functionality via `https://snappublisher.snapchat.com/snaps/create/new` and import my `xss-svg` image from here (███████/tokenstealer.svg). This alerts and logs `#hashfragment` in the console. 
I have already did this in my POC so this is just for understanding purpose. My image URL is `https://snappublisher.snapchat.com/api/v1/media/████████/file/somthine.svg?%23pranav`

3.. Now, other flaws in SSO …
1] In this URL 
`https://accounts.snapchat.com/accounts/sso?client_id=creativesuite-prod&referrer=https://snappublisher.snapchat.com/api/v1/media/████████/file/somthine.svg?%23pranav`

`referrer` parameter can be controlled and any `snappublisher.snapchat.com` URL is allowed.
Also, `%23pranav`, this `#hashfragment` is allowed in `referrer ` parameter. 

I take advantage of both these flaws to flow the `SSO login token` to my website or land to a page which I control.
Note: `#hashfragment` is send further by browser for `302` / `307` redirects.


4.. CSRF Login flaw
SSO functionality is vulnerable to CSRF attack so I can login other people into my account. I use this functionality to login user into my account.

5.. Token doesn’t expire flaw 
Once the SSO login token is used, it doesn’t expire and can be reused multiple times.

So, simple attack flow is as follows :
1. User is logged into `accounts.snapchat.com`.
2. Attacker logs user into his/her `snappublisher.snapchat.com` account via CSRF login flaw.
3. Now, attacker makes a request to fetch SSO login token `https://accounts.snapchat.com/accounts/sso?client_id=creativesuite-prod&referrer=https://snappublisher.snapchat.com/api/v1/media/█████████/file/somthine.svg?%23pranav` and redirects the token in `#hashfragment` to `https://snappublisher.snapchat.com/api/v1/media/█████/file/somthine.svg?%23pranav`
4. `https://snappublisher.snapchat.com/api/v1/media/████/file/somthine.svg?%23pranav` this redirects with `307` status code to `storage.googleapis.com/creativesuite-prod-media/*` with `SSO login token ticket` in  `#hashfragment` carried forward by browser.
5. Svg image executes my js code and alerts and logs the `SSO login token ticket` in the console.
6. I can use the `ticket` to login into victim’s account. Via `https://snappublisher.snapchat.com/sso_continue?ticket=<stolen token>`

# Proof Of Concept

Video POC : █████████(Unlisted video on youtube)

1. Login into your account on `accounts.snapchat.com`.
2. Login into your SnapPublisher account `snappublisher.snapchat.com`.
3. Visit (█████) which fetches `user’s SSO login token` which can be used to login. (This alerts and logs the `token` in console.)
4. Use the token via `https://snappublisher.snapchat.com/sso_continue?ticket=<stolen token>`


# Impact 
1. Gain unauthorized access to Snappublisher account.
2. Can use the SSO login token to make API requests.

# Recommendations

1. For SSO functionality …
1] Add `state` param to prevent `CSRF login` on `https://snappublisher.snapchat.com/sso_continue?ticket=<token>` 
2] In `referrer` param of the following URL 
`https://accounts.snapchat.com/accounts/sso?client_id=creativesuite-prod&referrer=https://snappublisher.snapchat.com/api/v1/media/██████████/file/somthine.svg?%23pranav` disallow `#hashfragments` to be included.
3] Make the `referrer` param of the following URL 
`https://accounts.snapchat.com/accounts/sso?client_id=creativesuite-prod&referrer=https://snappublisher.snapchat.com/api/v1/media/███████/file/somthine.svg?%23pranav` more specific and restricted similar to your OAuth2 adsapi.
4] SSO login token should be one time use and should not be able to use it again and again.

2. For SnapPublisher
1] I observed you are using Google Cloud Storage, so blocking `svg` images or disallowing any uploads of `svg-xss` images will further enhance security. Otherwise, one can easily get `xss` on `storage.google`


Let me know if you need any help. :-)

Regards,
Pranav Hivarekar


## Attachments
No attachments
