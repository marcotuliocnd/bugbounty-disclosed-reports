# Shared file link - password protection bypass under certain conditions

## Report Details
- **Report ID**: 231917
- **URL**: https://hackerone.com/reports/231917
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-05-25T19:19:24.928Z
- **Disclosed**: 2018-09-25T14:33:52.440Z

## Reporter
- **Username**: netranger
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary

An unauthenticated remote attacker can bypass password protection on certain shared file types through the file sharing app's publicpreview.php function.

## Vulnerable URL

http://[server]/nextcloud/index.php/apps/files_sharing/ajax/publicpreview.php?x=[width]&y=[height]&t=[share ID]

## Description

Nextcloud users have the option to protect files shared via a link with a password. Recipients must enter the correct password when trying to view the shared file. However, if the shared file is an image file, an unauthenticated remote attacker can obtain a preview of the file through the vulnerable URL by passing the file's share ID as the value of the 't' parameter. Nextcloud returns a preview of the file without prompting for the unlock password first. If the shared file is an image, an attacker can essentially retrieve the user's image file in it's entirety through the preview function.

## Reproduction

- Login to a Nextcloud server, select an image, and share it via a link. Password protect the share with any password.
- Copy the share link/URL. Note the share ID, which is the last part of the URL containing 15 random letters and numbers.
- Log out of Nextcloud, ending your session (not necessary but makes the demonstration more meaningful).
- Verify the share is password protected by visiting the share link and ensuring you are prompted for the share password.
- Paste and visit the following vulnerable URL into your browser. Replace [server] with the hostname or IP address of your Nextcloud server and replace [share ID] with the share ID that was noted in step 2.
http://[server]/nextcloud/index.php/apps/files_sharing/ajax/publicpreview.php?x=200&y=200&t=[share ID]
- Nextcloud should return a preview of the shared image, with dimensions equal to the 'x' and 'y' parameters (200 x 200 in this example). If the returned image is too small, you can adjust 'x' and 'y' to get a larger preview and ultimately recover the entirety of the shared image without ever entering the password.

## Attachments

1 share settings.png - demonstrates my test file's share settings.
2 password protected.png - demonstrates visiting the password protected file's link and getting prompted for a password.
3 preview 1.png - demonstrates getting a partial view of the file through the preview function. No password required.
4 preview 2.png - a larger preview (x and y parameters modified). Compared to picture 3 I have recovered more of the image, especially on the left and right edges.

## Impact/Notes

Image files are the most susceptible to this attack. Text files and markdown files generate preview images which can also be recovered using this technique; however, their generated preview images contain only a small portion of the overall file. Realistically speaking an attacker can recover limited information from a text file's preview image, usually just a few words total.

Other file types such as MS Office and PDF documents have their preview providers disabled by default. They may be vulnerable to this vulnerability but Nextcloud's security model assumes enabling their preview providers is insecure anyway (https://nextcloud.com/security/threat-model/) so I did not check them.

An attacker does not have to be authenticated to Nextcloud but does need to know the share ID to exploit this vulnerability.

## Possible Mitigation

Consider adding a check in the preview handler to only render a preview if the shared file isn't password protected or if the user has already entered the correct password.





## Attachments
- 1_share_settings.png
- 2_password_protected.png
- 3_preview_1.png
- 4_preview_2.png
