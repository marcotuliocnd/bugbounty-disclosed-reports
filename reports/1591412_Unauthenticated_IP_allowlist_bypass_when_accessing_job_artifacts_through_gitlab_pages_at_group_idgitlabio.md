# Unauthenticated IP allowlist bypass when accessing job artifacts through gitlab pages at `{group_id}.gitlab.io`

## Report Details
- **Report ID**: 1591412
- **URL**: https://hackerone.com/reports/1591412
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-06-04T21:45:07.939Z
- **Disclosed**: 2022-09-22T21:31:20.421Z

## Reporter
- **Username**: joaxcar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
## Summary

An owner of a group can restrict access to the group, subgroups and projects to only work from a specific IP range. See documentation [link](https://docs.gitlab.com/ee/user/group/#restrict-group-access-by-ip-address)

> To ensure only people from your organization can access particular resources, you can restrict access to groups by IP address.

This will restrict most actions, but have some caveats described in the documentation (which we will use to leak job IDs).

One thing that is restricted is access to pipeline job artifacts, both through the API and through the UI. But there exists a feature in GitLab that is used to "preview" HTML artifacts safely. GitLab exposes pipeline job artifacts for preview under the `pages` domain gitlab.io

What I have seen, this is for rendering HTML files, but it gives access to the complete artifact. This endpoint is not restricted by the IP block, and thus leaks job artifacts to users outside the IP range. Given that the IP block should restrict the group from users outside the IP range there is a high risk that projects protected this way have visibility `Public`, when this is the case these `artifacts` are leaked to `unathenticated` users outside the IP range.

To view the artifact files, a user would need access to the ID of the pipeline job. This makes the attack harder to pull off. But as IP restricted groups/projects are a bit leaky with their information, these IDs can be found in different ways. One way the job ID is leaked is through email notifications. If a user have enabled notifications on "pipeline finished" on the IP blocked project, then these job IDs will get sent to the user's email when a pipeline have finished. The user can then access the artifacts from any IP using the job ID from the email.

There might be other places where job IDs leak out. But the important thing is that the data is accessible to anyone with the link.

## Steps to reproduce

1. Create a user called `victim` and log in to Gitlab.com
2. Create a `public` group with at least `Premium` subscription (create an ultimate trail if needed), lets call it `group01`
3. Create a `public` project in the group, lets call it `project01`
4. In the project create two files
hidden.json
```json
{
   "hidden": "hidden"
}
```
and .gitlab-ci.yml
```yml
data:
  artifacts:
    paths:
    - ./
    expire_in: 2 weeks
```
5. When the files are created a pipeline job will run.
6. Go to gitlab.com/group01/project01/-/pipelines and click on the button `status done`, click on the job `data` and then on "browse" under job artifacts
7. You should now be able to click and download the artifact file. The URL should look like
```
https://gitlab.com/group01/project01/-/jobs/2493429745/artifacts/browse
```
and the file should be accessible like
```
https://gitlab.com/group01/project01/-/jobs/2493429745/artifacts/file/hidden.json
```
8. Now go to group settings https://gitlab.com/groups/group01/-/edit and expand "Permissions and group features"
9. Scroll down to "Allow access to the following IP addresses" and enter 1.1.1.1 and click enter (as owner you will always have access to this settings page so dont worry about the IP)
10. Click save
11. Now go back to the artifact URL and file URL and see that you will get a 404 error, no access anymore
12. Now go to (change the ID)
```
https://group01.gitlab.io/-/project01/-/jobs/2493429745/artifacts/hidden.json
```
13. You should see the content of the artifact file!
14. Open a new browser, or log out, visit the same site. The artifact is shown unauthenticated

## Impact

Users can access pipeline job artifacts in groups from restricted IP addresses

## Examples

This is a public project with an IP restriction. You should not be able to see the files

https://gitlab.com/joaxcarultimate3/teat3/-/jobs/2547216908/artifacts/browse

This is the hidden file accessible to anyone, any IP

https://joaxcarultimate3.gitlab.io/-/teat3/-/jobs/2547216908/artifacts/hidden.json

## What is the current *bug* behavior?

Pipeline job artifacts are exposed without IP restriction on gitlab pages domain

## What is the expected *correct* behavior?

The files should not be exposed

## Output of checks

This bug happens on GitLab.com

## Impact

Pipeline artifacts are leaked from IP restricted groups to possible unauthenticated users

## Attachments
No attachments
