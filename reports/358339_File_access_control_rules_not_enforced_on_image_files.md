# File access control rules not enforced on image files

## Report Details
- **Report ID**: 358339
- **URL**: https://hackerone.com/reports/358339
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-05-28T15:24:21.302Z
- **Disclosed**: 2018-06-15T21:24:24.625Z

## Reporter
- **Username**: reinism
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
1. Installed Nextcloud from Snap package (version 13.0.2snap1, revision 6916) on fresh Ubuntu 18.04 LTS install.
2. Installed and enabled Files access control (v1.3.0) and Files automated tagging (v1.3.0) apps.
3. As an administrator created an invisible collaborative tag `Secret`.
4. Added Files automated tagging rule to add the `Secret` tag for all files with user membership of `admin` group.
5. Added Files access control rule restricting the access for all files with the `Secret` tag and user who is not a member of `admin` group.
6. Created unprivileged user `user`.
7. Accessed the `admin` account from WebDAV interface (in order to avoid generating automatic file previews) and created the following files/folders on the server:

    ```
    folder:    Secret_Folder
    folder:    Secret_Folder/Secret_Subfolder
    file:      Secret_Folder/Secret_Subfolder/Secret_Picture.jpeg
    file:      Secret_Folder/Secret_Subfolder/Secret_Text.txt
    ```
8. Shared the `Secret_Folder` from `admin` user to the unprivileged user `user` with no edit rights.
9. From client computer authorized as the unprivileged user `user` and used WebDAV search to recursively list all files with their MIME types with the following `curl` command: {F302611}. This command downloaded the list of all shared files as an xml file: {F302614}.
10. Identified an image file `Secret_Folder/Secret_Subfolder/Secret_Picture.jpeg` from the file list and accessed its contents through files preview API with the following `curl` command:

    ```
    curl -u user 'https://test.frp.lv/index.php/apps/files/api/v1/thumbnail/1212/750/Secret_Folder/Secret_Subfolder/Secret_Picture.jpeg' -H 'Content-Type: application/x-www-form-urlencoded' > Secret_Picture.jpeg
    ```

## Impact

1. The unauthorized attacker can list all files recursively for an unlimited depth, even if explicitly denied by `Files access control` rules.
2. The unauthorized attacker can view the contents of all denied image files up to their maximum resolution. It is up to the attacker to choose the required image resolution (1024 x 768 in the example) and construct corresponding `GET` query through image preview API. Note that it is not even required for the file owner to use web interface and preview the protected image files before the attack. The corresponding image preview files are generated on the server upon the request of the attacker.
3. If the file owner has logged in Nextcloud web interface and browsed the protected files, thus automatically rendering thumbnail previews, it also becomes possible for the attacker to access previews of protected text files with the following `curl` command referencing the text file from the example, choosing 4096x4096 resolution:

    ```
    curl -u user 'https://test.frp.lv/index.php/apps/files/api/v1/thumbnail/4096/4096/Secret_Folder/Secret_Subfolder/Secret_Text.txt' -H 'Content-Type: application/x-www-form-urlencoded' > Secret_Text.png
    ```
The obtained preview image can contain critical information that should have been protected - see example of downloaded preview below:
{F302628}

## Attachments
- WebDAV_SEARCH
- data.xml
- Secret_Text.png
