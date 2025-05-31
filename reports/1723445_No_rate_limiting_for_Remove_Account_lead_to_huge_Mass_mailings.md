# No rate limiting for Remove Account lead to huge Mass mailings

## Report Details
- **Report ID**: 1723445
- **URL**: https://hackerone.com/reports/1723445
- **State**: Closed
- **Severity**: none
- **Submitted**: 2022-10-05T12:42:01.781Z
- **Disclosed**: 2022-11-20T09:08:27.996Z

## Reporter
- **Username**: tanvir_0x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Name of the vulnerability:- No rate limiting for Remove Account lead to huge Mass mailings

Hlw Team

I am a security researcher and I found this vulnerability in your website  Business Logic Errors
https://hosted.weblate.org

***Description :

No Rate Limit is a type of computer security vulnerability typically found in web applications. No Rate Limit  enables attackers to perform actions on the web application where the attacker can do signup creation, password reset or 2FA of other users. No Rate Limit vulnerability may be used by attackers to bypass access controls such & bruteforce tokens and passwords without any limiting of any requests. There should be protection on the web application for sensitive actions. Attackers send a high number of requests to perform desirable actions to get access to the application or accounts.
NO RL effects vary in range from petty nuisance to significant security risk, depending on the sensitivity of the data handled by the vulnerable site and the nature of any security mitigation implemented by the site's owner network.

***Steps to Reproduce:

Step 1-Go To This Link https://hosted.weblate.org/accounts/remove/

Step 2- Intercept This Request In Burp And Forward Till You Found Your Number In
 
Step 3- Now Send This Request To Intruder And Repeat It 250 Time By Fixing Any Arbitrary Payload Which Doesn't No Effect Request I Choose Accept-Language: en-US,en;q=0.$5$ and payload set null 250 and start attack

***[attachment / reference] Video POC Attached below.

***Remediation:

I Will Recommend You To Add A ReCaptcha & Sort Of Something Which Requires Manual Human Interaction To Proceed Like You Can Add Captcha Like 2+2=___ so that it cannot be brute forced and you also can have a limit at the backend for particular number upto 5 times a day user can request Forget Password Email or Link something like that will prevent you from someone exploiting this vulnerability

Regards

Tanvir Imon

## Impact

***Impact:

An Adversary can carry out No Rate-Limit attack and also can take over the victim Account.
Also, an adversary can manage to login through any other user's account.

***Business Impact:

Using rate limiting for website protection has significant drawbacks when it comes to your business. rate limiting is costing you money, and what you can do about it

## Attachments
No attachments
