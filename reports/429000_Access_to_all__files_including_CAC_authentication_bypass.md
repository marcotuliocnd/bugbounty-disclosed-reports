# Access to all █████████ files, including CAC authentication bypass

## Report Details
- **Report ID**: 429000
- **URL**: https://hackerone.com/reports/429000
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-10-25T22:21:22.672Z
- **Disclosed**: 2019-04-08T17:04:41.451Z

## Reporter
- **Username**: cablej_dds
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**

Due to an Insecure Direct Object Reference (IDOR) in adding recipients to a shared package on ██████████, an unauthenticated attacker can access all files uploaded to ████. As described on ██████████ website, this includes documents with classifications up to FOUO, including PII / PHI Privacy Act data, and documents classified `FOUO//CLOSE HOLD`, `FOUO//SENSITIVE`, and `FOUO//LIMITED DISTRIBUTION DOCUMENT`.

Additionally, █████ enforces CAC pickup requirements to require users to first authorize via CAC. This too, can be bypassed, allowing an attacker to download any file sent over ████.

Note that in addition to this vulnerability, other IDORs exist in sensitive areas, such as confirming email addresses, allowing an attacker to pretend to send documents from any email address.

## Impact

Based on analysis of file ids, over 2000 documents are uploaded per hour to ███. When combined with a ██████, this exposes over 500,000 recent documents and new documents that are sent every hour. Additionally, as metadata for historical documents is not purged, this also includes details such as sender names/emails, file descriptions, and share dates for over 15 million past documents.

## Step-by-step Reproduction Instructions

1. Visit████/Default.aspx and proceed to send a file to yourself.
2. Click through the verification email and verify the file.
3. Log in to the Package Status page at███/StatusLogIn.aspx?PackageID=x using the provided password.
4. Intercept the request to add a new recipient via the recipients list, entering your email address as the email to add. This is a `POST` request to `POST /████████/Status.aspx?ID=x`.
5. Modify the `ID` parameter to any other number, e.g. decrement the number by 1.
6. Observe that the package will be sent to your email, which can then be downloaded using the provided password.
7. Repeat with any numeric ID to download hundreds of thousands of files.

To bypass CAC authentication:

A user can elect to require CAC authentication when downloading a file. This can be bypassed via the normal file download flow.

1. Visit█████/███?id=15745307 (the initial file ID here does not matter).
2. Enter the password emailed for the file that requires CAC authentication.
3. Intercept the request to submit the form. Replace the `id` parameter in the url with the id of the file with CAC authentication.
4. Observe that the file's information will be displayed and can be downloaded.

## Suggested Mitigation/Remediation Actions
- Ensure that a user can only modify their own packages
- Ensure that a file cannot be downloaded without CAC authentication
- Ensure that a user can only verify their own packages.

## Impact

.

## Attachments
No attachments
