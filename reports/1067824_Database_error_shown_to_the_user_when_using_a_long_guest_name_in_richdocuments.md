# Database error shown to the user when using a long guest name in richdocuments

## Report Details
- **Report ID**: 1067824
- **URL**: https://hackerone.com/reports/1067824
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-12-28T22:33:09.675Z
- **Disclosed**: 2021-02-07T07:55:38.116Z

## Reporter
- **Username**: hitman_47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
When sharing a file to a guest and the file is allow for editing, the user is asked to enter a guestname if you enter a really long value for that name you get a database error that displays sensitive information:

An exception occurred while executing 'INSERT INTO `oc_richdocuments_wopi`(`fileid`,`owner_uid`,`version`,`canwrite`,`server_host`,`token`,`expiry`,`guest_displayname`,`template_destination`,`hide_download`,`direct`,`is_remote_token`,`template_id`,`share`) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)' with params [8606022, "8JaQyYP5xM7w2PJ6", 0, true, "https:\/\/demo2.nextcloud.com\/", "hUYL4uh9Dals51BoAT2YA7WZ1IJMaCLp", 1609196332, "reallylongnameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee (Guest)", 0, false, false, false, 0, "c4A53CW6wAN2ZZa"]: SQLSTATE[22001]: String data, right truncated: 1406 Data too long for column 'guest_displayname' at row 1

Demo
{F1133198}

## Impact

Information Disclosure

## Attachments
- recording-1609194562161.webm
