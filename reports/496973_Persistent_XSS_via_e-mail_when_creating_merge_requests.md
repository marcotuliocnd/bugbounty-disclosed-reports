# Persistent XSS via e-mail when creating merge requests

## Report Details
- **Report ID**: 496973
- **URL**: https://hackerone.com/reports/496973
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-02-16T07:34:25.515Z
- **Disclosed**: 2019-08-30T23:27:28.304Z

## Reporter
- **Username**: mario-areias
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
**Summary:**
The vulnerability consists in the ability to create branch names that contain characters such as `<>/`. This branch name is sent via e-mail which is rendered as HTML.

**Description:**
One way to exploit this is by forking a repository. Then an attacker would create a branch called `<script>alert(1)</script>` and make a simple change. Now the attacker creates a merge request to the original repository and assign a reviewer to it. The reviewer will receive the e-mail with the branch name not sanitised. 

Another way to exploit is to by adding Gitlab users to a repository the attacker controls and assign them to review merge requests.

## Steps To Reproduce:

Note: These instructions work on GDK with the latest version. I wasn't sure if it is allowed to test something like on gitlab.com

  1.  Choose a public repository and fork it (let's say HTML5 boilerplate)
  2. Go through the repository main page http://yourserver:3000/root/html5-boilerplate
  3. Click on the button + button and select New File
  4. Create any file but choose a different target branch (something like <script>alert(1)</script>
  5. Gitlab will direct you to a page to create a new merge request from your recently create branch to master. Ignore that.
  6. Open a New Merge Request
  7. Select Source Branch as your fork and the recently created branch
  8. As for Target branch select the original repo and master
  9. Click submit
10. Select one the maintainers of the original repo 
11. Submit
12. Go to letter opener (/rails/letter_opener/)
13. See the alert popping up.

The steps above only require UI, but an attacker can create a branch name through git client as well. The create branch option UI protects against this attack.

There is also another version of the attack, where a repository owner can add any Gitlab users to become members of her repo. The attacker now create a Merge Request in his own repo and assign the new member to it. Same result. 

## Supporting Material/References:

* Vulnerable code at `gitlab-ce/app/views/notify/new_merge_request_email.html.haml` line 6. This is the exploit above.
* Vulnerable code at `gitlab-ce/app/views/notify/repository_push_email.text.haml` line 49. I haven't created an exploit for this one, but I would assume it should be similar.

## Impact

E-mail clients nowadays are well protected against XSS. However, a malicious user could use Gitlab's name to mislead users. The problem with this vulnerability is the reach. It is my understanding, an attacker can add whoever is a Gitlab user as a member of her own repo. So she could send malicious e-mails to them. I would usually say that is a low vulnerability, however, given the number of users that could be affected I would say is a medium

## Attachments
No attachments
