# 2FA bypass by sending blank code

## Report Details
- **Report ID**: 897385
- **URL**: https://hackerone.com/reports/897385
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-06-13T08:41:22.866Z
- **Disclosed**: 2020-07-02T13:40:30.885Z

## Reporter
- **Username**: safehacker_2715
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glassdoor

## Vulnerability Information
**Summary:** █████████. This is a failure in null check of the entered code. In simple terms, the 2FA while logging in can be bypassed by sending a blank code. This could be because of incorrect comparison of entered code with true code. A pre-validation (may be null check) before comparing the codes would fix the issue

Affected URL or select Asset from In-Scope: Glassdoor 2FA
Affected Parameter: code
Vulnerability Type: Improper Authentication
Browsers tested: Browser independent

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1.  Login to Glassdoor and navigate to https://www.glassdoor.com/member/account/securitySettings_input.htm
  2. Enable 2FA
  3. Logout
  4. Login again and notice OTP is asked
  5. Now using Burp suite intercept the POST request by sending incorrect code. [Do not forward]
  6. Before forwarding the request to server, remove the code and forward
  7. Turnoff Intercept and notice that your login request has been fulfilled


## Supporting Material/References (screenshots, logs, videos):
* ███████

## Impact

2FA Protection bypass. Attacker could gain access despite the 2FA protection by victim

## Attachments
No attachments
