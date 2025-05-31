# File drop public link can also be converted to federated share

## Report Details
- **Report ID**: 1167929
- **URL**: https://hackerone.com/reports/1167929
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-04-18T18:45:03.415Z
- **Disclosed**: 2021-06-10T13:41:49.547Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
So bear with me. Because this one requires some user interaction and makes some assumptions.

1. victim creates a files drop public link
2. attacker has that link
3. the 'add to your nextcloud is hidden' but if you manually craft the request and send it a federated share will still be created.

for example

curl 'https://localhost/apps/federatedfilesharing/createFederatedShare' -X POST -d 'shareWith=user2%40https%3A%2F%2Flocalhost&token=KP3wSTdNbxsLGnq'

4. victim checks their shares for this folder
5. victim sees the federated share and checks the permission and sees the create permission, freaks out because they didn't want to give anybody that besides the file drop. 
6. Now the share is updated, create permissions are gone but read permissions are granted

So this is kind of a long short. But there is just so much happening that a user without any knowledge of the system can freak out or just mess up.
At step 3 the API should error out and just refuse to create the federated share. To make sure no confusion can occur.

## Impact

In the worst case making a share readable when it never was.
However as stated that is unlikely. But it should be considered and handled graceful as this is actually easy to prevent by a simple check before creating the federated share.

## Attachments
No attachments
