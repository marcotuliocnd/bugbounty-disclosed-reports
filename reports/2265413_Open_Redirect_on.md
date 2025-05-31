# Open Redirect on ███████

## Report Details
- **Report ID**: 2265413
- **URL**: https://hackerone.com/reports/2265413
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-11-27T19:28:25.262Z
- **Disclosed**: 2025-05-02T19:10:10.011Z

## Reporter
- **Username**: hasn0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: fastly-vdp

## Vulnerability Information
Vulnerability Details:

User can be Redirect to malicious site POC:  █████████

Steps To Reproduce:
Use a browser to navigate to ███

  1.Navigate to the vulnerable page on the website/application
  2.Modify the “redirect_url” parameter by adding a malicious URL as its value.
  3.Submit the request and observe that the page is redirected to the malicious URL.


  screenrecord

## Impact

Open redirect vulnerabilities can have various impacts on both users and organizations. Here are some potential consequences:

Phishing Attacks: Attackers can exploit open redirect vulnerabilities to craft convincing phishing attacks. They can redirect users to malicious websites that mimic legitimate ones, tricking them into divulging sensitive information such as usernames, passwords, or credit card details.

Malware Infections: Redirecting users to malicious websites through open redirect vulnerabilities can lead to the inadvertent download and installation of malware. This can result in the compromise of user devices, theft of personal information, or unauthorized access to sensitive data.

## Attachments
No attachments
