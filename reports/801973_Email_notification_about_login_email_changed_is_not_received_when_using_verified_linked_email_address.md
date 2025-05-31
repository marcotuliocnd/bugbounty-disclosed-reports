# Email notification about login email changed is not received when using verified linked email address

## Report Details
- **Report ID**: 801973
- **URL**: https://hackerone.com/reports/801973
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-02-21T18:05:35.585Z
- **Disclosed**: 2020-03-25T11:01:46.760Z

## Reporter
- **Username**: shaileshpratapwar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

In https://gitlab.com/profile, user can update the email id to use for login to gitlab account using field "Email".
Usually, when this login email id is updated, there will be 2 email sent on previous email Id with subjects as. 
Email 1 - Email Changed:- This tell that login email has been changed to new email.
Email 2 - Confirmation instructions :- This has a confirmation link to confirm the email id.

However, when we change this login email ID to one of the email ID which is already linked in our gitlab account under https://gitlab.com/profile/emails, then none of the above 2 emails are sent to previous email ID.

I understand that as linked email ID are already verified, so no need to send the 2nd email i.e. Confirmation Instruction but the first email i.e. "Email Changed" should be sent to previous email ID stating that your login email has been changed to new one.

### Steps to reproduce
1. User logs in to gitlab.com using his email ID ( ex. user-one@gmail.com)
2. Now, on https://gitlab.com/profile, user updates the login email id ("Email" field having "We also use email for avatar detection if no avatar is uploaded" written below it) to another email id (ex. user-two@gmail.com)
3. Now, an email will go to user-one@gmail.com informing that email change action is being done. This is as expected. (Email subject : "Email Changed")
4. Now, broken scenarios is as follows :
5. On https://gitlab.com/profile/emails, user adds new email address (ex. user-three@gmail.com).
6. user-one@gmail.com will receive email to confirm the newly added email by clicking on confirmation link received in new email.
7. So, one new email id i.e. user-three@gmail.com will be seen as verified under https://gitlab.com/profile/emails,
8. Now if we try to update login email id on https://gitlab.com/profile (as in step 2 above) to user-three@gmail.com, no email with subject as "Email Changed" will be received on user-one@gmail.com.


### Impact

1. Account primary owner will not be aware of the fact that owner has been changed to some other email id. Although, new email is verified, "Email Changed" email will be expected by account primary owner as this happens usually (as happened in step 3 in steps above). So, consistency is not maintained in informing new changes to account primary owner.

### What is the expected *correct* behavior?

I think there should be consistency in informing these critical account changes to account owner. "Email Changed" email is received by owner when unverified email is added. Similar should happen for verified email as body of this email is playing important role here to inform account owner of what changes happened.

### Output of checks
This bug happens on GitLab.com

#### Results of GitLab environment info
This bug happens on GitLab.com

Attached are the POC screenshots.
Please let me know if you need a video POC.

## Impact

Account owner will not be aware that login email id for the gitlab account has been changed to one of the linked email id.

## Attachments
- Primary_email_is_changed_to_linked_email.png
- Example_of_Verified_Linked_Email.png
- Expected_Email_Changed_Email.png
