# Race condition in GitLab import, giving access to other people their imports due to filename collision

## Report Details
- **Report ID**: 214028
- **URL**: https://hackerone.com/reports/214028
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-03-16T22:30:03.968Z
- **Disclosed**: 2017-10-03T19:11:28.808Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
# Vulnerability details
There's a race condition in the `Import::GitlabProjectsController#create` endpoint that allows an attacker to gain access to someone else's import file. The race condition happens when there's a collision in two or more file names uploaded at the same time, before the import gets processed by Sidekiq. The person uploading the file for the first time will see the last person's file contents instead.

# Impact
Depending on the contents of the GitLab import file, this could leak confidential information from other users on the GitLab instance.

# Proof of concept
This is hard to reproduce without a good setup, but conceptually it's pretty easy to explain by going through the code. When someone uploads a new file, the following code gets executed:

**app/controllers/import/gitlab_projects_controller.rb** (15-18)
```ruby
import_upload_path = Gitlab::ImportExport.import_upload_path(filename: project_params[:file].original_filename)

FileUtils.mkdir_p(File.dirname(import_upload_path))
FileUtils.copy_entry(project_params[:file].path, import_upload_path)
```

The `Gitlab::ImportExport.import_upload_path` method looks like this:

```ruby
def import_upload_path(filename:)
  File.join(storage_path, 'uploads', filename)
end
```

This means, when a file called `import.tar.gz` would get uploaded, it would copy the temporary file to `/var/opt/gitlab/gitlab-rails/shared/tmp/project_exports/uploads/import.tar.gz`. Next, it'll schedule an async job in Sidekiq that'll take care of unpacking the import file and restore it's contents. However, since there's a delay between when the file gets copied and when the job gets processed (depending on how busy the workers are, etc.), someone else could upload a file with the same filename. If this happens before the import job gets processed, the victim will unknowingly overwrite the attacker's import file. When the attacker's Sidekiq job gets executed, it'll unpack the victim's import file and restore the files in the attacker's repository.

The entropy of a GitLab export file is decent enough to make this extremely hard to pull off. However, when someone would rename the file to something more common, for example a repository name, project name, or something generic like `import.tar.gz`, the changes of this happening increase.

To reproduce this vulnerability locally, it is easiest to shutdown the Sidekiq workers and upload two files with the same name under two different accounts. After that, restart the Sidekiq workers. You'll notice that both repositories hold the contents of the last imported file.

# Remediation advice
Generate a random filename instead of using the original filename or add the namespace and project URL to avoid file name collisions.

## Attachments
No attachments
