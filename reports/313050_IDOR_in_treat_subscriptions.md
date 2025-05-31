# IDOR in treat subscriptions

## Report Details
- **Report ID**: 313050
- **URL**: https://hackerone.com/reports/313050
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-02-07T02:38:01.307Z
- **Disclosed**: 2018-04-25T12:25:30.883Z

## Reporter
- **Username**: harsh13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
The treat subscriptions tab in my profile has an IDOR.

The corresponding api:

POST /php/filter_user_tab_content.php HTTP/1.1
user_id=██████&tab=treat_subscription&order_history_offset=0&order_history_limit=20


You can give any user id and you will be able to see the treat subscriptions of that user.

## Impact

A user can view treat subscriptions of any other user.

## Attachments
No attachments
