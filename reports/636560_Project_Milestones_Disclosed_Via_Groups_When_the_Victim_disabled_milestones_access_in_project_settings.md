# Project Milestones Disclosed Via Groups When the Victim disabled milestones access in project settings

## Report Details
- **Report ID**: 636560
- **URL**: https://hackerone.com/reports/636560
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-05T18:43:37.166Z
- **Disclosed**: 2019-12-13T13:28:37.470Z

## Reporter
- **Username**: rockrzhackr9z
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
##Reproduction steps:


Create a public group and public project.


Go to public project settings and disable the project settings to members only.

{F522796}


If the attacker visits milestones via projects then may see 404 not found page.


https://gitlab.com/victim-waka-waka/test-group-for-sharing/-/milestones/1

{F522797}


But the attacker will view the project mile stones via groups.


{F522798}

## Impact

Attacker will view the project milestones which are disabled by the admin in project settings.

## Attachments
- disable_the_project_access_settings_to_only_project_members.png
- milestones_not_accessible_via_projects.png
- project_milestones_disclosed_via_groups.png
