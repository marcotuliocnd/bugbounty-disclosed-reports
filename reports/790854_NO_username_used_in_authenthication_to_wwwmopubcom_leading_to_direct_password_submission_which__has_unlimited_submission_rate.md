# NO username used in authenthication to www.mopub.com leading to direct password submission which  has unlimited submission rate.

## Report Details
- **Report ID**: 790854
- **URL**: https://hackerone.com/reports/790854
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-07T19:51:26.608Z
- **Disclosed**: 2020-02-28T00:00:48.060Z

## Reporter
- **Username**: adarsh_p
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:**user name is  not used in authentication leading to direct password submission

**Description:** user name not used in authentication in https://www.mopub.com/login/?next=/dsp-portfolio/       (this page is labelled as SITE ADMIN: refer POC) can lead to direct submitting of password and this password has  unlimited submission rate

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. go to https://www.mopub.com/login/?next=/dsp-portfolio/
  2. we get a text box input only for password submission.
  3. this password submission has unlimited rate for submitting leading to bruteforce attacks.

POC screenshots attached.

## Impact:This page is labelled as site admin (look in poc)and thus direct entry of password only which has no rate for submission can lead to attacker getting logged in.

## Supporting Material/References:

  * screenshots of POC attached.)

## Impact

attaker can login to page which is listed as SITE ADMIN in mopub.com

## Attachments
- siteadminpoc.PNG
- Capture2.jpg.PNG
- unlimited_password_submission_POC.PNG
