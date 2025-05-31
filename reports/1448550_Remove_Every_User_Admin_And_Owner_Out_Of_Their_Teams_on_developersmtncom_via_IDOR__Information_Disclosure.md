# Remove Every User, Admin, And Owner Out Of Their Teams on developers.mtn.com via IDOR + Information Disclosure

## Report Details
- **Report ID**: 1448550
- **URL**: https://hackerone.com/reports/1448550
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-01-13T06:01:56.649Z
- **Disclosed**: 2022-12-01T17:34:30.586Z

## Reporter
- **Username**: wallotry
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
Hello world,

This vulnerability is too involved with regular users, in order for us to prevent any damage, we need 3 different user accounts we own. 
This gives us specific "user_id" and "team_id" to work with.
There's an Information Disclosure as a side effect of this vulnerability. User and team names are disclosed in the response from the server.

## Steps To Reproduce(POC)

==First, let's paint a mental picture of this vulnerability and the required conditions using accounts with imaginary user_id & team_id.
The vulnerability and conditions are realistic, the only imaginary thing is the user_id and team_id.==

 1. Create 3 accounts on developers.mtn.com(Account A, B, and C)

==My imaginary accounts:==
- A: First Account(imaginary user_id=1111 & team_id=0001)
- B: Second Account(imaginary user_id=1112 & team_id=0002)
- C: Third Account(imaginary user_id=1113 & team_id=0003)
 2. Login to A, Invite B to your Team A
 3. Login to B, Invite C to your team B
 4. Open Burp Suite
 5. Login to A, Remove B(Please Intercept This Request)
 6. Send the Intercepted request to the repeater tab
 7. Modify the request(Our Goal is to remove C from Team B, which we don't have access or permissions to.)
 8. Replace the team_id with Team B's team_id. Replace the user_id with C's user_id.
 9. Send the Request. (This Request will disclose C's username And Team B's name. Making this an information disclosure. PII)

{F1577574}

 10. C will be removed from B's Team B.
 11. C will receive an email from MTN telling him/her that he/she has been removed from Team B.

{F1577544}

## Steps To Reproduce(Removing Every User)

==This can be done with a custom script/code without the need for Burp Suite==
 1. Intercept the request for removing a user, and send it to the Burp Suite intercept tab.
 2. Config your settings to brute-force through every team_id and user_id. This part is not that hard because every user_id and team_id has only 4 digits.
 3. Run the intruder request. When there's a successful user_id and team_id match, the user whose ID has been matched, will be removed.
 4. If my calculations are correct, it should take 12 Hours to remove every user from every group they're in, the maximum being 20 Hours. The faster the internet speed, the faster the computer, the shorter the time it'll take to brute-force through every user_id and team_id.

## Exploitability
- Anyone with an account on developers.mtn.com can exploit this vulnerability
- All you need is a user_id and a team_id to remove a user from his/her team.(Their privileges don't matter, even the owner is vulnerable)

## Remediation
- Ensure proper session management and object-level user access control checks.
- Apply access control mechanisms such as permissions to certain action.
- Validation of access to a team_id.
- You should always check if a user submitting the request isn't tampering and isn't submitting any ID's that do not belong to his/her account.

## Reference
#1448475

## Impact

A low level user can remove his Admin and Owner from the team.
Every user will be removed from every team they are in, including owners and admins.

## Attachments
- removed_email.png
- IDOR___Disclosure.mp4
