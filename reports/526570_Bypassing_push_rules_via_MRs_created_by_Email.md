# Bypassing push rules via MRs created by Email

## Report Details
- **Report ID**: 526570
- **URL**: https://hackerone.com/reports/526570
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-04-04T14:31:52.538Z
- **Disclosed**: 2019-10-01T11:03:04.209Z

## Reporter
- **Username**: xanbanx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hi GitLab Security Team,

GitLab EE has the feature of so-called push rules. An administrator, or more fine-grained per project, the owner can create certain push rules. The goal of these push rules is avoiding to push certain commits to the repository, which violate one of the push rules. If a commit violating one of the push rules is pushed to the repository, a pre-check gets executed, which decides a commit attempt should be rejected. Therefore, the user gets an error message indicating the commit does not follow the rules.

On the other hand, GitLab supports creating merge requests by writing an email address to a special address. If the email contains a `.patch` file as an attachment, the commits from this patch file are applied and pushed to the Repo. 

However, this step does not check for the push rules. This allows creating commits with content, that violates the configured push rules. It allows for example to push commits violating the commit message syntax, pushing an unsigned commit, pushing unwanted content (blacklisted secret files or bypassing regex), commits from unverified users, ...

## Steps to reproduce

Tested on GitLab.com 11.9.4-ee with a Gold Trial.

1. Create a repository with a Readme initialized
2. You then have to create one dummy merge request, e.g, by pushing some branch and create a new MR. The only purpose is that the empty state of `https://example.gitlab.com/<namespace>/<project>/merge_requests` does not show the incoming merge request email, which is required for the later steps.
3. Go to `https://example.gitlab.com/<namespace>/<project>/merge_requests`. At the bottom, there is a link opening a modal, which shows you the incoming merge request email. This email address looks similar to `incoming+<namespace>-<project-name>-<project-id>-<token>-request@incoming.example.gitlab.com`
4. Configure the push rules of the project under `https://example.gitlab.com/<namespace>/<project>/settings/repository`
   * Check `Committer restriction`
   * Check `Reject unsigned commits`
   * Check `Check whether author is a GitLab user`
   * Check `Prevent committing secrets to Git`
   * Change `Commit message` to `Fixes \d+\..*`
   * Change `Commit message negative match` to `ssh\:\/\`
   * Change `Commit author's email` to `@example.com$`
   * Change `Prohibited file names` to `(jar|exe)$`
5. Now clone the repo locally
6. In the local repo, create a branch named `bypass`, create a new file `test.exe` and a new file `id_dsa`
7. Add all created file to the git repo and commit it (unsigned) with the commit message `Bypassing push rules ssh://foo.bar`
8. Create a git patch of the last commit by using the command `git format-patch -n HEAD^`
9. Open the patch file and change the `From` line to e.g. `Lin Jen <lin@yen.com>`. Of course, you could also change the commit auther and commiter email git before. 
10. Create and send a new Email with the following content
  * Recipient address: Merge email address from above (Step 3)
  * Subject: bypass
  * Body: MR bypassing the push rules
  * Attachment: The patch file created before
11. The email created a new merge request with
  * a commit, which is unsigned <- violating the rule that othe commit message rulere accepted
  * a commit from Lin Jen (lin@yen.com) <- violating the author's email rule
  * a commit from Lin Jen (lin@yen.com) <- violating the rule that only verified emails can be used in pushed commits
  * a commit from Lin Jen (lin@yen.com) <- violating the rule whether the author is a GitLab user
  * a commit with message `Bypassing push rules ssh://foo.bar` <- violating the commit message rule
  * a commit with message `Bypassing push rules ssh://foo.bar` <- violating the commit message negative match
  * a file `test.exe` <- violating the prohibited file names rule
  * a file `id_dsa` <- violating the secrets rule

The only push rule, which seems to be enforced is the branch name push rule.

## Expected behavior

Push rules are enforced also for commits created by an email. The email should be rejected since it violates at least one push rule.

Best regards,
Xanbanx

## Impact

This allows anyone to bypass push rules set up by an administrator or project owner. This can lead to secrets being pushed to the repo, commits created by unknown users, etc

## Attachments
No attachments
