# Stored XSS in Name of Team Member Invitation

## Report Details
- **Report ID**: 786301
- **URL**: https://hackerone.com/reports/786301
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-01-30T16:09:30.436Z
- **Disclosed**: 2020-02-06T20:56:52.353Z

## Reporter
- **Username**: abdulsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: localizejs

## Vulnerability Information
hello team
i have found an stored in add team member
##Step to reproduce
1. Go to  https://localizestaging.com/organization/team?filter=all
2. click on add team member
3. On the name, enter payload:  </script><svg onload=alert(document.domain)>    
4. and in the email  add  your victim email
4. when he join the team the xss  will trigger.
{F701271}

now  victim , can't logout, he can't do anything in his account

best regards
@moodiabdoul3

## Impact

the victim can nothing in his account

## Attachments
- xsslocalize.png
