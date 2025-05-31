# Unexpected federated shares added via public link

## Report Details
- **Report ID**: 1167767
- **URL**: https://hackerone.com/reports/1167767
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-18T13:00:13.710Z
- **Disclosed**: 2021-04-26T15:55:55.138Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
So I'm not 100% sure if this is an security issue or not. But it is in my opinion at least unexpected and could be handled better to make sure people trust the system.

1. Get a public link share (again plenty of those around)
2. Click the 'add to your Nextcloud'
3. A federated share is added/created

However now the owner of the public link at 1 has a new federated share added.
Without any idea where it comes from. Which would be reason for concern in my book. Esp for people that do not know about the functionality etc.

## Impact

Missing descriptions or notifications can limit the trust in the system. Esp for regular users without technical knowledge on how things work.
I'd expect a notification. Or at the very least a description in the sharing tab (? is that the correct name?) for the federated share 'mounted from public link X'

## Attachments
No attachments
