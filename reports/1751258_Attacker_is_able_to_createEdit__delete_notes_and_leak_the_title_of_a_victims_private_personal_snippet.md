# Attacker is able to create,Edit & delete notes and leak the title of a victim's private personal snippet

## Report Details
- **Report ID**: 1751258
- **URL**: https://hackerone.com/reports/1751258
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-10-25T23:29:24.725Z
- **Disclosed**: 2023-06-02T01:57:09.182Z

## Reporter
- **Username**: cryptopone
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

An attacker is able to create new notes for a victim's private personal snippet. This attack leaks the title of the snippet on the attacker's activity page. The attacker is also able to edit/delete the note using the "id" value that is returned from the server after creating the comment, as they are the owner for the note.

I believe this attack is achieved by utilizing https://gitlab.com/gitlab-org/gitlab/-/blob/master/app/finders/notes_finder.rb when posting a comment within a project they control.

```ruby
  def noteables_for_type(noteable_type)
    case noteable_type
    when "issue"
      IssuesFinder.new(@current_user, project_id: @project.id).execute # rubocop: disable CodeReuse/Finder
    when "merge_request"
      MergeRequestsFinder.new(@current_user, project_id: @project.id).execute # rubocop: disable CodeReuse/Finder
    when "snippet", "project_snippet"
      SnippetsFinder.new(@current_user, project: @project).execute # rubocop: disable CodeReuse/Finder
    when "personal_snippet"
      PersonalSnippet.all
    else
      raise "invalid target_type '#{noteable_type}'"
    end
  end
```
By changing the POST parameter noteable_type from "issue" to "personal_snippet" the server doesn't perform the project check when attempting to create the note and as a result the comment is posted to the victim's personal snippet.

### Steps to reproduce

Reproduction steps require two accounts representing an attacker and a victim

#### Victim Setup:
1. Log in and navigate to https://gitlab-instance.example.com/dashboard/snippets then click the "New snippet" button.
1. Set the title of the Personal Snippet to "Private Victim Snippet", and supply a filename (ex. "test-victim-file.txt") with file contents "test file contents".
1. Ensure the visibility level is set to "Private" and click "Create Snippet".
1. Make a note of the ID for the snippet in the URL bar. We will refer to this value as VICTIM_SNIPPETID. The attacker will need it in their steps.

#### Attacker Setup and Create New Note on Personal Snippet:
1. Log in to GitLab and navigate to https://gitlab-instance.example.com/dashboard/projects and create a new private project for the attack (I named mine "PrivateAttackerProject").
1. Create a new issue (I created an issue with title "Attacker Issue").
1. Open up the issue that was just created (ie. https://gitlab-instance.example.com/attacker/privateattackerproject/-/issues/1).
1. Scroll down to "Activity" and create a new note. I used the text `@attacker was here`.
1. Prepare BurpSuite to intercept the request and then click "Comment". We want the request that looks like `/attacker/privateattackerproject/notes?target_id=6&target_type=issue` with post body looking like `{"note":{"noteable_type":"Issue","noteable_id":6,"internal":false,"note":"@attacker was here"}}`.
1. Send the intercepted POST request to Burp Repeater for easier testing.
1. Update target_type in the target resource from `target_type=issue` to `target_type=personal_snippet`.
1. Set the target_id in the target resource from `target_id=6` to `target_id=VICTIM_SNIPPETID` (Replacing VICTIM_SNIPPETID with the id that was generated for the victim).
1. The POST request should now look similar to `POST /attacker/privateattackerproject/notes?target_id=VICTIM_SNIPPETID&target_type=personal_snippet HTTP/2`
1. Send the request and review the response. A new note will be created under the private snippet.

#### Attacker editing a note they created previously
Note: When the attacker creates the note in the previous steps, an id value is returned in the response. This can also be obtained by the victim by copying the link to the note and making a note of the id (ex. https://gitlab-pentest2.example.com/-/snippets/3#note_7)
1. Have the attacker create a new note within the issue they created. We can then edit/delete this note and intercept the request in BurpSuite.
1. To edit the note on the personal snippet:
Take the original edit request:
```
PUT /attacker/privateattackerproject/notes/8 HTTP/2
Host: gitlab-pentest2.example.com
<Rest of headers>

{"target_type":"issue","target_id":7,"note":{"note":"test2"}}
```

Modify the body of the post so '"target_type"="personal_snippet"' and '"target_id"=VICTIM_SNIPPETID'

```
PUT /attacker/privateattackerproject/notes/8 HTTP/2
Host: gitlab-pentest2.example.com
<Rest of headers>

{"target_type":"personal_snippet","target_id":3,"note":{"note":"test2"}}
```

#### Attacker deleting a note they created previously
1. To delete the note on the personal snippet:
Take the original delete note request:
```
DELETE /attacker/privateattackerproject/notes/8 HTTP/2
Host: gitlab-pentest2.example.com
<Rest of headers>
```
Update the id in the request to point to the note id in the personal snippet (Attacker must be the owner of the note).

```
DELETE /attacker/privateattackerproject/notes/7 HTTP/2
Host: gitlab-pentest2.example.com
<Rest of headers>
```

### Impact

If the victim refreshes the snippet they will see a comment from the attacker. If the attacker visits their profile page (ie. https://gitlab-pentest2.example.com/attacker) and views activity, they will confirm if they reached the comment and can obtain the title of the private snippet.

Since snippet ids are sequential, an attacker could in theory create a snippet, then iterate from 1 to the snippet number of their own snippet and obtain the titles of all personal snippets.

The attacker is also able to update a note they have created and modify text and/or delete the note itself by intercepting the "Edit comment" and "Delete comment" requests within the issue and repeating the steps above. The attacker could delete their notes after collecting the titles for example to cover their tracks.

If the attacker makes their project public or internal and uses a label or references the issue in the comment, the victim will be able to see the label from the attacker's project. This helps provide further proof of a successful attack and may be used for social engineering.

### Examples

This bug is also reproducible on GitLab.com
Victim Snippet: https://gitlab.com/-/snippets/2436054
Attacker Issue: https://gitlab.com/Cryptopone/MyPrivateProject/-/issues/1

### What is the current *bug* behavior?

When the attacker posts a note to the victim's private snippet, the attacker will be able to obtain the title of the snippet. 

### What is the expected *correct* behavior?

The server should return an error message when attempting to create a note for a personal snippet the attacker does not own.

### Relevant logs and/or screenshots

Attacker viewing their activity page to obtain the title of the victim's private personal snippet.
{F2003894}

Victim seeing notes that have been posted by an attacker. Note the linked issue links back to the attacker's project where they conducted the attack.
{F2003895}

### Output of checks

This bug happens on GitLab.com)

#### Results of GitLab environment info

```
System information
System:         Ubuntu 20.04
Proxy:          no
Current User:   git
Using RVM:      no
Ruby Version:   2.7.5p203
Gem Version:    3.1.6
Bundler Version:2.3.15
Rake Version:   13.0.6
Redis Version:  6.2.7
Sidekiq Version:6.4.2
Go Version:     unknown

GitLab information
Version:        15.5.1-ee
Revision:       7344dd2631a
Directory:      /opt/gitlab/embedded/service/gitlab-rails
DB Adapter:     PostgreSQL
DB Version:     12.10
URL:            https://gitlab-pentest2.example.com
HTTP Clone URL: https://gitlab-pentest2.example.com/some-group/some-project.git
SSH Clone URL:  git@gitlab-pentest2.example.com:some-group/some-project.git
Elasticsearch:  no
Geo:            no
Using LDAP:     no
Using Omniauth: yes
Omniauth Providers:

GitLab Shell
Version:        14.12.0
Repository storage paths:
- default:      /var/opt/gitlab/git-data/repositories
GitLab Shell path:              /opt/gitlab/embedded/service/gitlab-shell
```

## Impact

When the attacker posts a note to the victim's private snippet, the attacker will be able to obtain the title of the snippet. 

If the attacker makes their project public or internal and creates a note with a label or references to an issue in the comment, the victim will be able to see the label from the attacker's project. This could be used as a social engineering vector to obtain the file contents of a snippet (or simply scare the victim into thinking the snippet is public).

## Attachments
- AttackerActivityProof.png
- VictimProof.png
