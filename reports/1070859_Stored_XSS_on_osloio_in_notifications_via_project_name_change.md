# Stored XSS on oslo.io in notifications via project name change

## Report Details
- **Report ID**: 1070859
- **URL**: https://hackerone.com/reports/1070859
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-04T02:22:21.873Z
- **Disclosed**: 2021-01-05T19:06:50.031Z

## Reporter
- **Username**: optional
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: logitech

## Vulnerability Information
Hey Logitech team.

## Summary:
It is possible for an editor on a project to rename a project to a malicious HTML element, which when opened in the notification dropdown will render and fire javascript.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Invite user to join the project and allow editor permissions.
  1. As the editor account, click on any of the projects and click rename. Insert malicious HTML there.
  1. Log in as the owner of the project directory and click on the notification bell on the top right. This will cause the XSS to fire.

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

_Fig 1: Inviting the editor to project_
{F1143360}

_Fig 2: Notification Settings for Owner:_
{F1143367}

_Fig 3: Editor Changing Project name to malicious object_
{F1143363}
{F1143364}

_Fig 4: Logging in as the owner again_
{F1143361}

_Fig 5: Opening Notification Bell_
{F1143362}

## Impact

The impact of this vulnerability is that users who are invited onto projects as an editor are able to inject malicious javascript such as keyloggers to escalate their privileges or perform actions as other users.

## Attachments
- invite_editor_onto_project.PNG
- logged_in_as_the_owner_admin.PNG
- opening_notifications_causes_payload_to_fire.PNG
- editor_changing_name_of_project_to_malicious_payload.PNG
- rename_button_for_editor_to_add.PNG
- notification_settings.PNG
