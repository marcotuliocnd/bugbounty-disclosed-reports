# [REMOTE] Full Account Takeover At https://██████████████/CAS/

## Report Details
- **Report ID**: 215859
- **URL**: https://hackerone.com/reports/215859
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-03-24T14:49:40.993Z
- **Disclosed**: 2019-10-04T15:23:30.728Z

## Reporter
- **Username**: karimrahal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
A session cookie **PROD_CAS_SESSION** takes a User ID as an input, hence an attacker is able to insert his victim's User ID and takeover his victim's account. (P.S The User ID is only 6 numbers long). 
## Impact
An attacker is able to insert his victim's User ID into the cookie **PROD_CAS_SESSION** and takeover his victim's account.
## Step-by-step Reproduction Instructions

1. Go to https://██████/MOS/ (This is one of many websites you can do this from)
2. Add a cookie with the domain **███**, the name **PROD_CAS_SESSION*, and the value should be ur victim's User ID (example: **195141**).
3. Refresh the page
4. Done, you will be logged into your victim's account.

**To Get User's Info**
4. At https://████/MOS/, you will notice a dropdown on the right top corner with **Welcome (Your Victim's Name)**, click the dropdown and click **My Profile**
5. Done, you will be able to see your victim's user info.

## Suggested Mitigation/Remediation Actions
Add a more secure session value.

## Attachments
No attachments
