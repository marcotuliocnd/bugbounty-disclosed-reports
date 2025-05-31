# No Rate Limit (Leads to huge email flooding/email bombing)

## Report Details
- **Report ID**: 272596
- **URL**: https://hackerone.com/reports/272596
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-28T05:15:24.226Z
- **Disclosed**: 2017-09-28T17:47:57.625Z

## Reporter
- **Username**: saikiran-10099
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: aspen

## Vulnerability Information
Dear sir,
At first,i want to say that this sensitive action definitely should be set with rate limit.
Note:-This is about huge bombing/brute force on any endpoints.

Vulnerability:-
->No rate limit has been set for generating account confirmation emails for accounts on above selected domain which is being served by using readthedocs.org
->As there is no rate limit set,an attacker can successfully perform brute force/huge email bombing/cookie bombing/email spoofing on the victim's account.

Impact:-
->This vulnerability makes the attackers to move on to next step of the attack what they want to do,this may be a best practice for attackers to exploit any other vulnerabilities.
->If attacker decides to trouble users by generating many emails/by email bombarding,how can a user can safely browse for the next time.
->users will get affected due to this attack and privilege escalation is possible for an attacker.
->access to user's account by brute force.
->Trouble to the users on the website because huge email bombing can be done by the attackers within seconds.

Steps to reproduce:-
1.Enter any user mail id by going to django.aspen.io and then sign up on readthedocs.org
2.generate account confirmation email
3.capture the POST request using proxy(i used burp)
4.send the POST request to burp intruder
5.set the pay load to high value
6.click on start attack
7.after finishing the attack,go to user mail account and check the inbox
8.The inbox will be completely bombarded with account confirmation emails(See Proof of concept-images)

proof of Concept:-
->I used a high payload value to attack on my own account.

Note:-this is not automated report.I manually discovered and configured on my own.

HTTP request:-
POST /accounts/email/ HTTP/1.1
Host: readthedocs.org
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 97
Referer: https://readthedocs.org/accounts/email/
Cookie: X-Mapping-fjhppofk=EC2A1AAE6893114C1E225F343087E94A; csrftoken=lTNq0kHts5gtFX8Y4AAEEPQJHsspaKyh; __utma=263995919.1657399472.1506574210.1506574210.1506574210.1; __utmb=263995919.8.10.1506574210; __utmc=263995919; __utmz=263995919.1506574210.1.1.utmcsr=django.aspen.io|utmccn=(referral)|utmcmd=referral|utmcct=/en/latest/; __utmt=1; sessionid=ul1gyenoaadrufuzhpm0yheblod87jx1
Connection: close
Upgrade-Insecure-Requests: 1

csrfmiddlewaretoken=lTNq0kHts5gtFX8Y4AAEEPQJHsspaKyh&email=saikiran10099%40gmail.com&action_send=

Reference Links:-
https://blog.twitter.com/official/en_us/a/2008/what-does-rate-limit-exceeded-mean-updated.html
https://code.tutsplus.com/tutorials/how-to-build-rate-limiting-into-your-web-app-login--cms-22133
https://hackerone.com/reports/159497
https://hackerone.com/reports/115844

Vulnerability Tested using:-
Browser:-Mozilla Firefox
Version:-54.0.1
Os:-Windows10

## Attachments
No attachments
