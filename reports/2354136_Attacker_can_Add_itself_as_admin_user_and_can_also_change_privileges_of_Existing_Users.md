# Attacker can Add itself as admin user and can also change privileges of Existing Users [█████████]

## Report Details
- **Report ID**: 2354136
- **URL**: https://hackerone.com/reports/2354136
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-02-04T10:04:12.901Z
- **Disclosed**: 2024-03-22T17:43:14.390Z

## Reporter
- **Username**: dishant_singh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi there,
i have found a vulnerability on you [domain](████). After directory bruteforcing i found an directory without having any kind of protection and authentication. so an attacker can add new user to the site As **Admin** and an attacker can also change privilege of the users without any authentication. for further read steps to reproducue.

## Impact

The attacker can add itself as admin user and can also change user privileges without any authentication. this can lead to huge impact the entire site can be compromised.

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Visit ████████:1:0:::::  you will see the website is asking to login 
2. Now change the **1 to 9** or directly visit this [url](██████████:::::).
3. Navigate to `Add New User`
4. enter email  address, First name, Last name and choose agency to Non-Agency.
5. Click on `add new user`
6. check mail inbox you will recieve the username and password for the admin account you just created. 
7. Login with the creds you just got in you email.



**NOTE: I CREATED 2 ACCOUNTS WHILE TESTING THIS ISSUE I HAVE PROVIED CREDS FOR THE BOTH ACCOUNT IN POC MAKE SURE TO CHECK THEM AS WELL**

## Suggested Mitigation/Remediation Actions
the website should have proper authentication for the url ████████::::: so that can any unauthorized user cannot add user or change the privileges of the existing users.



## Attachments
No attachments
