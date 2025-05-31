# HackerOne Jira integration plugin Leaked JWT to unauthorized jira users

## Report Details
- **Report ID**: 1103582
- **URL**: https://hackerone.com/reports/1103582
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-15T11:12:14.471Z
- **Disclosed**: 2021-04-01T19:41:43.004Z

## Reporter
- **Username**: updatelap
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
HackerOne provides an application tool [HackerOne for Jira](https://marketplace.atlassian.com/vendors/1214355/hackerone), an application that allows programs to track security issues through a jira instance. After testing the integration feature in the application, it was found that the application leads to the leakage of the `JWT` to unauthorized users.

### About jira:

Jira Cloud allows the system administrator to add users with different Roles such as "__Basic, Trusted, and Site administrator__" with the highest authority being "Site administrator" and least "Basic". Based on these Roles allows:

1. The administrator can fully manage the account by accessing all projects, issues, dashboards and configuring applications.
2. Access to specific projects or issues. It is not possible to access to configure applications or to change any of the account settings.

**Description:**
As we mentioned earlier, the HackerOne for Jira application, after installing it, creates an integration between the HackerOne platform and the atlassian where cases can be synchronized from HackerOne to atlassian
  And vice versa. So, after installation, __administrators__  jira account is allowed to go https://YOUDOMIN.atlassian.net/plugins/servlet/ac/com.hackerone/get-started-with-hackerone-on-jira When going to this page, the following message will appear:

{F1196098}

When you click on "click here", you will be directed to a link  this "`https://hackerone.com/apps/atlassian/claim-app?jwt=<TOKEN>`" containing JWT parameter to complete the integration process. So. Based on the __About jira description__, an employee with "`BSSIC`" privileges is not allowed to access the application configuration.  After testing if the [HackerOne for Jira](https://marketplace.atlassian.com/vendors/1214355/hackerone) app. checks the permissions of Jira users before providing the user with the `JWT`, it is found that the  [HackerOne for Jira] application does not verify the user's permissions and generates the JWT code for a user with `basic privileges`. This allows this malicious user to link their hackerone account to an instance of a jira that they do not own. Which leads, for example, to leak names of private projects or create issues in private projects .. etc

{F1196129}

The normal or expected behavior that the tool should work with is to verify the role of the user who requests the configuration page, and if he does not have the privilege to display the page, a message similar to this should appear.
{F1196135}

### Steps To Reproduce

1. Go to Jira cloud and create jira instance.
2. Add user with `Basic` roles.
1. The administrator creates 8 projects and is restricted to accessing 5 projects for the administrator only.
3. Admin Install [HackerOne for Jira](https://marketplace.atlassian.com/vendors/1214355/hackerone) app.
4. User Go to {BaseUrl}/plugins/servlet/ac/com.hackerone/get-started-with-hackerone-on-jira
5. User steals a hackerone generated configuration link `https://hackerone.com/apps/atlassian/claim-app?jwt=<TOKEN>` and uses it to link a Jira instance to their hackerone account
1. Now user can create issue in private project or linked H1 report with private issue project.


PoC █████████

## Impact

1. attacker can Create issue in priavet jira Project
1. attacker can Leaked priavet jira Project name.
1. When an administrator tries to link an instance of jira to the H1 account, they will not be able to because the instance has been linked to the attacking H1 account 

{F1196177}
1. Injecting comments on private issues into private jira projects.
1. Linking private jira issues with attacker H1 report

## Attachments
- H1PlugConf.png
- BasicVsAdmin.png
- NormBe.png
- DoS.png
