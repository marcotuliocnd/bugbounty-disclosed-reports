# [Part II] Email Confirmation Bypass in myshop.myshopify.com that Leads to Full Privilege Escalation

## Report Details
- **Report ID**: 796808
- **URL**: https://hackerone.com/reports/796808
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-02-14T17:37:31.543Z
- **Disclosed**: 2020-04-01T21:02:00.348Z

## Reporter
- **Username**: ngalog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary 
In #791775, I submitted a bug at Sunday 5pm Canada time, it was triaged two hours later, and I got the **temp** fix message at around 3am the next day in Canada time. Truly awesome, the next day I retested after the first fix, and found that I

- Cannot receive the email confirmation in the email used to sign up
- Cannot integrate across stores/partner even they share the same email address after confirming them

And the report was later resolved after I verified the fix.

For some reason, I decided to test again to see what's something new that I can find.

Then I found user can change their email prior to receiving the verification message on their original email. i.e. the same technique, I don't know what went wrong in my first retest, but Shopify security and engineering team again showed their professionalism, quickly resolving the second comments I left in ~3.5 hrs.

And when I thought this is the end of story, I later received a comment asking me to open a new report about the second retest, and here I am writing this report.

Thanks,
Ron

## Impact

.

## Attachments
No attachments
