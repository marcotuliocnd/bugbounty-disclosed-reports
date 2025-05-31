# IDOR Leads To Account Takeover Without User Interaction

## Report Details
- **Report ID**: 1272478
- **URL**: https://hackerone.com/reports/1272478
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-07-21T18:40:29.205Z
- **Disclosed**: 2022-09-04T13:23:03.840Z

## Reporter
- **Username**: theranger
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Hello Team,
There's IDOR Bug on this subdomain `mtnmobad.mtnbusiness.com.ng` leads to account takeover, More details check the Poc. 

## Steps To Reproduce:

  1. Create two accounts on `mtnmobad.mtnbusiness.com.ng` and both accounts verify the emails from your email inbox
  2. Login to attacker account on Browser A Go to update Profile Try to update the address for example and Capture the Request with burp send it to `Repeater`
{F1384484}
3. Login to Victim account on browser B do the same to get the victim `ID` you can Grab his ID without sending this request to `Repeater`
4. Go to the Attacker Request You sent to `Repeater` Change `/ID` with the Victim's `ID` you Grabbed From Step 3 Then change `Email` with different email, you need to change the `username` parameter not the `email` see this screenshot, Leave the email as your attacker email. the `username` Value is email and just update that one.

{F1384509} 
5.  Go Reset the Password (act like you don't know the Pass XD), login and successfully account Takeover without User Interaction

## Supporting Material/References:
--Check this Video :
{F1384553}

## Impact

Full account Takeover without user interaction

## Attachments
- Screenshot_1.png
- Screenshot_1.png
- idor.mp4
