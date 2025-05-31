# Registered users can change app password permissions for any user

## Report Details
- **Report ID**: 297751
- **URL**: https://hackerone.com/reports/297751
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-12-14T04:42:47.787Z
- **Disclosed**: 2018-02-08T14:29:22.710Z

## Reporter
- **Username**: netranger
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Vulnerable URL

http://[server]/nextcloud/index.php/settings/personal/authtokens/[token ID]

## Summary

Nextcloud users can create app-specific passwords, also called authtokens, giving an app limited access to their account. Users can grant or deny access to their files for each app password.

The function to change a password's  file access ("filesystem") permissions contains an IDOR vulnerability. An authenticated user can change permissions for other user's app passwords by changing the app password ID number when submitting the vulnerable request.

The vulnerable parameter is in the JSON body sent to the vulnerable URL. Sample request:

PUT /nextcloud/index.php/settings/personal/authtokens/95 HTTP/1.1
Host: 192.168.1.22
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
requesttoken: vc5TVyC0GjTVwEX/YNUMeJ79CWq4W9G0/F6dJTOKMvE=:i6U7bkv2Tna8lXe2NbN6OdO/QgSKP7X1tR/kV1TsC6Q=
OCS-APIREQUEST: true
X-Requested-With: XMLHttpRequest
Content-Length: 109
Cookie: oc0xkd23iidt=prfrkbtr1t6bdqou018cajubv7; oc_sessionPassphrase=mz4sLu%2BmEY3MNj1ItWaTYM6PsBpJikK34msNsw1zA%2BuUJoM9J2zXY26eF7PDr9Dy9DpafNTaWN8iIBrGmh%2FDghSJASzTIwQhjW4gC%2B%2BTjIDBXm0THC7nixmxvdfIPxNA; nc_sameSiteCookielax=true; nc_sameSiteCookiestrict=true
Connection: close

{"id":95,"name":"thisiatest","lastActivity":1513224099,"type":1,"scope":{"filesystem":true},"canDelete":true}

The "id" parameter is the one vulnerable to IDOR.

## Reproduction

Pre-requisites: a Nextcloud server with a couple of test users, a browser setup to go through a proxy like Burp. A WebDav client is also helpful; I used cadaver on Ubuntu.

- Go to Burp, click the "Proxy" tab, click the "Intercept" subtab, and click "Intercept is On" to toggle interception off (if it's not already off)
- Login to Nextcloud with a test user
- Create an app password and uncheck "Allow filesystem access"
- Go to Burp, click the "Proxy" tab, click the "HTTP history" subtab, scroll down the list and find the call to the vulnerable URL. Note the value for the authtoken ID. It's the number at the end of the URL and is also the "id" value in the JSON request body
- Logout of Nextcloud
- If you have a webdav client, login with the password. For cadaver, open up a terminal and enter "cadaver http://[server]/remote.php/webdav", login with the app password, and issue the "ls" command. Nothing should appear, since this password lacks permission to the user's files
- Login to Nextcloud as the second user
- Create an app password for this user and uncheck 'Allow filesystem access"
- Go to Burp -> Proxy -> Intercept and toggle interception on
- Go back to the browser and re-check the "Allow filesystem access" box for the app we just created.
- Burp should stall the request for viewing. The request should be to the vulnerable URL; if it isn't, click "Forward" until the vulnerable URL appears
- In the JSON request body, change the value of the "id" parameter to the authtoken ID noted earlier, from the first victim user
- Forward the request (or toggle interception off, either works)
- Go back to the webdav client and issue the "ls" command again. You should now get a directory listing for the victim user. If you don't, exit the webdav client and try logging in again
- If you don't have a webdav client, log out of Nextcloud and log back in as the first user. Go to their Personal settings, scroll down to the authtoken/app specific password and click the 3 dot elipses icon. "Allow filesystem access" should now be checked, indicating our IDOR attack was successful in changing this authtoken's permissions

## Screenshots

1_request - vulnerable request as seen in Burp.

## Impact

## Impact/Notes

If an attacker gained access to an app password that did not have file system access, and the attacker had an account on the same Nextcloud server, he or she could grant file system permissions to the compromised app password and then gain access to the victim's files.

A malicious user could write a quick script to loop through app password IDs and revoke file system access. But this would not really affect data confidentiality and would be more of an annoyance for the victims.

While an attacker won't know the app password ID just by compromising it, he or she could use automation to try changing permissions on possible app password IDs.  Since the ID seems to start at 1 and increase sequentially, it should be feasible to "flip the switch" on the compromised password in a fairly short time, starting from 1 and working upwards.

Tested on Nextcloud 12.0.3, 12.0.4.

If I can provide any further information please let me know. Thanks!

## Attachments
- 1_request.png
