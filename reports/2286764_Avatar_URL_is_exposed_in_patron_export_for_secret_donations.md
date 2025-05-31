# Avatar URL is exposed in patron export for secret donations

## Report Details
- **Report ID**: 2286764
- **URL**: https://hackerone.com/reports/2286764
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-12-14T19:14:15.499Z
- **Disclosed**: 2023-12-15T14:37:10.269Z

## Reporter
- **Username**: mdivecky
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
When user sets their donation Privacy level to "Secret" they are indicating that they don't want to be identified by the donation recipient.

By exporting the `patron_avatar_url`, in `https://liberapay.com/<account_name>/patrons/export.csv`, the user might be exposed just by doing a reverse image search for such avatar.

## Impact

I would hope that there is no gain in trying to deanonymise their donors, but including the avatar should not be needed and I hope it should be an easy fix. 


I do not wish to be compensated in any way, the reason for using HackerOne is just that I don't want to disclose the issue on Github. Thank you for your great service! :)

## Attachments
No attachments
