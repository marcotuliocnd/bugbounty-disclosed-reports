# S3 bucket unnecessarily discloses permissions

## Report Details
- **Report ID**: 330135
- **URL**: https://hackerone.com/reports/330135
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-03-27T02:41:38.028Z
- **Disclosed**: 2019-04-26T13:10:58.399Z

## Reporter
- **Username**: salmon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: udemy

## Vulnerability Information
The 'udemy-images' bucket allows the 'AllUsers' group to list ACLs that are applied to the bucket. By navigating to: [https://udemy-images.udemy.com](https://udemy-images.udemy.com) or by using the `aws-cli` tool an attacker can see which users have `READ`, `WRITE`, `READ_ACP`, and `WRITE_ACP` rights. Doing this now we can see one user who has these rights (see attached screenshot). We can see their ID and DisplayName (hi [@caglaroktay!](https://twitter.com/caglaroktay))

## Impact

While this doesn't give public users write access to the bucket, a motivated attacker can gather a lot of information from this. If one were targeting the Udemy AWS infrastructure, this information would give them all they need to know to start gathering intel on an authorized user (like @caglaroktay). An easy way to do this would be  to look for breached passwords belonging to the authorized user to try logging into their AWS console with.

This public permission is unnecessary as it is not needed for the site to run properly and should be removed immediately.

## Attachments
- udemy.png
