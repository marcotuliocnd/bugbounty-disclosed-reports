# protect against tabnabbing in statement

## Report Details
- **Report ID**: 109161
- **URL**: https://hackerone.com/reports/109161
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-01-07T23:47:57.495Z
- **Disclosed**: 2017-10-01T12:39:17.527Z

## Reporter
- **Username**: atom
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hello,

when we include a link on statement in our profile, it just create an html tag like this:
``` <a href="http://google.com">http://google.com</a> ```
^ That's vulnerable. How? Once the owner of the profile added a malicious url it is possible that the link has a referral link thingy that will open a tab that has a phishping page of  gratipay.

Fix:
``` <a href="http://google.com" rel="nofollow">http://google.com</a> ```

Allan

## Attachments
No attachments
