# New /add_contacts /remove_contacts quick commands susseptible to XSS from Customer Contact firstname/lastname fields

## Report Details
- **Report ID**: 1578400
- **URL**: https://hackerone.com/reports/1578400
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-05-22T19:55:10.820Z
- **Disclosed**: 2022-11-16T01:07:35.198Z

## Reporter
- **Username**: cryptopone
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

In Gitlab 15.0.0 a new Customer Relations feature was added that allows us to use quick actions to find the contact we wish to select.

However, I noticed that if I set the contact's first name or last name to <script>alert(document.domain)</script> we can get the XSS to trigger when we are attempting to use the quick commands to add/remove a contact.

### Steps to reproduce

1. Create a new group.
1. Once the group is created, navigate to the Settings -> General options for the group.
1. Expand the section "Permissions and group features" and under "Customer Relations" make sure "Enable customer relations" is selected.
1. Return back to the group page. On the left side of the screen a new menu option will appear titled "Customer relations". Select it.
1. Create a new contact with "First name" set to "`<script>alert(document.domain)</script>`" and "Last name" set to "`<script>alert(document.domain)</script>`". Provide an email address and save your changes.
1. The user you created in the previous step should now appear as a contact on the Customer Relations page.
1. Go to the create new project URL (https://gitlab.com/projects/new#blank_project) and under Project URL, select the Group you created earlier. Give the project a name Ex. "CustomerProject".
1. Once the project has been created on the left side of the project page select "Issues" and then click "New Issue".
1. In the description pane type "/add_contacts" so the popup appears, then press "enter" to trigger the XSS.

### Impact

Users attempting to utilize the quick commands /add_contacts or /remove_contacts could inadvertently trigger XSS while attempting to add/remove a customer to an issue.

### Examples

This bug was discovered originally on my self-hosted 15.0.0 but is reproducible on gitlab.com.

Create a contact with the payload in firstname and lastname fields
{F1740002}

Create a new issue and type "/add_contacts" in the markdown text area to trigger the popup to appear
{F1740003}

Press enter, which will trigger the XSS when attempting to load the list of contacts
{F1740004}

### What is the current *bug* behavior?
The HTML special characters are not escaped, allowing an iframe to be injected into the page with XSS.

### What is the expected *correct* behavior?

The HTML special characters would be escaped and shown in the diagram.

### Output of checks

This bug is reproducible on Gitlab.com

#### Results of GitLab environment info

```System information
System:         Ubuntu 20.04
Proxy:          no
Current User:   git
Using RVM:      no
Ruby Version:   2.7.5p203
Gem Version:    3.1.4
Bundler Version:2.2.33
Rake Version:   13.0.6
Redis Version:  6.2.6
Sidekiq Version:6.4.0
Go Version:     unknown

GitLab information
Version:        15.0.0-ee
Revision:       3b397c17532
Directory:      /opt/gitlab/embedded/service/gitlab-rails
DB Adapter:     PostgreSQL
DB Version:     12.10
URL:            http://gitlab-pentest4.example.com
HTTP Clone URL: http://gitlab-pentest4.example.com/some-group/some-project.git
SSH Clone URL:  git@gitlab-pentest4.example.com:some-group/some-project.git
Elasticsearch:  no
Geo:            no
Using LDAP:     no
Using Omniauth: yes
Omniauth Providers:

GitLab Shell
Version:        14.3.0
Repository storage paths:
- default:      /var/opt/gitlab/git-data/repositories
GitLab Shell path:              /opt/gitlab/embedded/service/gitlab-shell```

## Impact

JavaScript execution as the authenticated user when the user attempts to add or remove a contact for the new customer relations feature.

## Attachments
- Customer_Contact.png
- add_contacts_popup.png
- add_contact.png
