# Privilege Escalation Leads to Control The Owner Access Token Which leads to control the stream [streamlabs.com]

## Report Details
- **Report ID**: 1174527
- **URL**: https://hackerone.com/reports/1174527
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-04-26T03:15:59.913Z
- **Disclosed**: 2021-04-27T22:20:38.301Z

## Reporter
- **Username**: mrmax4o4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: logitech

## Vulnerability Information
Hi Security team,

##Summary:
 I was able as `Administrator`  to change the account owner access token 

##Description:

As `Administrator` i have high privileges but i have some restricted areas
{F1278364}
For example i got invitation from MrX with Administrator role.
When i navigated to MrX account as administrator i found all the menu items except the `settings` 
{F1278370}
so i tried to navigate to `dashboard/#settings` and i was able to access MrX's account settings! 
{F1278399}
I tried to use many features but couldn't but found on `API Settings --> API Tokens` some cool feature allowed me  to `Refresh API Access Token` which is part of a lot of requests (will describe on the impact section)

##Steps to reproduce:
we need 2 accounts 
-  MrX (account owner)
- MrMax
1.  Using MrX account go to `https://streamlabs.com/dashboard#/settings/shared-access` and create invitation with administration role, Copy the link
2.  Open the link on your other browser which you are logged in as MrMax, accept the invite then click on `MrX`to access his account
{F1278374}
3. You will get message on the top says `You are currently acting as MrX, click here to return to MrMax.` , now navigate to 
`https://streamlabs.com/dashboard#/settings/api-settings` you well see empty Access token field , click on `Refresh` then yes
{F1278380}

Done ^ ^

## Impact

The `API Access Token` is used in most of API requests and a lot of other places e.g. 
{F1278381}
Here is a list of URLs the token used on , This list represents about 80% of the uses for this token here is one of the uses for this token:
To stream
- I must install recording software supports streaming (e.g. OBS Studio..etc.)
- To use any of the streamlabs widgets (Alert box , Start goal , The jar ,Tip ticker , Follower goal , View count , Stream boss , Sponsor banner...etc. ) i must have link contains this token 

{F1278389}
I want to use this widget i should take this url and paste it on the streaming software to make it visible to the  stream viewers 
So as a bad administrator i can change the `API Access Token ` while MrX is streaming which will stop the above widgets which  revokes the main reason for making the streamlabs application which is `widgets` to help the streamers.

I am still investigating for more impacts and i will let you know if there is any updates

Best Wishes,
MrMax

## Attachments
- Logitech-PS-2.mp4
- Logitech-Admin-priv.png
- Logitech-PS2.png
- Logitech-PS1.png
- Logitech-P3.png
- Logitech-P4.png
- Logitech-P5.png
- Logitech-P6.png
