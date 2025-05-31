# Filename and directory enumeration

## Report Details
- **Report ID**: 149273
- **URL**: https://hackerone.com/reports/149273
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-05T05:37:57.738Z
- **Disclosed**: 2016-08-08T02:42:35.248Z

## Reporter
- **Username**: strukt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: expressionengine

## Vulnerability Information
Hello,

The "Import File Converter" can be abused by an admin to map the server directories and files, because the "File location" field doesn't sanitize the user input and allows access to root directories and files.

## Steps to reproduce:
1- Go to http://localhost/ee/admin.php?/cp/utilities/import_converter
2- Set the "File location" to `///etc/`, notice that the error "You must have at least 3 fields: username, screen_name, and email address", proving that the file exists.
3- Try with `///strukt/`, notice the different error message, now it says "The path you submitted is not valid.", meaning the directory doesn't exist.
3- Now try with `///etc/passwd`, the first error message shows up.
4- Finally, try with `///etc/strukt`, the second message appears.

## More successful test cases:
`///etc/hosts`
`///usr/`
`///var/`
`../../../../../../../../etc/passwd`

Regards

## Attachments
No attachments
