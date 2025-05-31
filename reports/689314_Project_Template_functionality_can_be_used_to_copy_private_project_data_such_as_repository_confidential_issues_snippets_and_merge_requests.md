# Project Template functionality can be used to copy private project data, such as repository, confidential issues, snippets, and merge requests

## Report Details
- **Report ID**: 689314
- **URL**: https://hackerone.com/reports/689314
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-09-06T05:40:41.068Z
- **Disclosed**: 2019-11-27T10:02:44.156Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
I've found a three minor vulnerabilities which, when combined, allow an attacker to copy private repositories, confidential issues, private snippets, and then some. I'll go through the code path to explain the vulnerabilities and how they are combined. See the **Proof of Concept** section if you want to reproduce it immediately.

Let's start at the `ProjectsController` of EE, which is prepended to `app/controllers/projects_controller.rb` in an EE instance. 

**ee/app/controllers/ee/projects_controller.rb**
```ruby
override :project_params_attributes
    def project_params_attributes
      super + project_params_ee
    end

def project_params_ee
  attrs = %i[
    # ...
    use_custom_template
    # ...
    group_with_project_templates_id
  ]

  # ...

  attrs
end
```

This method defines what parameters can be passed by the user. The two notable parameters here are `use_custom_template` and `group_with_project_templates_id`. This method appends the result value of `project_params_attributes` method in `app/controllers/projects_controller.rb` on line 351, which specifies all the CE attributes a user can provide when creating a project. The CE controller allows the `template_name` parameter to be passed, too. This means that these three parameters can be passed to the `Projects::CreateService` in the `create` method:

**app/controllers/projects_controller.rb**
```ruby
def create
  @project = ::Projects::CreateService.new(current_user, project_params(attributes: project_params_create_attributes)).execute

  # ...
end

# ...

def project_params_attributes
  [
    # ...
    :template_name,
    # ...
  ]
```

In EE, the `EE:Projects::CreateService` is prepended to the `Projects::CreateService`. The prepended EE code contains logic to validate the `use_custom_template` and `group_with_project_templates_id` parameters.

**ee/app/services/ee/projects/create_service.rb**
```ruby
def execute
  # ...

  group_with_project_templates_id = params.delete(:group_with_project_templates_id) if params[:template_name].blank?

  # ...

    validate_namespace_used_with_template(project, group_with_project_templates_id)
end

# ...

def validate_namespace_used_with_template(project, group_with_project_templates_id)
  return unless project.group

  subgroup_with_templates_id = group_with_project_templates_id || params[:group_with_project_templates_id]
  return if subgroup_with_templates_id.blank?

  templates_owner = ::Group.find(subgroup_with_templates_id).parent

  unless templates_owner.self_and_descendants.exists?(id: project.namespace_id)
    project.errors.add(:namespace, _("is not a descendant of the Group owning the template"))
  end
end
```

The code above is where the first vulnerability can be found. In a normal situation, a Project Template can only be copied to a namespace (group) that is a descendant of the project template. However, the `validate_namespace_used_with_template` method returns a `nil` value when the project is **not** being created for a group (`return unless project.group`). This means that if a `group_with_project_templates_id` is given for a project that is created in a `User` namespace, the authorization / validation logic is never executed. This means that the `use_custom_template` and `group_with_project_templates_id` parameters remain to be set on the instance variable `params`.

Because the EE code is prepended, the `execute` method is executed before the `Projects::CreateService` is called. Because the EE class its validation logic is bypassed, the `execute` method of the `Projects::CreateService` class is called:

**app/services/projects/create_service.rb**
```ruby
def execute
  if @params[:template_name].present?
    return ::Projects::CreateFromTemplateService.new(current_user, params).execute
  end

  # ...
end
```

When a `template_name` is given, instead of executing the normal execution flow, the result of `Projects::CreateFromTemplateService` is returned. The CE code for this class isn't very important. The EE class contains the logic that is worth checking out:

**ee/app/services/ee/projects/create_from_template_service.rb**
```ruby
def execute
  return super unless use_custom_template?

  override_params = params.dup
  params[:custom_template] = template_project if template_project

  ::Projects::GitlabProjectsImportService.new(current_user, params, override_params).execute
end

private

def use_custom_template?
  # ...
    template_name &&
      ::Gitlab::Utils.to_boolean(params.delete(:use_custom_template)) &&
      ::Gitlab::CurrentSettings.custom_project_templates_enabled?
  # ...
end

def template_project
  # ...
    current_user.available_custom_project_templates(search: template_name, subgroup_id: subgroup_id)
                .first
  # ...
end

def subgroup_id
  params[:group_with_project_templates_id].presence
end
```

This class does a couple of things: it makes sure a custom template name is given, that it should use the given template name, and that the GitLab instance has custom project templates enabled. For what it's worth: gitlab.com has this setting enabled. When it passes those checks, the `template_project` method is invoked. Here is the definition of the `available_custom_project_templates` method:

**ee/app/models/ee/user.rb**
```ruby
def available_custom_project_templates(search: nil, subgroup_id: nil)
  templates = ::Gitlab::CurrentSettings.available_custom_project_templates(subgroup_id)

  ::ProjectsFinder.new(current_user: self,
                       project_ids_relation: templates,
                       params: { search: search, sort: 'name_asc' })
                  .execute
end
```

This method requires two parameters: `search` and `subgroup_id`. The first one is the `template_name` the user passes, the second one `group_with_project_templates_id`. The `templates` variable gets its value based on the following method definition:

**ee/app/models/ee/application_setting.rb**
```ruby
def available_custom_project_templates(subgroup_id = nil)
  group_id = subgroup_id || custom_project_templates_group_id

  return ::Project.none unless group_id

  ::Project.where(namespace_id: group_id) 
end
```

This method will return all `Project` models based on the `namespace_id` that is provided in the `subgroup_id` parameter. This is then passed to the `ProjectsFinder` in the `available_custom_project_templates` method on the `User` model. This is where the second vulnerability can be found. The `ProjectsFinder` uses an initial collection, which consists of the projects the authenticated user can access. However, it does **not** check the access level of the user. This means that any project that is public, but has Repository, Issue, Snippets (etc.) access disabled for Guests, will be returned by the `available_custom_project_templates` method on the `User` model. In a perfect world, it seems that this method would limit the projects that can be returned based on the user's permissions for said projects.

If we go back to the `EE:Projects::CreateFromTemplateService` file, you can see that the `template_project` will return the first project that is returned by the `available_custom_project_templates` method. This means that `params[:custom_template]` may contain a `Project` model that the user is not authorized to see everything for. The `EE::Projects::CreateFromTemplateService` class then calls the `Projects::GitlabProjectsImportService` class with the updated parameters.

**ee/app/services/ee/projects/gitlab_projects_import_service.rb**
```ruby
def execute
  super.tap do |project|
    if project.saved? && custom_template
      custom_template.add_export_job(current_user: current_user,
                                     after_export_strategy: export_strategy(project))
    end
  end
end

private

override :prepare_import_params
def prepare_import_params
  super

  if custom_template
    params[:import_type] = 'gitlab_custom_project_template'
  end
end

def custom_template
  strong_memoize(:custom_template) do
    params.delete(:custom_template)
  end
end

def export_strategy(project) 
 Gitlab::ImportExport::AfterExportStrategies::CustomTemplateExportImportStrategy.new(export_into_project_id: project.id)
end
```

This EE class is prepended, but uses `super.tap` to call the CE code (`super`) and then taps into the result of the CE code. If `params[:custom_template]` has been set and the project was successfully saved by the `super` call, an export job is scheduled for the `custom_template` that was returned by the `ProjectsFinder`. It's worth nothing that at this point the user may not be authorized to see the code, issues, etc., of the project. Additionally, an export strategy is passed that imports the export file in the newly created project.

This is where the third vulnerability can be found. When an export job is scheduled, it assumes the user is authorized to make the export. Ideally, the Sidekiq job (`ProjectExportWorker`) that is scheduled would do an authorization check to make sure that the user is authorized to export the project. This would also avoid a TOCTOU issue where the user schedules a job when the queue is clogged / Sidekiq workers are paused and would leave the project before the job is executed. When the export is created, it'll automatically be imported in the project that the user has full access to.

Combined, these vulnerabilities results in an attacker being able to obtain any confidential information that is included in a project export. This vulnerability **only** works for public projects with limited access levels for repositories, issues, pipelines, merge requests (and more) that belong to a group. A good example of this would be `gitlab-org`, `gitlab-data`, `gitlab-com`, on gitlab.com. There are plenty of repositories, such as https://gitlab.com/gitlab-com/finance (see below), that are public but don't expose the repository, issues, and merge requests.

{F576178}

# Proof of Concept
To reproduce this vulnerability:

* sign in as a normal user and create a group, let's assume this is group ID 1
* within this group, create a public project named `test_project`
* under **Settings > General** update the **Visibility, project features, permissions** to only allow Issues, Repository, Wiki, and Snippets to be seen by **Only Project Members**:

{F576180}

* sign into another account and go to http://instance/projects/new
* create a new project and intercept the request, it'll look something like this (I've left out unimportant parameters):

```
POST /projects HTTP/1.1
Host: instance
...

----------506740453
Content-Disposition: form-data; name="project[use_custom_template]"

false
----------506740453
Content-Disposition: form-data; name="project[template_name]"

----------506740453
Content-Disposition: form-data; name="project[group_with_project_templates_id]"

----------506740453
Content-Disposition: form-data; name="project[name]"

project_name
----------506740453
Content-Disposition: form-data; name="project[namespace_id]"

1
----------506740453
Content-Disposition: form-data; name="project[path]"

project_name
----------506740453--
```

* in this request, change `use_custom_template` to `true`, the `template_name` to the name the victim gave to the project (`test_project`), and `group_with_project_templates_id` to the group ID of the public group the victim created (`1`). When forwarded, the server will respond with a redirect and, when followed, show a page indicating that the project is being imported:

{F576184}

Depending on the size of the project and how busy the queues are, it can take a couple of minutes to generate the export of the project and then import it to the new project. Come back in a couple minutes and find the repository, confidential issues, private snippets, merge requests, CI pipelines, and more being copied to the attacker's project.

**Redacted copy of `gitlab-com/finance`**
{F576189}

## Impact

Any access level that has been put in place for projects the user can access can be bypassed using this vulnerability. According to the documentation, this means that the following information can be obtained:

* Project and wiki repositories
* Project uploads
* Project configuration, including services
* Issues with comments, merge requests with diffs and comments, labels, milestones, snippets, and other project entities
* LFS objects
* Issue Boards

{F576190}

## Attachments
- Screen_Shot_2019-09-05_at_10.08.18_PM.png
- Screen_Shot_2019-09-05_at_10.13.21_PM.png
- Screen_Shot_2019-09-05_at_10.17.09_PM.png
- Screen_Shot_2019-09-05_at_10.19.15_PM.png
- cat.gif
