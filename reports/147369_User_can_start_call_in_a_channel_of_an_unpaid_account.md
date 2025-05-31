# User can start call in a channel of an unpaid account

## Report Details
- **Report ID**: 147369
- **URL**: https://hackerone.com/reports/147369
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-26T03:32:17.371Z
- **Disclosed**: 2016-09-15T02:05:21.679Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
Found a super minor issue that allows a user to start a call in a channel of an unpaid account. Besides the minor financial incentive for an attacker, this doesn't have a super high impact. Wanted to let you know anyway since it's not possible through the UI by default. To reproce it, start by signing in to a user that is part of an unpaid account and start intercepting your network traffic (I used Burp Suite).

 - Go to a channel, in the top bar, you'll see that the Call feature is not available.

{F101678}

 - Go to a private chat window of another user
 - Intercept your network traffic and click the "Call" button in the top bar. The first request will be to https://account.slack.com/call/ID. Forward this request.
 - The next request will look like this:

```
POST /api/screenhero.rooms.create?_x_id=<ID> HTTP/1.1
Host: account.slack.com
...

------WebKitFormBoundaryoqDvFcsV6Y4A1ByJ
Content-Disposition: form-data; name="regions"

west|east|ap|eu
------WebKitFormBoundaryoqDvFcsV6Y4A1ByJ
Content-Disposition: form-data; name="protocol"

1.0
------WebKitFormBoundaryoqDvFcsV6Y4A1ByJ
Content-Disposition: form-data; name="channel"

D1CCM92P5
------WebKitFormBoundaryoqDvFcsV6Y4A1ByJ
Content-Disposition: form-data; name="token"

<SLACK API TOKEN>
------WebKitFormBoundaryoqDvFcsV6Y4A1ByJ--
```

 - Change the `channel` value to the ID of the a channel. This ID can be obtained by clicking on a channel in the left column and copy it from the WebSocket data being sent to Slack. Now forward the requests and stop intercepting traffic.
 - The call will be posted in the channel:

{F101676}

## Attachments
- call-in-channel.png
- call-not-available.png
