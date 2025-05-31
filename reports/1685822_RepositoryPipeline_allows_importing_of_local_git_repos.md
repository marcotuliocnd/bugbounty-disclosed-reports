# RepositoryPipeline allows importing of local git repos

## Report Details
- **Report ID**: 1685822
- **URL**: https://hackerone.com/reports/1685822
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-08-30T19:01:01.925Z
- **Disclosed**: 2022-11-04T03:43:34.930Z

## Reporter
- **Username**: vakzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

When importing a project via the BulkImports, the response field `httpUrlToRepo` from the client is used to fetch the repo:

https://gitlab.com/gitlab-org/gitlab/-/blob/v15.3.1-ee/lib/bulk_imports/projects/pipelines/repository_pipeline.rb#L17
```ruby
        def load(context, data)
          url = data['httpUrlToRepo']
          return unless url.present?

          url = url.sub("://", "://oauth2:#{context.configuration.access_token}@")
          project = context.portable

          Gitlab::UrlBlocker.validate!(url, allow_local_network: allow_local_requests?, allow_localhost: allow_local_requests?)

          project.ensure_repository
          project.repository.fetch_as_mirror(url)
        end
```

`Gitlab::UrlBlocker.validate` is called, but since no schemas are passed in it allows any (such as file) so long as the rest of the url is valid.

This means that if a url such as `file://aw.rs/var/opt/gitlab/git-data/repositories/@hashed/b1/74/b174103b399555239923697fbe124faa61de4d441bd5c5678275eb0a5a27a562.git` is supplied, this will end up being used by git fetch, eg:

```bash
$ git fetch file://aw.rs/var/opt/gitlab/git-data/repositories/@hashed/b1/74/b174103b399555239923697fbe124faa61de4d441bd5c5678275eb0a5a27a562.git
fatal: '/var/opt/gitlab/git-data/repositories/@hashed/b1/74/b174103b399555239923697fbe124faa61de4d441bd5c5678275eb0a5a27a562.git' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

This allows an attacker to import any local repository that the current machine has access to if the path is known.

The storage path for projects in gitlab is just based on a configurable folder combined with a bucketed sha2 hash of  the id, eg for project 38006449 the `Digest::SHA2.hexdigest("38006449")` is  `b174103b399555239923697fbe124faa61de4d441bd5c5678275eb0a5a27a562` so the path will be at `@hashed/b1/74/b174103b399555239923697fbe124faa61de4d441bd5c5678275eb0a5a27a562.git`.

This can then be used to import any gitlab repository via the project id by calculating the path, such as the gitlab ctf project!

`{gitlab-bounty-flag-7a3f26698d2ef146843d7209e5efc8ec}`


### Steps to reproduce

1. Create a private project with User A and edit the readme file, make note of the project id
1. Download {F1892171} and edit line 99 with the new path to the repository above (replace `b1/74/b174103b399555239923697fbe124faa61de4d441bd5c5678275eb0a5a27a562` with the new `sha2[0:2]/sha2[2:4]/sha2`)
1. Run the server with `FLASK_APP=fake_server.py FLASK_ENV=development flask run`
1. Start ngrok with `ngrok http 500`
1. User B, visit https://gitlab.com/groups/new#import-group-pane and enter your ngrok url, any token and hit connect
1. In the browser console,  replace `"destination_namespace":"vakzz"` with your gitlab username (or a group you have access too) in the code below and run it:

  ```javascript
await fetch("/import/bulk_imports.json", { method: "POST", headers: { "X-CSRF-Token": document.querySelector("[name=csrf-token]").content, "Content-Type": "application/json" }, body: `{"bulk_import":[{"source_type":"project_entity","source_full_path":"group1/project1","destination_namespace":"vakzz","destination_slug":"some_project_z_${Math.floor(Math.random() * 10000)}"}]}` });
  ```

1. After a few minutes you should see a new project appear
1. Initially it will just show `No repository`
1. After another minute or so the project will either show `The repository for this project is empty`  or it will be a clone of the project from User A
1. If you see `The repository for this project is empty` then just repeat the fetch call again, it can take a few tries to end up on the same server as the victim (I think that's what is happening)

This can also be done with a Helm install of gitlab using the base path of `/home/git/repositories` or using the omnibus edition, but you will need to check where the repositories are located on disk and use that as the base path.
 
### Impact

Allows an attacked to clone any repo on gitlab with just the project id

### Examples

Example of me cloning the gitlab ctf project - https://gitlab.com/vakzz-h1/secret_ctf_5401/-/blob/main/you/found/id/flag.txt

### What is the current *bug* behavior?

The `RepositoryPipeline` allows for arbitrary url protocols to be passed to `project.repository.fetch_as_mirror(url)`

### What is the expected *correct* behavior?

It should be restricted to https/git/ssh

### Relevant logs and/or screenshots
{F1892192}
### Output of checks

This bug happens on GitLab.com

## Impact

Allows an attacked to clone any repo on gitlab with just the project id

## Attachments
- fake_server.py
- image.png
- IntrospectionQuery.json
