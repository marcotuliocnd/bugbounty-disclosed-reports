# Improper access control to messages of Social app

## Report Details
- **Report ID**: 921717
- **URL**: https://hackerone.com/reports/921717
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-12T22:16:43.535Z
- **Disclosed**: 2020-11-17T16:36:32.453Z

## Reporter
- **Username**: sanktjodel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The Social App (https://apps.nextcloud.com/apps/social) lacks access controls in the `displayPost` function (`/@{username}/{token}`) allowing an unauthenticated user to view any message content by knowing or guessing the message ID.

The vulnerable code is at https://github.com/nextcloud/social/blob/97fb063479d4c0ad6fccdea3774601a619f8a886/lib/Controller/ActivityPubController.php#L367.
Note the TODO comment and the lack of authentication and authorization checks.

The following is a sample curl request to access a direct (private) message (replace the host, username, and the token value):

```
curl -X 'GET' -H 'Accept: application/activity+json' 'http://{nextcloudHost}/apps/social/@{username}/{token}'|jq
```

The `token` value consists of digits only and is based on the unix time.
An attacker would have to know or guess (e.g. brute force) this message ID.

## Impact

An unauthenticated attacker can view any social message, including private (direct) messages from one user to another.
The attacker would have to know or guess the token value.

## Attachments
No attachments
