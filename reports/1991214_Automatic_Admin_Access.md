# Automatic Admin Access

## Report Details
- **Report ID**: 1991214
- **URL**: https://hackerone.com/reports/1991214
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2023-05-17T20:38:38.340Z
- **Disclosed**: 2024-07-19T14:44:14.917Z

## Reporter
- **Username**: bulldawg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
URL: https://█████████.mil/apexcrrel/f?p=150:1:23467499301323::NO:::

When visiting the following URL, the user is automatically signed into a user with administrative access. 

███

This user is allowed to:
1. Create new submissions, allowing file uploads

████████

2. See all submissions going back to 2012

██████████

3. Manage users - add, delete, and link users. This user could also add the Administrator role to a user. 

███

████

4. Send spam emails to all users

█████████

5. Access admin tools like publishing data and removing publications

██████████

I did not test all functionality provided by this access as I did not want to damage the integrity of the data on the web application.

Please let me know if you would like me to test adding/deleting users, creating submissions and testing file upload vulnerabilities, etc. This would also allow me to demonstrate the severity of this vulnerability as well as find new vulnerabilities in the application. For example, with permission I would like to test the file upload functionality for vulnerabilities.

## Impact

This is a critical vulnerability. This impacts the integrity, confidentiality, and availability of the application. 

Integrity: Unauthorized users can upload arbitrary data, publish data, and delete publications.
Confidentiality: This exposes names, emails, and submissions.
Availability: This administrative user can delete other user accounts, denying them access.

## System Host(s)
███████.mil

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Visiting URL: https://███.mil/apexcrrel/f?p=150:24:23467499301323::NO:::
2. View active user in top right corner: "ben auto log user". This user is an administrator.

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
