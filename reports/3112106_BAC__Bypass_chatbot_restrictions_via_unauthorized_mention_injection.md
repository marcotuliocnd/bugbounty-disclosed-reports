# BAC – Bypass chatbot restrictions via unauthorized mention injection

## Report Details
- **Report ID**: 3112106
- **URL**: https://hackerone.com/reports/3112106
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-04-25T08:45:06.524Z
- **Disclosed**: 2025-05-06T14:24:05.516Z

## Reporter
- **Username**: yoyomiski
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: dust

## Vulnerability Information
## Summary:
- A member user who is not authorized to use the Gemini chatbot can still send and receive messages from this chatbot by manually editing the request and changing the ```mention``` and ```configurationId```. This bypasses the permission control from the Admin side, leading to abuse of the chatbot beyond the scope of permission.
- Similar to other chatbots, if disabled, members can still use it.

## Steps To Reproduce:
1. Login admin (████████)
2. Go to “Manage Agents”Verify. That the **Gemini agent is disabled** or not available
{F4285482}
3. Now go back to  the member account (█████). we make a new chat . When chatting nomally. we select “which agent would you like to chat with?”
{F4285485}
4. In the step, turn on Burp and capture the request, we capture the request with API:
```POST /api/w/BSsJ1zPUYE/assistant/conversations/PdBk9DSYXA/messages/UyXjPLmW5j/edit```
{F4285487}
5. This request is passed to mention, we change mention and configurationId to gemini's ```gemini-pro``` and forward the request, the result is that we can chat with chatbot ```gemini``` even though the admin does not grant us permission to chat with this chatbot
```{"content":":mention[gemini-pro]{sId=gemini-pro} how are you?","mentions":[{"type":"agent","configurationId":"gemini-pro"}]}```
{F4285490}

Response:
{F4285491}
{F4285493}
{F4285494}

##HTTP header:
```
POST /api/w/BSsJ1zPUYE/assistant/conversations/PdBk9DSYXA/messages/UyXjPLmW5j/edit HTTP/2
Host: eu.dust.tt
Cookie: …
Content-Length: 124
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US,en;q=0.9
Sec-Ch-Ua: "Chromium";v="135", "Not-A.Brand";v="8"
Content-Type: application/json
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36
Accept: */*
Origin: [https://eu.dust.tt](https://eu.dust.tt/)
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://eu.dust.tt/w/BSsJ1zPUYE/assistant/PdBk9DSYXA
Accept-Encoding: gzip, deflate, br
Priority: u=1, i

{"content":":mention[gemini-pro]{sId=gemini-pro} how are you?","mentions":[{"type":"agent","configurationId":"gemini-pro"}]}
```

## Impact

- Member users are not granted permissions, but can still use Gemini chatbot by editing requests → Clear violation of authorization policy

## Attachments
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
