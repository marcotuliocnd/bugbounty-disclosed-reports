# XSS via /api/v1/chat.postMessage 

## Report Details
- **Report ID**: 219957
- **URL**: https://hackerone.com/reports/219957
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-04-10T15:28:33.860Z
- **Disclosed**: 2024-08-10T22:01:03.393Z

## Reporter
- **Username**: gronke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

**Summary:** An attacker can craft a custom message using the REST API that, once seen by the observer, executes arbitrary code in the context of the client user.

**Description:** According to the API documentation chat messages can have attachments. These attachments then can have fields which contain a title and subtitle for the attachment. When the attachment has an `image_url` assigned, the first field's value can be used to inject HTML tags. For example <img onload=""> can be used to execute arbitrary code. `<` must be the leading character of the field's value property.

## Releases Affected:

  * Client App (OSX)
  * Firefox 48 (Debian)
  * Firefox 52 (OSX)
  * Chrome 58 (OSX)

## Steps To Reproduce (from initial installation to vulnerability):

  1. Create a Channel or get obtain a RoomId of a private conversation
  2. Login to the Rest API
  3. Send crafted message

## Supporting Material/References:

```bash
# Login to get Auth Token and User Id
curl http://127.0.0.1:3000/api/v1/login -d "username=<USER_NAME>&password=<PASSWORD>"

# Send crafted message
curl -H "X-Auth-Token: <USER_TOKEN>" -H "X-User-Id: <USER_ID>" http://127.0.0.1:3000/api/v1/chat.postMessage -d "channel=<CHANNEL_NAME>&attachments[0][image_url]=/assets/logo&attachments[0][fields][0][title]=&attachments[0][fields][0][value]=<img src=/assets/logo width=1 height=1 onload=alert('XSS4') />You're Pwned!"
```

## Suggested mitigation

  * Encode all user inputs to HTML entities


## Attachments
No attachments
