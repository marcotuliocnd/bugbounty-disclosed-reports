# Federated shares are not password protected

## Report Details
- **Report ID**: 1167817
- **URL**: https://hackerone.com/reports/1167817
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-18T14:46:50.707Z
- **Disclosed**: 2021-06-16T08:56:05.539Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi again,

So more from me.
Bare with me because this is a highly theoretical issue. But I never the less thing it should be mitigated. Or at least disclosed.

Premissie:
1. user1 on serverA has a federated share established with user2 on serverB
2. the database (not the full system) of serverB is compromised

Now since federated shares are not created with a password which is stored encrypted in the database this means that an attacker to serverB obtains access to data on serverA directly.

Now I am aware that if serverB is fully compromised the password could also be decrypted using the server secret

## Impact

Using federated sharing exposes the servers to a much larger attack service currently. Since an attacker on a different system can obtain access to data on your system as well. In some cases easier than to the target system.

I'd recommend to make sure that there is a password set that is stored encrypted. And that there is a way for admins to obtain a list of federated servers they need to notify in case they had a breach of their own system.

## Attachments
No attachments
