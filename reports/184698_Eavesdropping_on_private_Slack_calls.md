# Eavesdropping on private Slack calls

## Report Details
- **Report ID**: 184698
- **URL**: https://hackerone.com/reports/184698
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-11-24T02:57:14.816Z
- **Disclosed**: 2017-02-08T21:14:04.833Z

## Reporter
- **Username**: michiel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
A vulnerability exists in Slack's call functionality that allows a team member to eavesdrop on private ongoing Slack calls by inviting themselves into the conversation without the permission from either participant. By doing so they can eavesdrop on co-workers' private conversations as well as taking part in these conversations. To make the attack less obvious, the attacker could re-use Slackbot's avatar and choose a username that is similar to Slackbot. Another scenario would be to pick the avatar of the person you want to impersonate and choose a username that is similar to theirs. 

## Setup
Before trying to reproduce the vulnerability, make sure you have the following:
- Slack Calls should be enabled in your Slack instance.
- Have at least two accounts you control. One we will call the Main Account, the other one we will call the Eavesdropper Account.
- Have at least two accounts you do not control on the same Slack instance. They will be used to mock the situation of two co-workers having a private Slack call.
- For easy reproduction, it is advised to initiate the call from a web browser rather than a native app.
- Make sure to have some type of intercepting proxy running that allows you to record HTTP requests and replay them easily.

## Steps to Reproduce
### Obtaining the vulnerable request
First off, we are going to obtain the exact request to the endpoint that contains the vulnerability (`/api/screenhero.rooms.invite`). This will be needed to later on modify and add Eavesdropper Account to the private call. 

Set up a call and invite someone to the call. Make sure to capture the request to `/api/screenhero.rooms.invite` and save it so you can replay it easily later. The request should look something like:

```
POST /api/screenhero.rooms.invite?_x_id=91700980-1479951838.521 HTTP/1.1
Host: hackerone.slack.com
Origin: https://hackerone.slack.com
X-Slack-Version-Ts: 1479949022
[...]

is_video_call=false&responder=U0254GYNR&room=R36L2K8P6&set_active=true&should_share=true&token=<snip>
```

### Staging the attack environment
Start by setting up a 1:1 call between two users (both accounts you don't necessarily have control over). This is to mock a situation where two co-workers are on a private 1:1 Slack call. 

Note the Screenhero room ID of the call. You will need this later. In this scenario, I am going to assume the attacker is already in possession of the room ID. The room ID can be recognized by the ID after `/call/` in https://hackerone.slack.com/call/R36L2K8P6 (an example).

### Pulling off the attack
Take the request you saved earlier, and now modify the request as follows:
- change the value of the `room` parameter to the room ID you noted from the previous step
- change the value of the `responder` to the user ID of Eavesdropper Account. The reason why this can't be your own user ID (Main Account) is that you're not allowed to invite `self`. 

After these changes, forward the request and wait for a call on Eavesdropper Account. When you accept this call, you will be placed into the private conversation the two victims were having. 

Let me know if there's anything else you need to validate this issue.


## Attachments
No attachments
