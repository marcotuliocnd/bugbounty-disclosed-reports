# Session fixation on public talk links

## Report Details
- **Report ID**: 1181962
- **URL**: https://hackerone.com/reports/1181962
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-01T14:18:01.836Z
- **Disclosed**: 2021-06-16T08:40:00.261Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
1. userA shares a talk room and protects it with a password
2. userB opens links but doesn't enter the password yet
3. Attacker steals the cookies from userB
4. userB logs in
5. attacker is now also able to read the conversation etc

## Impact

In short the attacker is able to take over the session of the guest userB on this talk room.

The session id should be renewed once the password is entered.

## Attachments
No attachments
