# Knowledge Base Articles are Globally Modifiable via ██████

## Report Details
- **Report ID**: 819911
- **URL**: https://hackerone.com/reports/819911
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-16T05:16:58.516Z
- **Disclosed**: 2021-02-18T19:03:32.558Z

## Reporter
- **Username**: un4gi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
A user is able to create an account on `██████████` and modify or create any knowledge base articles. This includes articles that have been created by the ██████████ as a canned response to help users with frequently asked questions.

**Description:**
Knowledge base articles are used within the ██████████ to assist users with common issues that they may encounter. Permissions to these articles are not properly restricted, allowing any user with an account to modify or create an article. Additionally, regular users could deface these articles or mislead other users.

## Impact
An adversary could modify a knowledge base article to lead a user into clicking a malicious link or downloading a malicious file. This could ultimately lead to a compromise of DoD Information Systems.

## Step-by-step Reproduction Instructions

1. Create an account or login to `████████` and browse to `█████████`.
████████
2. Click the `Knowledge` category and select an article to modify. I chose the first one.
███████
3. Click `edit` in the top right corner.
██████████
4. Here you see you have full control over the article.
██████
5. To test the ability to modify the article, I added `-h1-` at the bottom.
████
6. After clicking `Update`, it appears the article updated successfully.
████
7. To verify other users can see this change, I returned to the main page `█████████` and manually browsed to the knowledge base articles.
██████████
█████████
█████
███

## Suggested Mitigation/Remediation Actions
Restrict modification of knowledge base articles to ███████ employees only. Regular users should not be able to modify these articles, as it could provide misleading or even malicious information to other users.

## Impact

An adversary could modify a knowledge base article to lead a user into clicking a malicious link or downloading a malicious file. This could ultimately lead to a compromise of DoD Information Systems. Additionally, regular users could deface these articles or mislead other users.

## Attachments
No attachments
