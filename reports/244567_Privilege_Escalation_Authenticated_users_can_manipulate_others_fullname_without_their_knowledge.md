# [Privilege Escalation] Authenticated users can manipulate others fullname without their knowledge

## Report Details
- **Report ID**: 244567
- **URL**: https://hackerone.com/reports/244567
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-06-30T00:07:53.557Z
- **Disclosed**: 2017-08-10T02:13:47.946Z

## Reporter
- **Username**: r3y
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Hi Team,

## Summary
I have found a vulnerability, Which is you can change/update others Fullname without there knowledge.

## Step-by-step Reproduction Instructions
1.) login your account https://wakatime.com/login
2.) after you login go to `Leaderboard` then click `Create new one` or in easy way is to go here https://wakatime.com/leaders/new
3.) Now put any name you want e.g. `Test` then hit `Ceate Leaderboard`
4.) Then you will see `Leaderboards · Test · Notifications` or notification page, something like that, then just click `Daily`
5.)  Go to `Members` Panel and invite other users. just fill the `fullname` any name you want e.g. `test` then fill up the target email e.g. `██████@gmail.com` then hit `Send Invitation`
6.) after you do step 5. you will see the inviteded victim in `Members` panel
7.) You will notice the `Edit Icon` on the Victim fullname, Click that.
8.) Them  prompt box  will pop up saying `Enter new name for Test`, then just put the  `Fullname in input a value` e.g. `HACKED`.
9.) Now go login the victim email, and you will notice that the `fullname` of the victim was change into `HACKED`

## As you can see on my PoC Video
{F198789}

## Suggested Mitigation/Remediation Actions
Don't  allow other users to manipulate victim fullname.

Regards,
Reyd


## Attachments
No attachments
