# Talk discloses turn server to anybody

## Report Details
- **Report ID**: 1195593
- **URL**: https://hackerone.com/reports/1195593
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-13T13:16:08.844Z
- **Disclosed**: 2021-05-26T10:52:32.962Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
The attack is straight forward.

1. send a request to

```bash
curl -H 'OCS-APIREQUEST: true' https://server/ocs/v2.php/apps/spreed/api/v2/signaling/settings
```

And you get back a lot of information.

* signaling server
* stun server
* turn server (inc credentials)

The stun server is harmless enough. I did not look at the signaling server.
However the Turn server (esp inc credentials). Can be used by the attacker to proxy their web traffic trough.
Esp in combination with your docs: https://github.com/nextcloud/spreed/blob/master/docs/TURN.md

This would allow the access internal network on the turn server.

## Impact

Anybody (they do not even have to have a valid talk room) can request the turn server credentials of a Nextcloud server running Talk.
In combination with your guides on how to set those things up this can result in dangerous situations.

I would furthermore advise to as a start only hand out turn credentials to guests that at least have access to a room.
And to improve the documentation.

## Attachments
No attachments
