# Privilege Escalation leading to post in channel without having privilege

## Report Details
- **Report ID**: 1114617
- **URL**: https://hackerone.com/reports/1114617
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-03-02T12:21:42.110Z
- **Disclosed**: 2021-09-13T05:36:41.848Z

## Reporter
- **Username**: fuzzsqlb0f
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mattermost

## Vulnerability Information
Hi H1,

mattermost.cloud has a feature of making a channel and once its set to public any other user can join the channel and post comments on that channel. In System Console --> Channel --> Permission channel owner can assign wether member can post comment or not. Once channel owner selects that channel member can not post even than they can post the comment in channel.


Steps To Reproduce:


- Step1: user1 `█████` created a channel which is public and under System Console --> Channel --> Permission gives guest and members to post comment.

- Step2: user2 `█████` joined user1 channel `mikefourchannel`  (already joined)

- Step3: user2 posted comment `has permission to comment in channel` in `mikefourchannel`  and captured the request and send it to repeater (

- Step3: user2 `███████` also created a channel `privilegeescalation` (already done)

- Step4: user1 `█████` and under System Console --> Channel --> Permission  guest and members removes right to comment.

- Step5: user2 `████████` now can not post any comment `This channel is read only. Only members with permission can post here`

- Step6: user2 `██████` goes to channel `privilegeescalation` and posted comment and captures the request and used post request which was captured in `Step3`

Note:
In video POC at time 0:01:42 user2 commenting when he was having privilege of commenting in channel and there is only that comment `has permission to comment in channel` below there is no other comment now plz go to time 0:04:29  you can see user2 commented `commenting in mike4 channel even no privielge` in user1 channel without proper privileges

Video POC attached for your reference.

Result:

user2 `███` posted comment in user1 channel `mikefourchannel` even user2 dosen't have privilege to do so.

## Impact

Impact:

Privilege escalation leading to comment on channel.

## Attachments
No attachments
