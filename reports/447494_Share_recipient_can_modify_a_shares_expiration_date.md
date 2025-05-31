# Share recipient can modify a share's expiration date

## Report Details
- **Report ID**: 447494
- **URL**: https://hackerone.com/reports/447494
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-11-20T05:07:57.241Z
- **Disclosed**: 2020-01-31T16:17:17.929Z

## Reporter
- **Username**: netranger
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Vulnerable URL

http://[server]/nextcloud/ocs/v2.php/apps/files_sharing/api/v1/shares/[share ID number]

## Summary

Nextcloud users can set expiration dates on documents they share with others. However, the function to update a share does not appear to properly validate the requester is the owner when changing a share's expiration date. A user could exploit the vulnerability to extend the expiration date of a file shared with them.

The vulnerable parameter appears to be the share ID number at the end of the request URL. Sample request:

PUT /nextcloud/ocs/v2.php/apps/files_sharing/api/v1/shares/74 HTTP/1.1
OCS-APIREQUEST: true
Authorization: Basic anJlYWNoZXI6d0xzVU5vVnpDZDFsNGpkdmIxZnFtOWlGUHpWbDRmWkNHTDdTMUtxRml3R3M1ZlFhc1FVUXNOV2tvY3gwcUVmbllnNmdBMVJR
User-Agent: Mozilla/5.0 (Android) ownCloud-android/3.3.2
Host: 192.168.1.22
Cookie: nc_sameSiteCookielax=true; nc_sameSiteCookiestrict=true; oc_sessionPassphrase=O5dbusaO3KwFs6e2P4ew7oE99UlUYbbpGa8ZwH01u6gHsvVjPiXfj362cyMkq4XNIIbYCqHESynLeG9VCWUDHHM%2B%2FHeitr910brNsOOTc5NnBy7g0JoY1uj1aY9KRQf7; oc0xkd23iidt=fc7vbute5s5efftqf2k9af9op0
Content-Length: 21
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Connection: close

expireDate=2018-11-25


## Reproduction

Pre-requisites: a Nextcloud server with a couple of test users, a browser setup to go through a proxy like Burp. 

- Go to Burp, click the "Proxy" tab, click the "Intercept" subtab, and click "Intercept is On" to toggle interception off (if it's not already off)
- Login to Nextcloud with a test user
- Share a file with another user. Set an expiration date, for example 17-05-2019
- Go to Burp, click the "Proxy" tab, click the "HTTP history" subtab, scroll down the list and find the call to the vulnerable URL. Note the value for the share ID (the integer at the end of the URL)
- Logout of Nextcloud
- Login to Nextcloud as the user you just shared the file with

At this point, we need to submit the vulnerable request as this second user. However, the vulnerable URL uses the PUT method so copy/pasting into a browser isn't really feasible. One way is to use a legitimate request as a "template" and insert the share ID of the file shared with us.

- As the second user, open a file's sharing dialog and share it with any user
- Go to Burp -> Proxy -> Intercept and toggle interception on
- Go back to the browser and set an expiration date such as 17-05-2020
- Burp should stall the request for viewing. The request should be to the vulnerable URL; if it isn't, click "Forward" until the vulnerable URL appears
- At the end of the URL, change the share ID number to the share ID noted earlier (the share ID of the file shared with the current user by the first user)
- Forward the request (or toggle interception off, either works)
- Logout and log back in as the first user. Navigate to the shared file and look at the expiration date. It should be 17-05-2020, demonstrating the share recipient has extended their access to the file by a year.

## Screenshots

1_request - vulnerable request as seen in Burp.

## Impact

## Impact/Notes

If someone shares a static file with another user, the vulnerability is less of an issue. The user granted access could download an offline copy  and refer to it after share access expires.

Where this issue becomes more concerning is with "living" files that an individual might frequently edit, like a spreadsheet. A share recipient could extend their access and continue to view updated file contents until someone noticed the share instance was still in place.

This does not appear to affect groups; i.e. if a group is the recipient of a share I have not been able to successfully invoke this vulnerability as a group member.

If I can provide any further information or help with proof of concept please let me know. Thanks!

## Attachments
- 1_request.png
