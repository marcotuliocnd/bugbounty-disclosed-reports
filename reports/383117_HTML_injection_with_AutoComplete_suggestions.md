# HTML injection with AutoComplete suggestions

## Report Details
- **Report ID**: 383117
- **URL**: https://hackerone.com/reports/383117
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-07-18T13:45:00.816Z
- **Disclosed**: 2018-08-10T09:41:28.528Z

## Reporter
- **Username**: nickvergessen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
1. As user1 set your displayname to `<a href="https://nextcloud.com">Name</a>`
2. As user2 autocomplete the name in the comments input (or Talk chat input)
3. Click on the user name you just autocompleted

User2 is redirected to `https://nextcloud.com`

Only works with HTML, not with `script`

## Impact

User1 can trick user2 to render any html

## Attachments
No attachments
