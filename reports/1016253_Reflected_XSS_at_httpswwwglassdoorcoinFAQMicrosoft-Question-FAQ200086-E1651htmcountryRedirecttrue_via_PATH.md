# Reflected XSS at https://www.glassdoor.co.in/FAQ/Microsoft-Question-FAQ200086-E1651.htm?countryRedirect=true via PATH

## Report Details
- **Report ID**: 1016253
- **URL**: https://hackerone.com/reports/1016253
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-22T12:31:56.116Z
- **Disclosed**: 2021-04-16T02:56:06.992Z

## Reporter
- **Username**: n1xk_10
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glassdoor

## Vulnerability Information
**Summary:** 
The endpoint https://www.glassdoor.co.in/FAQ/Microsoft-Question-FAQ200086-E1651.htm?countryRedirect=true  is vulnerable to reflected XSS.
Injecting any input in path will be reflected back without any sanitisation.
 
Affected URL or select Asset from In-Scope: https://www.glassdoor.co.in/FAQ/Microsoft-Question-FAQ200086-E1651.htm?countryRedirect=true
Injection point: Path
Vulnerability Type: Reflected XSS
Browsers tested: Safari, Chrome, Firefox
Payload: %22%3e%3cimg%20onerro%3d%3e%3cimg%20src%3dx%20onerror%3dalert%601%60%3e

## Steps To Reproduce:

  1. Navigate to https://www.glassdoor.co.in/FAQ/Microsoft-Question-FAQ200086-E1651.htm?countryRedirect=true
  2. input the payload inside path.

  3.Open this url: https://www.glassdoor.co.in/FAQ/Mic%22%3e%3cimg%20onerro%3d%3e%3cimg%20src%3dx%20onerror%3dalert%601%60%3e
rosoft-Question-FAQ200086-E1651.htm?countryRedirect=true

  An alert will be popped up.

## Impact

Using XSS an attacker can steals the victim cookie and can also redirect him to a malicious site controlled by the attacker.

## Attachments
- Screenshot_2020-10-22_at_5.58.31_PM.png
