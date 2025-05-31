# Trusted servers exchange can be triggered by attacker

## Report Details
- **Report ID**: 1167853
- **URL**: https://hackerone.com/reports/1167853
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-18T15:55:35.278Z
- **Disclosed**: 2021-06-10T11:44:39.218Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi again,

So this seems to be less bad these days as the trusted servers are no longer enabled by default (however they were some versions ago).
The trusted servers exchanged the full user list with another server. As soon as 1 federated share is created between two instances. It is questionable if this is something that should be allowed by 1 federated share on corporate systems. But maybe this is more of a community feature?

But back to the issue at hand. If trusted servers are enabled.
Then a single public link share can expose the whole system address book to an attacker. To take again the example of cloud.nextcloud.com

1. Assume trusted servers are enabled
2. Pick one of the many public links that circulate
3. Click 'add to your nextcloud' and point it to your own server
4. Accept the federated share
5. wait for the trusted server handshake and exchange
6. Now you have a list of all users on cloud.nextcloud.com

This happens because the federated share is created. And thus the trusted server logic kicks in.

## Impact

If a system has the "Add server automatically once a federated share was created successfully" enabled.
Then if there is a public link circulating an attacker can obtain the shared info from all users on the system

This can contain

* username
* displayname
* email
* federated cloud id

Possibly more but I did not check.

If this is part of the expected behavior. Then I feel this should be communicated a lot more clear when an admin tries to enable this.

## Attachments
No attachments
