# Cleartext Transmission of Sensitive Information Leads to administrator access

## Report Details
- **Report ID**: 813159
- **URL**: https://hackerone.com/reports/813159
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-08T13:50:33.121Z
- **Disclosed**: 2020-05-30T10:51:13.632Z

## Reporter
- **Username**: kdr9666
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: helium

## Vulnerability Information
The weakness of the program is Cleartext Transmission of Sensitive Information through URL Leads to administrator access. This program is having one feature like we can add users like administrator and read-only, these are roles, into organizations. Here I get the administrator role at same organization by removing the original user id.

Vulnerable URL:  https%3A%2F%2Fconsole.helium.com%2Fusers

Steps to Reproduce:
1. After creating the account for your organization, go to the Users tab and here you can see your organization name on the top, now try to add a user by using the mail id with the role of the administration.
2. Then the opposite user will receive the invitation link from the first user, Click on the invitation link it will take you into the registration page of Console.helium.com, but here thing is, just go to URL of current page here you can see the organization name, inviter id and also invite receiver id and change the mail id of receiver and click on enter.
3. Now, you able to see the registration page again with different mail id in the field of the username and create a password for this id and click on the Register button.
4. Now, this last mail id will receive a confirmation link to complete the registration process, for this go to the mailbox and click on the link and after trying to log in.
5. After a successful login to the account, you can see the organization name of the inviter. Now you are also one the administrator of this organization.
6. To confirm this, go to a first user account who invited into the administrator role, here you can able see the mail id of the last user instead of the real one.
7. Yes… we have successfully done it.

## Impact

Full administrator account take over.


Severity:
Critical

## Attachments
- Pic1.png
- Pic2.png
- Pic3.png
- Pic4.png
- Pic5.png
- Pic6.png
- Pic7.png
- Pic8.png
- Pic9.png
- Pic10.png
- Pic11.png
- HELIUM.mp4
