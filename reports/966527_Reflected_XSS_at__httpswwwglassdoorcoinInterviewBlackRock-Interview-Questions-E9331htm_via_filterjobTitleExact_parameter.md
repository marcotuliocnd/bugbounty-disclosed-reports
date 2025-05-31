# Reflected XSS at  https://www.glassdoor.co.in/Interview/BlackRock-Interview-Questions-E9331.htm via filter.jobTitleExact parameter

## Report Details
- **Report ID**: 966527
- **URL**: https://hackerone.com/reports/966527
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-25T08:52:53.797Z
- **Disclosed**: 2021-04-16T02:54:54.015Z

## Reporter
- **Username**: n1xk_10
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glassdoor

## Vulnerability Information
Summary: There is a reflected XSS vulnerability in https://www.glassdoor.co.in/Interview/BlackRock-Interview-Questions-E9331.htm?filter.jobTitleExact=Portfolio+Management+Group-Fixed+Income+Analyst&countryRedirect=true

Affected Parameter: filter.jobTitleExact
Browsers tested: Chrome, Firefox
Payload : %3c%3cs%3escript%3ealert%601%60%3c%3cs%3e/script%3e

Steps To Reproduce:

  1.  Navigate to https://www.glassdoor.co.in/Interview/BlackRock-Interview-Questions-E9331.htm?filter.jobTitleExact=Portfolio+Management+Group-Fixed+Income+Analyst&countryRedirect=true 
  2.  Enter this payload : %3c%3cs%3escript%3ealert%601%60%3c%3cs%3e/script%3e in the input parameter filter.jobTitleExact
  3.  Then see the response in browser, an pop up will appear.

## Impact

Using XSS an attacker can steals the victim cookie and can also redirect him to a malicious site controlled by the attacker.

## Attachments
- Screenshot_at_2020-08-25_14-22-01.png
