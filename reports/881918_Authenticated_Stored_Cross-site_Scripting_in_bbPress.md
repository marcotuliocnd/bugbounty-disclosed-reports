# Authenticated Stored Cross-site Scripting in bbPress

## Report Details
- **Report ID**: 881918
- **URL**: https://hackerone.com/reports/881918
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-24T19:39:24.327Z
- **Disclosed**: 2020-06-29T10:08:42.091Z

## Reporter
- **Username**: whoisbinit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
## Description:
There exists a stored XSS vulnerability in bbPress, due to which the XSS payload which I enter in my content, gets executed at **/wp-admin/edit.php?post_type=forum**. This vulnerability requires you to be an authenticated user.

## Steps To Reproduce:
Step 1. Visit /wp-admin/edit.php?post_type=forum
Step 2. Click on **Add New**
Step 3. Write any title, and in content, write your XSS payload through the "Text" editor, rather than the "Visual" one, and publish the content.
Step 4. Now, visit /wp-admin/edit.php?post_type=forum, and you will be able to see the payload getting executed.

## Recommendations
Making use of proper functions in PHP or WordPress core in the bbPress source code regarding the filtering or sanitization of user input is a recommended way to fix this vulnerability.

## Impact

By taking an advantage of this vulnerability, an owner of a WordPress-based website would be able to execute their malicious JavaScript codes in context to the WordPress dashboard, which could result in bad issues to other users.

## Attachments
- bbPress.png
