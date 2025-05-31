# Autoclose can close any task regardless of policies/spaces

## Report Details
- **Report ID**: 220909
- **URL**: https://hackerone.com/reports/220909
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-04-14T03:03:43.117Z
- **Disclosed**: 2017-04-24T04:20:25.148Z

## Reporter
- **Username**: almanac
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
# Description

If a user can push to a repository that has autoclose enabled, they can close //any// Maniphest task on the install, including tasks whose policies otherwise restrict the user from viewing or editing, and tasks inside Spaces that the user can't view.

I don't think this rises to the level of "security vulnerability." In particular, I don't think this is an issue on installs that operate like the upstream, where the repositories and projects are all related, and the developers who can push to the repositories are trusted throughout the install. On my install, though, the users are multiple, disparate teams who want to restrict access from each other, and they shouldn't be able to close each other's tickets. The only reason I'm filing here instead of as a normal bug report is so that in case there are other installs like mine, the issue doesn't become public before Phacility has a chance to review it.

# Steps to Reproduce

These steps involve an administrator and two users, Alice and Eve.

1. As an administrator:
  1. Create a repository R and configure it so that it's Visible To, Editable By, and Pushable By Eve, and Autoclose is On. OR Configure Diffusion's policies, setting the Default Edit Policy and Can Create Repositories to All Users.
  1. (Optional) Create a Space S, and make it visible to only Alice.
1. As Alice:
  1. Create a Maniphest task T. Set policies so it's Visible To and Editable By only Alice. If the administrator created Space S, then also make the task visible to Space S instead of the default space.
1. As Eve:
  1. Confirm that task T is not visible.
  1. If the administrator created repository R, then clone it. If instead the administrator configured Diffusion to allow anyone to create repositories, then create a new repository R with Autoclose turned On, and clone it.
  1. Commit something. The author can be anyone and doesn't need to be a Phabricator user. In the commit message, write something about a mongoose, and use autoclose syntax to close task T.
  1. Push the commit.
1. As Alice again:
  1. Confirm that task T has been closed despite policies and restricted spaces.
  1. Hunt down and destroy Eve. (Being hunted down and destroyed is probably a security vulnerability?)

# Versions

I reproduced this on a test instance on Phacility with the following versions:

* **phabricator:** 699ab153e3751e5389c69db4387d261e358de290 (Fri, Apr 7) (branched from 7707685733d26bf1c7278a2f338416a038c2709b on origin)
* **arcanist:** 3512c4ab86d66a103a6733a0589177f93b6d6811 (Fri, Apr 7) (branched from a59cfca5f190c44403dfc7449c678a2aa1626bb4 on origin)
* **phutil:** f568eb7b9542259cd3c0dcb3405cc9a83c90a2f5 (Mon, Apr 3) (branched from c581e769f10c6d2b427900897edba74e01a572bd on origin)
* **libcore:** 3eebdfca5b325792fdd2003a261e1ab94b919322 (Fri, Mar 24)
* **services:** 198eb67bd82296b6938d038836c7269c84bad98f (Feb 13 2017) (branched from 772620edd80ce593b104dba7721db42b9eb020a2 on origin)



## Attachments
No attachments
