# Stored XSS on Issue details page

## Report Details
- **Report ID**: 384255
- **URL**: https://hackerone.com/reports/384255
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-07-19T17:49:43.530Z
- **Disclosed**: 2018-10-30T06:12:08.889Z

## Reporter
- **Username**: 8ayac
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
**Summary:**
The detail page of Issue (the page that provides the content of an Issue) is vulnerable to Stored XSS.

**Description:**
The two exploits are via the function of submittin an issue or the function of editing an issue.
This vulnerability is reproduced in `Firefox` and`Chrome`. `IE11` and`Edge` are not. I did not test the reproduction on other browsers.

## Steps To Reproduce:
1. Sign in to GitLab.
2. Click the "[+]" icon.
3. Click "New Project".
4. Fill out "Project name" form with "PoC".
5. Check the check box of "Public".
6. Click "Issues"
7. Click "New issue" button.
8. Fill out the each form as follows:
    * Title: PoC
    * Description: `![xss" onload=alert(1);//](a)`
9. Click "Submit issue".

Furthermore, when editing an already existing issue, you can also reproduce by entering A in the "Description" form and saving it.

## Impact

The security impact is the same as any typical Stored XSS.

Thank you!

## Attachments
- poc.PNG
