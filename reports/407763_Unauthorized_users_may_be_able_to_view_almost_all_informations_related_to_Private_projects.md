# Unauthorized users may be able to view almost all informations related to Private projects.

## Report Details
- **Report ID**: 407763
- **URL**: https://hackerone.com/reports/407763
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-09-09T16:40:04.208Z
- **Disclosed**: 2018-12-03T22:15:29.740Z

## Reporter
- **Username**: 8ayac
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
**Summary:**
On the most of pages related to Private projects, cache control is inadequate, so the contents of Private projects may leak to unauthorized users.

**Description:**
For visibility of projects, you can select `Public`, `Internal`, and `Private`.
Among them, Private projects can only be viewed from project members. (In other words, it can not be viewed by who are not project members.)
In also [GitLab Documentation](https://docs.gitlab.com/ee/public_access/public_access.html), it is mentioned as follows:
> Private projects can only be cloned and viewed by project members, ...

However, due to inadequate cache control on the most of pages related to Private projects, an attacker may view these contents using the 'Back' button in browser.
In addition, users without logging in can also exploit this problem.

Note: This issue supports all modern browsers.

## Steps To Reproduce:
1. Sign in to GitLab.
2. Click the "[+]" icon.
3. Click "New Project".
4. Fill out "Project name" form with "PoC".
5. Check the check box of "Private".
6. Click "Create project" button.
7. Sign out from Gitlab.
8. Hit the "Back" button in browser.

Result: The content of the private project "PoC" is displayed without logging in.

## Impact

This issue leads to information leakage.
Cache control is inadequate on the most pages related to Private projects.
Therefore, almost all contents of Private project may leak.

Although the exploitation needs physical access to the victim's PC, It is not very difficult to access someone's PC in the following scenes:
- Office scenario
- Laptop case

The examples of critical information that may leak are as follows:
- List of file names
- Source code
- Commit log
- Issues
- Contents of the wiki

Note: The official document specifies that they will not be viewed by unauthorized users.

## Attachments
No attachments
