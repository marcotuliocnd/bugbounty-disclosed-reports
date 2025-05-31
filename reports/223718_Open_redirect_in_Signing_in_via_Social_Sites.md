# Open redirect in Signing in via Social Sites

## Report Details
- **Report ID**: 223718
- **URL**: https://hackerone.com/reports/223718
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-25T10:32:16.876Z
- **Disclosed**: 2017-05-17T14:09:01.333Z

## Reporter
- **Username**: rajauzairabdullah
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Weak **Authentication** Leads to the **Open redirection** to **_Malicios Sites_** :

### Signing in via Facebook :
+ https://hosted.weblate.org/accounts/login/facebook/?next=///evil.com

### Signing in via Gmail :
+ https://hosted.weblate.org/accounts/login/google-oauth2/?next=///evil.com

### Signing in via Github:

+ https://hosted.weblate.org/accounts/login/github/?next=///evil.com

### Signing in via Bitbucket:

+ https://hosted.weblate.org/accounts/login/bitbucket/?next=///evil.com

### Signing in via Gitlab:

+ https://hosted.weblate.org/accounts/login/gitlab/?next=///evil.com

### Vulnarable Parameter: 

**" next  "**

Greets
**Raja Uzair Abdullah**

## Attachments
No attachments
