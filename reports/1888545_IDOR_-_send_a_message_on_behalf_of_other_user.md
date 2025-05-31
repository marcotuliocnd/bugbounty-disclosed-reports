# IDOR - send a message on behalf of other user 

## Report Details
- **Report ID**: 1888545
- **URL**: https://hackerone.com/reports/1888545
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-02-27T19:01:59.458Z
- **Disclosed**: 2023-09-20T09:37:17.662Z

## Reporter
- **Username**: lamscun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
Hi there, 


I just found an IDOR in https://hello.dev.myhubs.net/. It allow attacker send a message on behalf of other user 

Step to reproduce:
	- 1.  Admin: Create Room 
	- 2.  Attacker: Join room
	- 3.  Attacker get "session_id" of other user in response "presence_diff"

		{F2200381}
	- 4.  Attacker send add "session_id" parameter to request send message 
		```
		["8",null,"hub:84fbckn","message",{"session_id":"<victim_session_id>","body":"eeeee","type":"chat"}]
		```
		{F2200382}
	- Now the message will be send on behalf of victim 

POC:  
{F2200384}

## Impact

It allow attacker send a message on behalf of other user

## Attachments
- 1.png
- 2.png
- recording-1677524444699.webm
