# Attacker can obtain write access to any federated share/public link

## Report Details
- **Report ID**: 1170024
- **URL**: https://hackerone.com/reports/1170024
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-04-20T20:48:20.362Z
- **Disclosed**: 2021-06-10T13:41:19.545Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi mates,

I stumbled across this with public links. But the same holds true for any federated share. I will try to describe the link scenario.
At first I thought there were more steps (and resharing was involved). But it really is very simples:

1. An attacker obtains a public link (again plenty of those around). For the sake of the attack it is a read only public link
2. The attacker uses the 'add to my nextcloud' functionality to have a federated share created to their own instance
3. The attacker accepts this share
4. Now the attacker checks their database and finds the entry in the `oc_share_external` table.

We are looking for really only the remote id. And the token.
For the sake of this example the `remote id = 2` and the `token = nOxdNJkb1xbI1VX`

5. Now we craft our request

```
curl -v -X POST http://localhost/index.php/ocm/notifications -d '{"notificationType":"RESHARE_CHANGE_PERMISSION","resourceType":"file","providerId":2,"notification":{"sharedSecret":"nOxdNJkb1xbI1VX","permission":["read","write","share"]}}' -H 'Content-type: application/json'
```

To break this down.
We send an (anonymous) POST request to the victims server to be precise to index.php/ocm/notifications
And we pass it the following json

```json
{
   "notificationType":"RESHARE_CHANGE_PERMISSION",
   "resourceType":"file",
   "providerId":2,
   "notification":{
      "sharedSecret":"nOxdNJkb1xbI1VX",
      "permission":[
         "read",
         "write",
         "share"
      ]
   }
}
```

6. The attacker now enjoys their federated share with READ+WRITE+UPDATE+CREATE+SHARE access. (I think it is probably even a bug that there is no way to grant DELETE).


Since we create a federated share at step 1. This also holds true for any created federated share.

## Impact

In short if an attacker has a public link. Or a federated share with them they can elevate their permissions very easily.

This allows them to overwrite files. Add new files. And so on. In short the integrity of all files in public links and federated shares should be considered compromised.

Pardon my directness. But you really should take a serious look at your federation code. As it seems to miss checks all over the place. Maybe recommending everybody to disable it for now is the best course of action.

## Attachments
No attachments
