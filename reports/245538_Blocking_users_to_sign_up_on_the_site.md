# Blocking users to sign up on the site

## Report Details
- **Report ID**: 245538
- **URL**: https://hackerone.com/reports/245538
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-07-03T13:40:13.369Z
- **Disclosed**: 2017-07-08T18:38:50.450Z

## Reporter
- **Username**: saikiran-10097
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Dear sir,
            This may be a low priority issue,but has the importance to resolve at your priority.I request you to think over this report,because this vulnerability is not a spam on many other sites.

URL:-
https://wakatime.com/signup
https://wakatime.com/login

Vulnerability:-
->Attacker can block users to create their own accounts on your site.
->Attacker can create multiple fake accounts by using users email addresses ,so that he can become advantageous to perform any violated actions without being identified.

Steps to reproduce(Attack Scenario) and imapct:-
->Let "A" be the attacker.
->He will know the original mail id of the victim.(we know that,mail id's are public in all sites).
->He will sign up using victim mail id and now confirmation email will be send to user mail.
->Now,immediately the attacker will update the created account with an invalid mail address (or) with his own mail address.
->After updating the mail address,whether the attacker confirms it or not,the following actions are being taken place.
                 (a)The user mail id is being blocked to create an account,that means whenever the original user wants to sign up on the site with his mail id,he can't because it shows that email has already been registered.
                 (b)As email confirmation is not being asked immediately and it is also not set to mandatory,after updating with an invalid mail address,this turns into a fake account.so that,this gives an attacker an advantage to perform any other attacks and also he can know the website functionality.(Remediation:-some sites will create an account after email is being confirmed as like hackerone)
                 (c)This trouble is caused for users:-
                     whenever a user creates an account with his personal mail address,and now he wants the same account to be updated with his office mail address,he can do it.
                     But,if user again wants to create an another account using his personal mail address,his mail address will not be accepted to sign up.(as a result,users will also suffer regarding this issue).
                  (d)whenever a user mail id is updated by the attacker,the "your email has changed" mail should be sent to the user,because who knows may be attacker has taken control over victim's account.Here,the email has not being sent to user(alternately,it is being sent to attacker mail),as a result whenever attacker has taken control over user's account,user can't recover his account immediately.

Vulnerability Tested in:-
Browser:-Google Chrome
Version:-59.0.3071.115
Os:-Windows10


## Attachments
No attachments
