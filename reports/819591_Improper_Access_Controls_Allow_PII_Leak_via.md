# Improper Access Controls Allow PII Leak via ████

## Report Details
- **Report ID**: 819591
- **URL**: https://hackerone.com/reports/819591
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-03-15T10:52:24.953Z
- **Disclosed**: 2021-02-18T19:01:07.337Z

## Reporter
- **Username**: un4gi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
Dashboards in `██████████` allow a user to add widgets and obtain large amounts of information to include PII and diagnostic information. Additionally, a user is able to make changes to certain catalogs via these widgets.

**Description:**

## Impact
An adversary can gain access to PII to include full names, e-mail addresses, physical addresses, phone numbers, etc., as well as modifying fields within the underlying system. Additionally, the adversary could identify information such as the number/type of incidents, as well as diagnostic information such as memory usage.

## Step-by-step Reproduction Instructions

1. Create an account on `███████/` and browse to `███████` once your account has been verified. 
██████
2. If this is your first time accessing this page, you will need to create a dashboard.
██████
3. Using the `Add Widgets` feature, an adversary can gain access to various information as shown in the picture below. This is just a small glimpse of what an adversary has access to through this panel.
████
4. Clicking on the `All(22)` text in the third widget above, an adversary can access various configuration items.
██████████
5. These can then be modified by the adversary as shown below:
████
6. If an adversary browses to `███/home`, they get a slightly different interface:
████
7. By clicking `Add Content` in the top left corner, the adversary can add widgets similar to before. This dashboard seems to contain a little more functionality..
████████
8. By adding `███████`, the adversary can access PII of many of the users of the website.
█████
█████
9. The `███` account shown below does not contain much sensitive information, but the fields for the other accounts are highly populated. The ████████ account was used instead in effort to prevent showing real user information.
████████

## Suggested Mitigation/Remediation Actions
Restrict access to these widgets to only those users that need this functionality. Regular users should not have access to this data, especially when the account creation process is so easy.

## Impact

An adversary can gain access to PII to include full names, e-mail addresses, physical addresses, phone numbers, etc., as well as modifying fields within the underlying system. Additionally, the adversary could identify information such as the number/type of incidents, as well as diagnostic information such as memory usage.

## Attachments
No attachments
