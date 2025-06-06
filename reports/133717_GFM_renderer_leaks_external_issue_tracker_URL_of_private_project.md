# GFM renderer leaks external issue tracker URL of private project

## Report Details
- **Report ID**: 133717
- **URL**: https://hackerone.com/reports/133717
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-22T05:34:07.948Z
- **Disclosed**: 2017-06-08T22:02:26.903Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
# Vulnerability details
The GFM renderer has the ability to cross-link issues between projects. When this project is private and the user doesn't have access, the link isn't made. This is good. However, when the private project has an external issue tracker set up, an attacker can extract the external URL from a private project. In some cases, this could lead to the disclosure of the issue.

# Proof of concept
As a victim, set up a new private project and activate an external issue tracker. I used Jira to reproduce my find. Lets say the victim's project can be found at `root/secret`. Now sign in as a different user that does not have access to that program. Create a new project. In that project, create an issue with the body `root/secret#1`. The rendered body of the issue will now contain a link to the issue URL of the private project.

# Guessing namespaces
The issue described above is hard to exploit because there are two unknowns to the attacker: the namespace and the name of the private project. I find an ID enumeration vulnerability in the merge request controller that allows an attacker to dump all namespaces and project names. An attacker can use this endpoint to generate a markdown message that contains all namespaces and project names, appended with `#1` in order to extract all external issue tracker URLs.

The ID enumeration vulnerability can be reproduced by creating a new merge request and changing the `merge_request[target_project_id]` parameter in the URL to reference another project. The returned HTML will contain the name of the namespace and project name of the project associated with that ID. By enumerating all IDs, all project names can be extracted.

http://gitlab-instance/jane/project/merge_requests/new?change_branches=true&merge_request%5Bsource_branch%5D=fix&merge_request%5Bsource_project_id%5D=20&merge_request%5Btarget_branch%5D=master&merge_request%5Btarget_project_id%5D=24

The name of the project can be found in the response on line 74 and 75:

{F88690}

# Impact
The issue by itself isn't super likely to be exploited, because the attacker doesn't know the namespace and project name. However, by combing the two issues, they become a lot more severe. Both issues should be addressed in order to mitigate the leakage of the private program names and the external issue tracker URL of a private project.

## Attachments
- Screen_Shot_2016-04-21_at_22.30.18.png
