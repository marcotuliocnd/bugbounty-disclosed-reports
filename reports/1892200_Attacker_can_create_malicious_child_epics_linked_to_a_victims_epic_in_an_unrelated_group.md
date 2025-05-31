# Attacker can create malicious child epics linked to a victim's epic in an unrelated group

## Report Details
- **Report ID**: 1892200
- **URL**: https://hackerone.com/reports/1892200
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-03-04T19:21:15.426Z
- **Disclosed**: 2023-06-02T01:55:38.542Z

## Reporter
- **Username**: cryptopone
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

An attacker with the capabilities to create multi-level epics (requires Ultimate license) may create malicious children epics by referring to a victim's epic via the parent_id. This is done through the REST api via the attacker's endpoint (https://gitlab.example.com/api/v4/groups/attackergroup/epics). The attacker can obtain the victim ID without being a member of the victim's group if the victim uses Public/Internal visibility.

It is also possible to add child epics to private groups, and although the attacker would have to guess or know the epic id and while no confidential information is leaked initially, a victim may still navigate to the attacker's epic and leak information that way.

### Steps to reproduce

Note: Attacker requires BurpSuite and an Ultimate license and Victim may also need Ultimate (but maybe just Premium?). The attacker needs the ultimate license to create "Multi-level epics" but victim may need it too (I am unable to verify at this time as my whole self-hosted instance is licensed as Ultimate).

#### Victim
1. Log into GitLab and create a new group called "VictimEpicGroup" with internal or public visibility (https://gitlab.example.com/groups/new#create-group-pane).
1. Create an epic inside of the group created from Step 1 called "Public Victim Epic" (https://gitlab.example.com/groups/victimepicgroup/-/epics/new).

#### Attacker
1. Log into GitLab and create a new group called "AttackerEpicGroup" with internal or public visibility (https://gitlab.example.com/groups/new#create-group-pane).
1. Create an epic inside of the group created from Step 1 called "Attacker Public Epic" (https://gitlab.example.com/groups/attackerepicgroup/-/epics/new).
1. Navigate to the Victim's epic to obtain the global epic id (https://gitlab.example.com/groups/victimepicgroup/-/epics/1).
1. View page source and search for "gid://gitlab/Epic". One of the first results will be similar to:
```html
<button aria-label="Add a to do" issuable-type="epic" issuable-id="gid://gitlab/Epic/29" type="button" class="btn hide-collapsed btn-default btn-sm gl-button" size="small"><!----> <!---->  <span class="gl-button-text">  Add a to do </span></button>
``` 
(in this case the attacker is targeting `29`).

5. Navigate to the attacker's epic created in step 2 (https://gitlab.example.com/groups/attackerepicgroup/-/epics/1).
6. In the "Child issues and epics" section click "Add" -> "Add a new epic".
7. Set the title to "Attacker Child Epic" and group to "AttackerGroup".
8. Set BurpSuite to intercept requests via "Proxy" -> "Intercept" and ensure the intercept button states "Intercept is on".
9. Back in the browser window click "Create epic".
10. Intercept the POST request to `/api/v4/groups/attackerepicgroup/epics` in BurpSuite.
11. Update `parent_id` in the POST body from the current value to the victim's value in step 4 (In this example use `29`).
For example, if the body contains:
```json
{"parent_id":30,"confidential":false,"title":"Attacker Child Epic"}
```

Update the parent_id so the request looks like:
```json
{"parent_id":29,"confidential":false,"title":"Attacker Child Epic"}
```
12. Click forward to send the request and intercept can now be turned off.
13. Note the epic is created successfully.

#### Victim
1. Navigate to the epic the victim created earlier (https://gitlab.example.com/groups/victimepicgroup/-/epics/1).
1. Note the attacker's epic is now associated to the epic as a child.
1. Click on the attacker's epic and notice the URL of the page is now within the attacker's group/control.

### Impact

An attacker is able to create an attacker controlled epic linked to a victim's epic inside of a separate group not controlled by the attacker.

My initial report uses the following reasoning for the CVSS score:
* `AC:L`: IDOR using simple guessable ID - Attacker can find the epic ID with public/internal projects or if they previously obtained the id from a private project they no longer have access to.
* `PR:L`: Attacker requires an account but does not necessarily require roles within the victim's group.
* `UI:N`: Attacker is able to create the child epic linked to the victim without requiring action from the victim.
* `S:U`: Impact is localized to the exploitable component.
* `C:N`: No confidential information is disclosed.
* `I:L`: Victim is able see the association to the attacker's child epic and may trust/navigate to the attacker's group when clicking on it.
* `A:N`: No Availability impact.

### Examples

I have not tested this bug on GitLab.com as I do not have two ultimate accounts to test with at this time.

The following group exports help demonstrate the parent_id link with the attacker's epic.

Attacker Epic Group - Export
F2209069

Victim Epic Group - Export
F2209070

### What is the current *bug* behavior?

An attacker using their own group is able to create new epics that are linked to a victim's epic (via parent_id) where they have no privileges.

### What is the expected *correct* behavior?

When an attacker creates an epic and specifies a parent_id for an epic inside of a group they do not have rights for, the server should return an error.

### Relevant logs and/or screenshots

Demonstration of an attacker creating a child epic and linking to an unrelated victim epic
{F2209041}

### Output of checks

#### Results of GitLab environment info

```
System information
System:		Ubuntu 22.04
Proxy:		no
Current User:	git
Using RVM:	no
Ruby Version:	2.7.7p221
Gem Version:	3.1.6
Bundler Version:2.3.15
Rake Version:	13.0.6
Redis Version:	6.2.8
Sidekiq Version:6.5.7
Go Version:	unknown

GitLab information
Version:	15.9.2-ee
Revision:	d80458522dd
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	13.8
URL:		http://gitlab.cryptopone.com
HTTP Clone URL:	http://gitlab.cryptopone.com/some-group/some-project.git
SSH Clone URL:	git@gitlab.cryptopone.com:some-group/some-project.git
Elasticsearch:	no
Geo:		no
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers: 

GitLab Shell
Version:	14.17.0
Repository storages:
- default: 	unix:/var/opt/gitlab/gitaly/gitaly.socket
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
```

## Impact

An attacker is able to create an attacker controlled epic linked to a victim's epic inside of a separate group not controlled by the attacker.

My initial report uses the following reasoning for the CVSS score:
* `AC:L`: IDOR using simple guessable ID - Attacker can find the epic ID with public/internal projects or if they previously obtained the id from a private project they no longer have access to.
* `PR:L`: Attacker requires an account but does not necessarily require roles within the victim's group.
* `UI:N`: Attacker is able to create the child epic linked to the victim without requiring action from the victim.
* `S:U`: Impact is localized to the exploitable component.
* `C:N`: No confidential information is disclosed.
* `I:L`: Victim is able see the association to the attacker's child epic and may trust/navigate to the attacker's group when clicking on it.
* `A:N`: No Availability impact.

## Attachments
- AttackerCreatingChildEpic.mp4
- attackerepicgroup_export.tar.gz
- victimepicgroup_export.tar.gz
