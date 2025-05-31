# Adding everyone to the repo due to the lack of rate limit

## Report Details
- **Report ID**: 978768
- **URL**: https://hackerone.com/reports/978768
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-09-10T22:21:21.836Z
- **Disclosed**: 2020-09-14T23:28:30.952Z

## Reporter
- **Username**: sadd_man
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

Since there is no rate limit in the inviting users to the repository section, it is possible to add all users on gitlab to a repository.

### Steps to reproduce

(Step-by-step guide to reproduce the issue, including:)

1. Create a repository
2. go to the project members section
3. choose a random user
4. before clicking the invite button, we need to capture the request with the burp suite..
5. ███████
6. Send it to the Intruder module, specify the █████ field here between 1 and 7006996 and send the request.

### Impact

It is possible to collect all users on Gitlab in a single repository, so users' mailboxes will be filled with notifications.


### Note

Because the rate limit is out of scope, I tested it and I could not stop the python script, and there were users affected.

## Impact

It is possible to collect all users on Gitlab in a single repository, so users' mailboxes will be filled with notifications.

## Attachments
No attachments
