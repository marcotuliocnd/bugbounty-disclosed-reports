# User Editable nextcloud Wiki pages of Public Repositories

## Report Details
- **Report ID**: 498878
- **URL**: https://hackerone.com/reports/498878
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-02-20T22:00:44.232Z
- **Disclosed**: 2019-08-31T12:32:06.581Z

## Reporter
- **Username**: chernobyl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
###Summary :
I have found that the "Edit" Permissions of WIKI pages are NOT disabled on the public repositories of nextcloud. Generally Edit permissions are given only to the collaborators of a specific repository. but that is not the case with Nextcloud, It is public editable which isn't right in terms of security. 

An attacker can create a new Wiki page for this particular nextcloud Github Wiki page : There is no restriction on it.


https://github.com/nextcloud/logreader/wiki

An attacker could include any content/links and direct users to other similar nextcloud pages to steal user information. 
Attacker could even provide false information about the user to provide their private keys or passwords using a form/page.

## Impact

These wikis should not be publicly editable due to the possibility of abuse through hacktivities such as Phishing, Defacement, etc

Many companies (even on hackerone) are correcting this issue and removing the "Edit" Permissions to the wiki page of public repositories.

## Attachments
No attachments
