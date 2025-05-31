# Persistent XSS - Deleting a project (No Longer Vulnerable in 10.7)

## Report Details
- **Report ID**: 351554
- **URL**: https://hackerone.com/reports/351554
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-05-14T18:02:48.002Z
- **Disclosed**: 2018-09-20T20:02:52.445Z

## Reporter
- **Username**: phillycheeze
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
**Summary:**
When deleting a project in gitlab, it is possible to trigger a XSS with a malicious user name string.

**Description:**
I'd like to first point out that this is no longer vulnerable, but I filed a report anyways since it was never discovered. It looks like this was fixed on "accident". Originally, JS was rendering the username via a ".html()" jquery method, but was refactored to ".text()" and fixed the vulnerability.

I'm not sure how Gitlab would disclose this, but I have attached the exact commit that fixed the issue. This was done about a month ago, so I wanted to report this just in case Gitlab decides to update the release notes to point out that this was fixed. The original offending line was line 11 of the file in the commit below.

Commit: https://gitlab.com/gitlab-org/gitlab-ee/commit/2024aa5fa593e31b7c4aa30d107cc17d08b0a009

I ranked this a Medium since the number of users that are impacted are probably very low. For someone to become a victim, they must have Master access to a project that is under the malicious user's own account.

The steps to reproduce are fairly simple but there are some restrictions:
  * Only members of a project with Master access can become victims of the XSS.
  * The project must be under a personal "group", as in the project must be a personal project, not one under a custom group.

## Steps To Reproduce:
  1. Set your own username as "<img src=x onerror=alert(document.domain)> foo / bar"
  1. Under your own profile, create a new project.
  1. -- the steps below can render the XSS on yourself. To test another user, grant a second user to have Master access on this new project and run the same steps below. --
  1. Under Project Settings, General, Advanced Options, Danger Zone... click the Remove Project button.
  1. Notice the XSS renders on the modal that pops up asking for confirmation.

## Supporting Material/References:
More information can be provided upon request.

## Impact

The security impact is the same as any typical persistent xss. I lowered from High -> Medium because of the potential number of users impacted (described above).

The hacker selected the **Cross-site Scripting (XSS) - Stored** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://gitlab.com/group/project/edit

**Verified**
Yes



## Attachments
No attachments
