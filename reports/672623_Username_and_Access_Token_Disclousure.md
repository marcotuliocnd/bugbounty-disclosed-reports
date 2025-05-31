# Username and Access Token Disclousure

## Report Details
- **Report ID**: 672623
- **URL**: https://hackerone.com/reports/672623
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-08-13T19:37:00.040Z
- **Disclosed**: 2020-03-01T11:22:19.644Z

## Reporter
- **Username**: jannikg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Versions
=====================
Nextcloud Server Version: 16.0.3.0
it.tsweb.Nextcloud (iOS App) Version: 2.23.7

Description
=====================
While logging in to an owncloud instance the iOS client sends the Username and password to the ressource
`/login?redirect_url=/login/flow/grant`
and recieves an token by the ressource /login/flow in the process. This happens in the form of an HTTP 303 redierect Location [Picture 1].
`/login/flow/grant?clientIdentifier=&stateToken=ji76VUQooqEHFwIPyUUHkAqGaazB8XJ5DHQiJK6vk5aBLfhS1XMf2flTMPVxgFm3`

This Token is from now on used to authenticate every request made by the App to the owncloud instance [Picture 4].
This happens in the form of an Basic-Authentication header, where username and password are encodet in an Base-64 String [Picture 3].

Additionally the iOS client automaticaly registers some user specific parameters at `push-notifications.nextcloud.com` without notifying the user. While this process the client also sends the Basic-Authentication header of the owncloud instance to the third Party server [Picture 2].

## Impact

This leads to an massive user information disclousure which affects all iOS users of the nextcloud App (i have not tested Android) to the third party `push-notifications.nextcloud.com`.
The owner of the domain and the operator of the server recieve a high ammount of valid Usernames an access tokens of every owncloud instance with iOS users.

## Attachments
- 1.png
- 2.png
- 3.png
- 4.png
