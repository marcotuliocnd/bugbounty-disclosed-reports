# Cross Site WebSocket Hijacking

## Report Details
- **Report ID**: 211283
- **URL**: https://hackerone.com/reports/211283
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-07T07:55:45.004Z
- **Disclosed**: 2017-10-16T07:07:08.356Z

## Reporter
- **Username**: aishu_kc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
### Description:
The given URL fails to validate Origin header- leading to Cross-Site WebSocket Hijacking. 

### Impact:
The impact, however, depends on how the server is configured. For example, it might require an authentication token which are user specific. In such cases, it might not be as sever as it would be in cases where server doesn't require anything at all.  
Since almost all the request in the site are performed in web socket, it might be possible to hijack the websocket. The impact would be similar to side-wise CSRF plus every response from server could be possible to be read by attacker.

### Affected Domain: 
app.legalrobot.com/socketjs/444/jfalksf/websocket

### Reference: 
https://www.christian-schneider.net/CrossSiteWebSocketHijacking.html
https://www.notsosecure.com/how-cross-site-websocket-hijacking-could-lead-to-full-session-compromise/

## Attachments
No attachments
