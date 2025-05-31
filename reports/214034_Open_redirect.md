# Open redirect

## Report Details
- **Report ID**: 214034
- **URL**: https://hackerone.com/reports/214034
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-16T22:56:04.278Z
- **Disclosed**: 2017-04-06T08:06:22.582Z

## Reporter
- **Username**: eadz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
POC:

$GITLAB_INSTANCE = gitlab.com

Visit: 

https://$GITLAB_INSTANCE/dashboard/todos?page=99999999&host=www.google.com

Bug is in Dashboard::TodosController line 10

Likey
Same bug in Projects::IssuesController line 32
and other places in the codebase where you `redirect_to params.merge(..)` 


## Attachments
No attachments
