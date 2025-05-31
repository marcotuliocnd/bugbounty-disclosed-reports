# Privilege Persistence via Cloned Agent

## Report Details
- **Report ID**: 3114554
- **URL**: https://hackerone.com/reports/3114554
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-04-27T13:35:59.591Z
- **Disclosed**: 2025-04-30T07:07:43.110Z

## Reporter
- **Username**: yoyomiski
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: dust

## Vulnerability Information
##Summary:
Hi, I found a new problem. It allows a member to create an agent based on the sid of an agent that the admin manages. Specifically, in this issue, I describe gemini-pro. This is similar to chatbots like o3-mini, gpt-4, etc.

##Scenario: 
Suppose the admin manages agents through the dashboard. The admin allows a member to use the agent gemini-pro for 10 minutes (just as an example). However, by changing the sid, the member can clone gemini-pro. At this point, even if the admin disables gemini-pro, the member still has a cloned version of gemini-pro.

##Steps to reproduce:
1. Access the admin account `█████████` and change the agent `gemini-pro` from `disabled` to `enabled`.
{F4291432} 
change
 {F4291433}

2. Now access the member account `████████` and create a new agent. The image below shows that I have created a new agent.
{F4291440}
{F4291441}
3. Edit this new agent, and change the `sid` to the sid of gemini-pro, which is: `gemini-pro`.
`PATCH /api/w/BSsJ1zPUYE/assistant/agent_configurations/JpY5xizXRo`
{F4291446}
-----
PATCH /api/w/BSsJ1zPUYE/assistant/agent_configurations/gemini-pro
{F4291449}
4. `Disable` gemini-pro on admin
{F4291450}
5. Now, we have successfully cloned gemini-pro. Although the admin `disables gemini-pro`, we can still use this cloned agent to call gemini-pro.
{F4291454}
{F4291456}

Note: Now i cant even delete this agent on member account ::v

## Impact

- Admin thinks he has disabled an agent (eg gemini-pro), but members can still continue using it via clone by editing the sid. This completely breaks the admin's resource management mechanism.

API: `PATCH /api/w/{w_id}/assistant/agent_configurations/{agent-id}`

HTTP header: 
```
PATCH /api/w/BSsJ1zPUYE/assistant/agent_configurations/{agent-id} HTTP/2
Host: eu.dust.tt
Cookie: ..
Content-Length: 459
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US,en;q=0.9
Sec-Ch-Ua: "Chromium";v="135", "Not-A.Brand";v="8"
Content-Type: application/json
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36
Accept: */*
Origin: https://eu.dust.tt
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://eu.dust.tt/w/BSsJ1zPUYE/builder/assistants/JpY5xizXRo?flow=workspace_assistants
Accept-Encoding: gzip, deflate, br
Priority: u=1, i

{"assistant":{"name":"gemini-pro-clone","pictureUrl":"https://dust.tt/static/emojis/bg-blue-300/brain/1f9e0","description":"An assistant designed to provide clear, concise, and factual responses efficiently.","instructions":"test-gemini-pro","status":"active","scope":"private","actions":[],"model":{"modelId":"claude-3-5-sonnet-20241022","providerId":"anthropic","temperature":0.7},"maxStepsPerRun":8,"visualizationEnabled":true,"templateId":null,"tags":[]}}
```

## Attachments
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
