# Attacker can extract list of private project's project members

## Report Details
- **Report ID**: 128051
- **URL**: https://hackerone.com/reports/128051
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-03T21:15:56.751Z
- **Disclosed**: 2016-08-01T15:17:46.654Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
There's a minor information disclosure issue in the Import members feature. It can be abused to get a list of project members that are working on a private project. The following steps require that you're signed in as a user that can create a new project. When someone imports project members from another project, the following code is executed:

```ruby
# app/controllers/projects/project_members_controller.rb:96
def apply_import
  giver = Project.find(params[:source_project_id])
  
  # ...

  redirect_to(namespace_project_project_members_path(project.namespace, project),
                notice: notice)
end
```

When an attacker would specify a `source_project_id` that references a private project, it would copy the members of that project and it would add them to your own project. This way, you can check out who has access to which project. This information could be helpful in other attacks and/or could be used for social engineering since the email address of those people are public too.

The fix of this issue depends on if you want to allow projects to be imported the user has access to or only within the team scope.

## Attachments
No attachments
