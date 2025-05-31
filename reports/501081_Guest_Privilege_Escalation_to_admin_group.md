# Guest Privilege Escalation to admin group

## Report Details
- **Report ID**: 501081
- **URL**: https://hackerone.com/reports/501081
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-02-25T14:47:03.826Z
- **Disclosed**: 2024-08-10T22:00:09.452Z

## Reporter
- **Username**: gronke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
Due to improper ACLs it was found possible to escalate privileges from a guest user to admin.

As first step the guest user adds itself to the `bot` group that holds the `manage-own-integrations` permission. With this permission it is possible to create a custom Integration with a script that, if triggered, adds the user to the `admin` group.

The `insertOrUpdateUser` method improperly validates a users permissions to change its groups. Because an explicit check prevents from adding itself to the `admin` group directly, the privileges of the `bot` group need to be used to further escalate to global admin.

## Releases Affected:

  * [develop@5f0180d](https://github.com/RocketChat/Rocket.Chat/commit/5f0180dc1500b4e37b8320b39869babadb5d01cd)

## Steps To Reproduce (from initial installation to vulnerability):

(Add details for how we can reproduce the issue)

  1. Login Guest user
  2. Determine own users `_id` from browser traffic
  3. Escalate to `bot` group
  4. Create malicious Integration script
  5. Trigger Integration

## Supporting Material/References:

### Bot group privilege escalation
```json
["{\"msg\":\"method\",\"method\":\"insertOrUpdateUser\",\"params\":[{\"_id\": \"<USER_ID>\", \"roles\": [\"user\", \"bot\"]}],\"id\":\"17\"}"]
```

### Malicious Integrations Script
```javascript
this.Roles.addUserRoles("9HN4Brdmo2Qc2wsiX", "admin")
class Script {
  process_incoming_request({ request }) {};
}
```

## Suggested mitigation

  * Only allow administrators to modify user groups
  * Isolate Integration script context from server application

## Impact

Guest users can become server administrator.

## Attachments
No attachments
