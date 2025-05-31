# [Repository Import] Open Redirect via "continue[to]" parameter 

## Report Details
- **Report ID**: 215970
- **URL**: https://hackerone.com/reports/215970
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-25T08:44:49.387Z
- **Disclosed**: 2017-04-06T04:27:32.522Z

## Reporter
- **Username**: ysx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hi,

While experimenting with Repository Import functionality on a fresh GitLab 9.0 CE install, I noticed that the `continue[to]` parameter can be used to perform an Open Redirect through the inclusion of a double-slash prefix. 

## Proof of Concept
The following Proof of Concept URL enables a malicious actor to execute this redirect against any user – as long as they have permissions to view a certain repository. 

```
http://<instance>/<user>/<repository>/import?continue[to]=//google.com
```

## Observation
I first noticed the `continue[to]` parameter while receiving the `You're not allowed to make changes to this project directly` message – demonstrating that edit-level access to the repository in question is not required.

Thanks!

## Attachments
No attachments
