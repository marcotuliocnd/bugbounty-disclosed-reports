# Allow authenticated users can edit, trash,and add new in BuddyPress Emails function

## Report Details
- **Report ID**: 833782
- **URL**: https://hackerone.com/reports/833782
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-29T08:52:13.199Z
- **Disclosed**: 2020-05-22T00:33:04.676Z

## Reporter
- **Username**: hoangkien1020
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
## Description:

Allow author can edit, trash,and add new your posts in BuddyPress Emails function
And editor can edit,trash, add new any posts in BuddyPress Emails default.
## Steps To Reproduce:

Step 1 : Create two accounts: Admin and Author
Step 2: Login with admin account. In admin account, give author to admin account.
Step 4: Login with author within dashboard
Access link:
*domain/wp-admin/edit.php?post_type=bp-email*
Step 5: Revoke author to author privilege in admin account
Step 6: Within author dashboard, author can edit, trash,and add new
PoC by video:
https://bit.ly/2UH7iLz
## Recommendations
Valid user current session access.

## Impact

Author can edit, trash,and add new in BuddyPress Emails.
And editor can edit,trash, add new any posts in BuddyPress Emails default.

## Attachments
No attachments
