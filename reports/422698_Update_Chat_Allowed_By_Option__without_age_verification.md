# Update Chat Allowed By Option ( without age verification )

## Report Details
- **Report ID**: 422698
- **URL**: https://hackerone.com/reports/422698
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-10-11T18:57:01.553Z
- **Disclosed**: 2018-10-18T12:34:39.056Z

## Reporter
- **Username**: yuvraj_dighe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
##Summary##
Hi Team,
I am here again with one interesting issue.
This issue deals with the fact that according to the policies of chaturbate, a broadcaster cannot modify the option - Chat Allowed By - until and unless he/she has verified his/her age (default choice is set to all).
This thing could be bypassed and any broadcaster who doesn't have his/her age verified could update this option.

## Steps To Reproduce:

1. First of all, start broadcasting.
2. Click on the gear icon in the chat options to open broadcaster settings.
3. Edit any option and intercept the request in Burp Suite.
4. Now in that request, replace the value of the parameter allowed_chat with any of the following 
   1. all
   2. tip_recent
   3. tip_anytime
   4. tokens
5. The value would get updated even though the age has not been verified.

## Impact

Any user who doesn't have his/her age verified can update settings which have been blocked for them.

## Attachments
- Screenshot_(88).png
