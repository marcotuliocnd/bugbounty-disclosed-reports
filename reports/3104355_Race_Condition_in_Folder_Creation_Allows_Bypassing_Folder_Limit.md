# Race Condition in Folder Creation Allows Bypassing Folder Limit

## Report Details
- **Report ID**: 3104355
- **URL**: https://hackerone.com/reports/3104355
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-04-22T15:17:48.612Z
- **Disclosed**: 2025-04-29T10:17:40.701Z

## Reporter
- **Username**: 0xsom3a
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: dust

## Vulnerability Information
## Summary:
The application enforces a hard limit of **10 folders** per user under a specific space (`Knowledge -> Space -> Folder`). However, due to a **Race Condition**, it is possible to bypass this limit by sending multiple folder creation requests simultaneously after deleting one folder. This leads to creating **more than 10 folders**, breaking the intended restriction.


## Steps to Reproduce

1. Navigate to the **Knowledge** section and enter a specific **Space**.
2. Create folders until you reach the maximum limit of 10.
3. Attempt to create an additional folder — you will receive an error indicating the limit has been reached.

{F4275950}

4. Delete one folder so the total becomes 9.
5. Immediately after deletion, send a large number of simultaneous folder creation requests (e.g., using Burp Suite Intruder or a custom script).
6. Observe that more than 10 folders are created — the limit is bypassed successfully.

{F4275962}

---
#POC VIDEO:

███████

---

## Impact

This vulnerability allows users to bypass the folder creation limit by sending multiple requests at the same time. As a result, they can create more folders than allowed.

This breaks the platform's rules and can lead to:

- Unfair use of resources.
- Slower performance for other users.
- Abuse of system limits that are meant to keep things stable.

If someone uses this in a large workspace, it could cause serious problems for the whole team.

## Attachments
- 22.04.2025_16.47.11_REC.png
- 22.04.2025_17.06.16_REC.png
