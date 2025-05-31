# Remote Code Execution in the Import Channel function

## Report Details
- **Report ID**: 236607
- **URL**: https://hackerone.com/reports/236607
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-05T15:17:34.888Z
- **Disclosed**: 2018-04-04T16:36:38.276Z

## Reporter
- **Username**: strukt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: expressionengine

## Vulnerability Information
Hello,

Administrators are allow to import channels by visiting http://HOST/PATH_TO_EE/admin.php?/cp/channels/sets and uploading .zip archives that contain the information about the channels to be imported. The archives are then extracted into temporary directories, which are kept in the `/system/user/cache/cset/` directory. The problem is that, if the archive doesn't have all the required files for the import to be successful, the extracted files remain in their folders and an error is thrown to the administrator stating that a file doesn't exist in the archive.

This allows an administrator to upload .php scripts to the server, which is not allowed by default in ExpressionEngine as far as I can see.

###Steps to reproduce:
1- Download the attached .zip archive and browse to http://HOST/PATH_TO_EE/admin.php?/cp/channels/sets
2- Try to upload the zip file you just downloaded as the imported channel
3- Navigate to http://HOST/PATH_TO_EE/system/user/cache/cset/, which will show a directory listing of all the temporary directories, this is a problem by itself
4- If this is your first time trying this, you should find a single directory, click the directory's name and then click the test.php file and edit the URL in the address bar by adding "?cmd=whoami" to the URL
5- Notice that the command has executed and that the information is returned in the page

Regards,

## Attachments
No attachments
