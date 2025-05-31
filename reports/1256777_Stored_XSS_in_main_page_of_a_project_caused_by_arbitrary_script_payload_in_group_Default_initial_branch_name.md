# Stored XSS in main page of a project caused by arbitrary script payload in group "Default initial branch name"

## Report Details
- **Report ID**: 1256777
- **URL**: https://hackerone.com/reports/1256777
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-07-10T09:40:15.310Z
- **Disclosed**: 2021-09-15T13:44:00.162Z

## Reporter
- **Username**: joaxcar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

A stored XXS exists in the main page of a `project`. By changing the "default branch name" of a group a malicious user can inject arbitrary JavaScript into the main page of a project. Any user that is either at least developer of the project, or an administrator of the GitLab instance, and access the project URL will trigger the payload.

The field "default branch name" under https://gitlab.com/groups/group_name/-/settings/repository accepts arbitrary text (long JavaScript strings as an example). When a project without a initial repository is created in the group the developers are presented with an information page with example terminal commands to execute to set up a repository. This information includes two unzanatized inclusions of the "default branch name", resulting in execution of the JavaScript payload.
{F1371756}

As a default self-hosted GitLab instance does not enforce any CSP rules any javascript can be called. Including inclusion of external script files (<script src="external_script"></script>). On GitLab.com I have not been able to bypass the CSP except from changing the `base-uri` which causes all links on the page(including navigation bars) to point to the attackers site (with payload `<Base Href="attacker_site">`).

On a self-hosted instance without proper CSP I was able to generate `personal access tokens` from the victim that could be extracted by the attacker to get complete access to the victims content and actions. If the victim is an Administrator this leads to complete access to the system. (I will post a script PoC when I have cleaned it up)

As I mentioned, the victim needs to be at least a `Developer` on the project (if not a site admin) when accessing the project main page. This is not a problem (rather an asset) for the attacker. All the attacker needs to do is invite targeted victim users as `Developers` to the project. This will trigger GitLab to send out information to the victim (emails or notifications) that will work as validated phishing links (see image below). The victim just need to click the link in the email and land on the project main page.
{F1371755}

### Steps to reproduce

1. Create two users, `attacker01` and `victim01`
2. Log in as `attacker01`
3. Create a group `attack_group` by visiting https://gitlab.domain.com/groups/new#create-group-pane
4. Go to https://gitlab.domain.com/groups/attack_group/-/settings/repository and expand the "Default initial branch name" tab
5. Enter `<script>alert(1);</script>` as "Default initial branch name" and click "save changes"

{F1371757}

6. Go to https://gitlab.domain.com/groups/attack_group and click the button "New project" and choose to create a "Create blank project"
7. Name the project `attacking_project` and click "Create project"
8. Now the project will load and the alert should pop up.

{F1371758}

optional:
9. On the project main page click the "Invite members" button and invite `victim01` as a Developer
10. Log in with `victim01`
11. Visit https://gitlab.domain.com/attack_group/attacking-project and the script will run for the victim as well

### Impact

Stored XXS capable of arbitrary script execution. Impact depends on the instance CSP settings.

### Examples

If an administrator of GitLab.com visit https://gitlab.com/attack_xxs_group/test3 (a private group and project) one can see that ALL links on the site (all navigation and actions) are redirected to google.com. This is caused by the payload `<Base Href="//www.google.com">`

### What is the current *bug* behavior?

Arbitrary JavaScript is executed on a project main page

### What is the expected *correct* behavior?

The branch name should be sanitized and checked for bad input, and the included branch name should be sanitized when displayed.

### Output of checks

This bug happens on GitLab.com

But CSP removes most of the impact

#### Results of GitLab environment info

I did not manage to run the environment script. I tried this on a Azure hosted GitLab server created from the Azure store.

## Impact

Stored XXS capable of arbitrary script execution. Impact depends on the instance CSP settings. If CSP is not properly set the attacker can execute arbitrary commands as the victim and/or generate `personal access tokens` for full account access. If an Administrator gets compromised, this could lead to complete instance access.

On GitLab.com an attacker can change the `base-uri` to make all links redirect to the attacker's site

## Attachments
- email.png
- info.png
- input.png
- popup.png
