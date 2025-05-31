# Endpoint Redirects to Admin Page and Provides Admin role

## Report Details
- **Report ID**: 1991290
- **URL**: https://hackerone.com/reports/1991290
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2023-05-18T00:11:05.535Z
- **Disclosed**: 2024-07-19T14:43:23.062Z

## Reporter
- **Username**: bulldawg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
By navigating to https://████████.mil/apexcrrel/f?p=165:56, the user will automatically be redirected to the web application admin portal with Admin access.

**Description:**
There is a web application running at the following URL:

https://█████.mil/apexcrrel/f?p=165:1::::::

████

For context, this is a web application running on a Oracle Apex Express platform. The '165' in the 'p' parameter in the URL is a unique identifier for the web application. The '1' following the '165' represents the page that the user is viewing. 

The page '56' can be used to automatically obtain administrator access to this application. 

Here we can see that we can't access the 45th page (https://████.mil/apexcrrel/f?p=165:45) because we are not an Admin.

███████

However, navigating to the 56th page (https://██████████.mil/apexcrrel/f?p=165:56) automatically redirects to the 45th page but provides a valid admin session. 

█████████

We can also see that we have the ability to manage users, including admin users.

██████████

As a note, I found this due to the application at https://████.mil/apexcrrel/f?p=164:5::::::
This is a separate web application, given that the unique identifier is now 164. 

On this page there is a 'Go To Admin' button. When clicking this, it calls the /apexcrrel/DISDI_PORTAL_DEV.login_admin endpoint. This redirects the user to the 56th page, breaking the access control and providing Admin access.

███████

## Impact

This is a critical severity bug that impacts confidentiality, integrity, and availability. 

Confidentiality: An attacker can obtain first names, last names, email addresses, and filenames of uploaded files.
Integrity: An attacker can upload files, edit documents, and edit user roles
Availability: An attacker could remove all users, including admins, making it difficult for users to use the application.

## System Host(s)
█████.mil

## Affected Product(s) and Version(s)
Oracle Apex Express

## CVE Numbers


## Steps to Reproduce
1. To verify that you do not have any valid sessions to view the admin pages, visit https://██████.mil/apexcrrel/f?p=165:45
2. Now, navigate to https://█████████.mil/apexcrrel/f?p=165:56
3. You now have admin access to the application.

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
