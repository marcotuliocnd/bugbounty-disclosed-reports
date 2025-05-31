# Restrict any user from Login to their account

## Report Details
- **Report ID**: 2586616
- **URL**: https://hackerone.com/reports/2586616
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-07-04T17:06:48.432Z
- **Disclosed**: 2024-07-19T14:39:12.204Z

## Reporter
- **Username**: prakhar0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hii Triager,

I found that an attacker can change their email address to the victim's(existing user) email and restrict the victim from accessing their account.

Vulnerable Domain: `www.██████████.mil`

User-A: Attacker
User-B: Victim 

Both User-A & User-B are registered user & have their separate accounts on `www.███.mil`

## Step To Reproduce
1 - Login to Attacker's account, User-A (attacker@email.com)
2 - Login to Victim's Account, User-B (victim@email.com)
3 - In the Attacker's account, Navigate to `Update Profile`  section.
4- Change the Attacker's email to `victim@email.com`. You can successfully takeover the victim email. (not victim account)
5 - Now, Try to login as victim account(with victim email & password) , Application will Return `Invalid Credentials`

## References
████

## Impact

1 -Restric any user from accessing their account.
2 - Improper Authentication on change email fuctionality.

## System Host(s)
www.██████.mil

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1 - Login to Attacker's account, User-A (attacker@email.com)
2 - Login to Victim's Account, User-B (victim@email.com)
3 - In the Attacker's account, Navigate to `Update Profile`  section.
4- Change the Attacker's email to `victim@email.com`. You can successfully takeover the victim email. (not victim account)
5 - Now, Try to login as victim account(with victim email & password) , Application will Return `Invalid Credentials`

## Suggested Mitigation/Remediation Actions
1 - Set proper authentication on the `Update Profile` functionality



## Attachments
No attachments
