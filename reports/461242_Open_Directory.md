# Open Directory

## Report Details
- **Report ID**: 461242
- **URL**: https://hackerone.com/reports/461242
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-12-12T13:24:14.576Z
- **Disclosed**: 2018-12-24T10:17:36.375Z

## Reporter
- **Username**: wasjerry
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ratelimited

## Vulnerability Information
**Summary:** A misconfigured server can show a directory listing, which could potentially yield sensitive information to an attacker. 

**Solution** :     
1.  Disable directory listings in the web- or application-server configuration by default.
2. Restrict access to unnecessary directories and files.
3. Create an index (default) file for each directory.

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. go to ratelimited.me
  2. right click on and image and open it
  3.  go to this url https://ratelimited.me/assets/
  4. Click on parent directory
  5. now you can access all the folders shown


Some Examples :
1. https://ratelimited.me/assets/sass/material-kit/sections/
2. https://ratelimited.me/assets/sass/material-kit/plugins/
3. https://ratelimited.me/assets/js/
4. https://ratelimited.me/assets/css/

## Impact

A directory listing provides an attacker with the complete index of all the resources located inside of the directory. The specific risks and consequences vary depending on which files are listed and accessible.

## Attachments
- OpenDirectoryRATELIMITED1.png
