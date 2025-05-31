# cross site web socket hijacking

## Report Details
- **Report ID**: 274324
- **URL**: https://hackerone.com/reports/274324
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-10-04T10:47:08.858Z
- **Disclosed**: 2017-10-11T00:20:00.655Z

## Reporter
- **Username**: bb97a5545a1c33015200e2b
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
In the below web-socket request successful 101 protocol handshake is working with the origin:https://app.legalrobot.com, but if you place the malicious origin in the place of https://thisdata.com which is http://evil.com or any page containing the malware, the web socket server is still giving 101 protocol successful handshake which means that we socket server is not checking origin headers while opening the connection which may lead to cross site web socket hijacking.

1. Open https://app.legalrobot.com
2. Intercept the websocket request with burpsuite like i've intercepted and send it to repeater

GET /sockjs/431/bcbqwec5/websocket HTTP/1.1
Host: app.legalrobot.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Sec-WebSocket-Version: 13
Origin: https://app.legalrobot.com
Sec-WebSocket-Extensions: permessage-deflate
Sec-WebSocket-Key: jrJn6D4ddqaeGfrLMxQdow==
Cookie: __cfduid=d3446c9cf6346287bf143c4d82a4843e81506572367; _ga=GA1.2.1754317931.1506572375; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%22d0db4012-5f13-4ef4-b25e-ea87340bddb9%22; intercom-id-nmyyq5i5=6ee58969-0370-4131-bae3-3f15c320ca9d; _gat=1; galaxy-sticky=!fqm5S7o42sAL2eD8T-zkg1n; _gid=GA1.2.930494122.1507113142
Connection: keep-alive, Upgrade
Pragma: no-cache
Cache-Control: no-cache
Upgrade: websocket

3. Now change the origin (from https://app.legalrobot.com) and replace it (to https://evil.com) with
maliious origin.
4. The web socket server is still giving successfull 101 handshake which means web socket server is not verifying the origin while opening the connection.

Both of the request i've attached below.
Thank you.


## Attachments
- 1.JPG
- 2.JPG
