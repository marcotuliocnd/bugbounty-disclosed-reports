# Email Takeover leads to permanent account deletion

## Report Details
- **Report ID**: 2587953
- **URL**: https://hackerone.com/reports/2587953
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-07-06T12:38:35.355Z
- **Disclosed**: 2024-07-19T14:40:22.210Z

## Reporter
- **Username**: prakhar0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hii Triager,

**NOTE: Just to clarify, I reported a similar issue yesterday, but it was on a different endpoint. _In this report, the vulnerable domain is the same, but the endpoint is different._**

I found that an attacker can change their email address to the victim's(existing user) email, which then leads to permanent account deletion of the victim's account.

User-A: Attacker
User-B: Victim

Both User-A & User-B are registered user & have their separate accounts on `https://www.██████████/852585B6003EBA25/CreateAccount.html`

## Impact

- Possible Account Takeover (Probably)
- Permanent Account Deletion
- Improper Authentication on change email functionality.

## System Host(s)
www.█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1 - Login to Attacker's account, User-A (`attacker@email.com`)
2 - Login to Victim's Account, User-B (`victim@email.com`)
3 - In the Attacker's account, Navigate to the `Change Your Email Address` section.
4- Change the **Attacker's email** to **`victim@email.com`**. You can successfully take over the victim's email. (probably victim account)
5 - Now, Try to login as victim account(with victim email & password) , Application will Return Invalid Credentials

 - This is the indication of an **Email Takeover of the victim's account**

6 - Now, Navigate to the Attacker's account & change the email back to `attacker@email.com`
7 - Navigate to the Registration page, Enter the victim's email `victim@email.com` & click `Check Availability`. You'll see that the victim's email is deleted from the DB & available for a new account.

- This is the indication of **Permanent deletion of the Victim's account. **

## Video PoC

████

## Suggested Mitigation/Remediation Actions
- Set proper authentication on the Update Profile functionality.



## Attachments
No attachments
