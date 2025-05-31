# PII Leak via https://████████

## Report Details
- **Report ID**: 808338
- **URL**: https://hackerone.com/reports/808338
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-03-02T06:06:48.435Z
- **Disclosed**: 2020-05-11T16:34:35.787Z

## Reporter
- **Username**: un4gi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
An attacker can create an account on https://████ and gain access to a wealth of PII for practically every member that is registered on the website. This includes e-mail addresses, physical addresses, telephone numbers, and other information about a vast majority of the US Air Force, as this portal is where ████████ support is hosted.

**Description:**

## Impact
An adversary can sign up for an account on https://█████████ to gather a vast amount of PII related to a large portion of the USAF. This can be used for many purposes and should not be accessible by a regular user.

## Step-by-step Reproduction Instructions

1. Browse to https://██████████
███████
2. Create an account or sign in and visit your profile page in the top right corner.
████
3. Click on `Department` and select `AU Registrar` from the drop-down menu. Once selected, click the `i` icon to the left of the `AU Registrar` field.
█████████
4. In the next screen, click the `Users` field in the `Related Lists` section.
█████████
5. All users in the `AU Registrar` department will be shown. Clicking a user will display PII and other account information. I have redacted any PII from the screenshot.
█████████
6. To access data from ALL users, simply click the `All` field above the user table. You can search for specific users as well, as shown in the below screenshot were I searched for `Bob`. Once again, I redacted any PII from this screenshot.
███

## Suggested Mitigation/Remediation Actions
Limit this function to administrators only, as regular users should not be able to access this type of data (especially when any user can sign up from the open internet, regardless of ██████████ enrollment).

## Impact

An adversary can sign up for an account on https://███████ to gather a vast amount of PII related to a large portion of the USAF. This can be used for many purposes and should not be accessible by a regular user.

## Attachments
No attachments
