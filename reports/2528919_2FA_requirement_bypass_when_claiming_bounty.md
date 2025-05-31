# 2FA requirement bypass when claiming bounty 

## Report Details
- **Report ID**: 2528919
- **URL**: https://hackerone.com/reports/2528919
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2024-05-31T12:38:36.011Z
- **Disclosed**: 2024-07-11T14:45:40.762Z

## Reporter
- **Username**: raymatp
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
When claiming bounty, hackerone doesnt check if the user have enabled 2FA even if the program requires that user enabled 2FA

**Description:**
Programs can enable 2FA requirement for users to force users to enable 2FA before they can submit report to the program. At some instance like submitting via embedded submission, hackerone would enforce the 2FA requirement before user can claim the report. However, the requirement isnt enforced if the user is claiming bounty thus bypassing the 2fa requirement


### Steps To Reproduce

1. Using your sandbox program, enable 2fa requirement in https://hackerone.com/{program_handle}/submission_requirements
2. create an API token with reward privilege
3. reward your dummy account with no 2fa enabled
4. using your dummy account, claim the bounty. Notice that you can claim the bounty even without enabling 2fa


### Optional: Supporting Material/References (Screenshots)

{F3315849}{F3315851}{F3315852}

## Impact

bypassing 2fa requirement by the program

## Attachments
- image.png
- image.png
- image.png
