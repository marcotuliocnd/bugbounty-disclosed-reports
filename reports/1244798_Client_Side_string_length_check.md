# Client Side string length check

## Report Details
- **Report ID**: 1244798
- **URL**: https://hackerone.com/reports/1244798
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-26T02:47:50.938Z
- **Disclosed**: 2023-10-14T00:36:00.126Z

## Reporter
- **Username**: tomh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
Hi,
in the "Class Settings" page on khanacademy.org  you can rename the class, but the string length check is not done on the server side. 
Throughout the experimentation I used an account with associated email "██████████" and where applicable, class ID ████.
An attacker can save thousands of characters instead of the expected 50 (while I was testing I was able to set a string of over 108 thousand characters!).
The fix may be limited to the server-side string length check, however I recommend checking the string length on all other pages as well.

Request URL: https://it.khanacademy.org/api/internal/graphql/renameStudentListMutation
Parameter (POST): "name"

## Impact

An attacker could exploit this lack of control to save content, break the page template (for /profile/attackerusername too), crash the page for low-memory visitors, and possibly cause unexpected behavior.

## Attachments
No attachments
