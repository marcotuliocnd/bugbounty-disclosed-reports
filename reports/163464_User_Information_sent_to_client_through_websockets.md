# User Information sent to client through websockets

## Report Details
- **Report ID**: 163464
- **URL**: https://hackerone.com/reports/163464
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-26T02:16:20.127Z
- **Disclosed**: 2016-09-12T18:47:42.285Z

## Reporter
- **Username**: cablej
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hey,

I noticed when monitoring the websocket requests that the account information of many users, including email address, is sent to the client. For example:

```
██████

██████████

█████████

████████

███████

```

There's hundreds of these requests, each containing user information. Please let me know if this is meant to be happening, but I didn't see a list of users on the site.

## Attachments
No attachments
