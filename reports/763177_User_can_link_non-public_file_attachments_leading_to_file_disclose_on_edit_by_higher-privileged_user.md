# User can link non-public file attachments, leading to file disclose on edit by higher-privileged user

## Report Details
- **Report ID**: 763177
- **URL**: https://hackerone.com/reports/763177
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-22T12:58:26.335Z
- **Disclosed**: 2022-06-26T18:25:25.860Z

## Reporter
- **Username**: foobar7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
CVSS
----

Medium 6.5 [CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N)

Description
-----------

Uploaded files can be linked to from anywhere by referencing their ID. If the user viewing the reference to the file has permission to access the file, it will be rendered. Otherwise, the reference will be displayed as text.

If a user references a file from a private location in a public location, the file permissions will silently be updated and the file will be made available publicly as well (if the user has permission to access the file; otherwise, permissions will remain unchanged).

This behavior results in problems when a higher-privileged user edits the post of a lower-privileged user which contains a reference to a private file. The file will be disclosed publicly, without the user intending this or being aware of it.

POC
---

Setup:

- Create a private task (task is just one example, all components are affected by this): `/maniphest/` -> create task -> Visible to / Editable by: administrators (or some other high-privileged group).
- Add an attachment: leave a comment -> Upload file. Note the file ID.

Attack:

- With a lower-privileged user, create a public task (or some other component): `/maniphest/` -> create task -> Include a reference to the private file in the description, eg `{F27}`. Include some formatting mistakes, typos, profanity, etc to entice a higher-privileged user into editing the post.
- Wait for a higher-privileged user viewing the task. The user will see the file attachment resolve normally, edit the task and fix the formatting error. Nothing will indicate that a private file has been made public.
- After the user has edited the post, the file will be available to the lower-privileged user.

## Impact

disclosure of private file attachments when a user with access to the attachment edits a post of a user without access to it.

## Attachments
No attachments
