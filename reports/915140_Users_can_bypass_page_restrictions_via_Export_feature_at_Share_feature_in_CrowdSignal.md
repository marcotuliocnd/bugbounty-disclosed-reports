# Users can bypass page restrictions via Export feature at "Share" feature in CrowdSignal

## Report Details
- **Report ID**: 915140
- **URL**: https://hackerone.com/reports/915140
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-04T04:51:16.155Z
- **Disclosed**: 2020-11-18T14:22:38.190Z

## Reporter
- **Username**: bugra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Hi team,
If you upgraded your account, you can share your survey results via "Share" button.
{F893428}

As you can see, I selected `Results` page on `Allow access to the following`. So user will access only `Results` page. But if user has the `Export` feature.
User can export the restricted pages with these URLs :
- Overview page : https://app.crowdsignal.com/share/(surveytoken).xlsx
- Locations page : https://app.crowdsignal.com/share/(surveytoken)/locations.xlsx
- Participants page : https://app.crowdsignal.com/share/(surveytoken)/participants.xlsx

Replace the survey token with your's.

## Steps To Reproduce:

  1. Go to your survey's `Results` page with upgraded account
  1. Click `Share`
  1. Write the user's email
  1. Select `Results` page only on `Allow access to the following` and give access to Export.
  1. Click `Save` and  wait the `Shared survey` mail
  1. Click to survey link on mail
  1. Now try to export restricted pages via visiting the above URLs

## Impact

Users can export restricted pages on survey sharing feature

Thanks,
Bugra

## Attachments
- share.PNG
