# Stored XSS via Create Project (Add new translation project)

## Report Details
- **Report ID**: 610219
- **URL**: https://hackerone.com/reports/610219
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-06-12T14:28:32.362Z
- **Disclosed**: 2019-07-09T13:43:21.812Z

## Reporter
- **Username**: th3_alchem1st
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi, Input validation and/or sanitisation is not currently applied in the **Project Name** field in https://<domain>/create/project/. As, a result, it is possible to have a stored XSS that will affect all the users in the Weblate application. To identify this XSS I used the Docker environment from https://github.com/WeblateOrg/docker.

**Steps to reproduce:**

1. Administrator creates a project and then adds a user in that project.
2. Depending on permissions the user will login go to **watched projects** pick the project -> **Manage** -> **Settings** and will have the ability to change the Project Name. Here I changed it to `<svg/onload=alert(document.domain)>` and hit save.
3. When the user visits his `/accounts/profile/` page, he will trigger the Stored XSS.

I also found that even a user that doesn't have access to that project, but I guess the project is public, he will also get xss'ed. Furthermore, with this he also has the ability to xss the Admin, all the have to do is visit the `/accounts/profile/` page.

So, this has the potential to affect all users.

## Impact

Input validation and/or sanitisation on the Project Name field.

Please let me know if you require any additional information regarding this issue.

Thanks.

## Attachments
- xss-weblate.png
