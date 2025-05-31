# [Privilege Escalation] Authenticated users can manipulate others fullname without their knowledge [Team Vector]

## Report Details
- **Report ID**: 246419
- **URL**: https://hackerone.com/reports/246419
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-07-06T13:00:55.541Z
- **Disclosed**: 2017-08-10T02:14:02.065Z

## Reporter
- **Username**: r3y
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Hi Team,

## Summary,
When my free trial subscription was activated on wakatime.com, i also found that there is a new tab or features which is the `Teams`, 
In `Teams` you can manipulate again others `fullname` without their knowledge.
as the details of my other reports [[Privilege Escalation] Authenticated users can manipulate others fullname without their knowledge
](https://hackerone.com/reports/244567) This time the endpoint that we are using is Teams, not Leaderboards.

## Steps:
1.) Go to the Teams->Settings->Members
2.) Invite other users on your Teams member settings
3.) Now you will see again that there is `Edit Icon` on the victim after fullname, Click that.
4.) Then prompt will pop up saying "Enter new name for blahblah.." then just put a value e.g. HACKED AGAIN!
5.) Now go login the victim email, and you will notice that the fullname of the victim was change into HACKED AGAIN!

## Here is the PoC Video for clearer demonstration.
{F200597}

## Suggested Mitigation/Remediation Actions

Don't allow other authenticated users to manipulate others fullname.

Kind Regards,
@reydd

## Attachments
No attachments
