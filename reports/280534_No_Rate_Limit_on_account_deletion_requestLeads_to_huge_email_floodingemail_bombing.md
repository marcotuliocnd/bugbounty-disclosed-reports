# No Rate Limit on account deletion request(Leads to huge email flooding/email bombing)

## Report Details
- **Report ID**: 280534
- **URL**: https://hackerone.com/reports/280534
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-10-19T14:57:36.400Z
- **Disclosed**: 2017-12-12T19:48:51.842Z

## Reporter
- **Username**: saikiran-10099
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
Dear sir,
At first,i want to say that this sensitive action definitely should be set with rate limit.
Note:-This is about huge bombing/brute force on any endpoints.

Vulnerability:-
->No rate limit has been set for generating account deletion emails for accounts on above selected domain.
->As there is no rate limit set,an attacker can successfully perform brute force/huge email bombing/cookie bombing/email spoofing on the victim's account.

Impact:-
->This vulnerability makes the attackers to move on to next step of the attack what they want to do,this may be a best practice for attackers to exploit any other vulnerabilities.
->If attacker decides to trouble users by generating many emails/by email bombarding,how can a user can safely browse for the next time.
->users will get affected due to this attack and privilege escalation is possible for an attacker.
->access to user's account by brute force.
->Trouble to the users on the website because huge email bombing can be done by the attackers within seconds.

Steps to reproduce:-
1.Enter any user mail id by going to https://infogram.com/
2.generate account deletion email
3.capture the POST request using proxy(i used burp)
4.send the POST request to burp intruder
5.set the pay load to high value
6.click on start attack
7.after finishing the attack,go to user mail account and check the inbox
8.The inbox will be completely bombarded with forgot password emails(See Proof of concept-images)

proof of Concept:-
->I used a high payload value to attack on my own account.

Note:-this is not automated report.I manually discovered and configured on my own.

HTTP Request:-
POST /api/requests/account_delete HTTP/1.1
Host: infogram.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 42
Cookie: ab=a11; _ga=GA1.2.229897234.1508421432; _paths=https%3A%2F%2Finfogram.com%2F%2Chttps%3A%2F%2Fe.infogram.com%2F_%2FLbgSk2kucbdLGe9a9t09%2Chttps%3A%2F%2Finfogram.com%2Flogin%2Chttps%3A%2F%2Finfogram.com%2Fforgot%2Chttps%3A%2F%2Finfogram.com%2Flogin%2Chttps%3A%2F%2Finfogram.com%2Fforgot%2Chttps%3A%2F%2Finfogram.com%2Flogin%2Chttps%3A%2F%2Finfogram.com%2Freset_password%2Chttps%3A%2F%2Finfogram.com%2Flogin%2Chttps%3A%2F%2Finfogram.com%2Freset_password%2Chttps%3A%2F%2Finfogram.com%2Fforgot%2Chttps%3A%2F%2Finfogram.com%2Freset_password%2Chttps%3A%2F%2Finfogram.com%2Flogin%2Chttps%3A%2F%2Finfogram.com%2Freset_password%2Chttps%3A%2F%2Finfogram.com%2Flogin%2Chttps%3A%2F%2Finfogram.com%2Freset_password%2Chttps%3A%2F%2Finfogram.com%2Flogin%2Chttps%3A%2F%2Finfogram.com%2F%2Chttps%3A%2F%2Finfogram.com%2Flogin; cookieConsent=true; __zlcmid=j4gpexLaxANDLh; dc=as; ig_session=s%3AGKmNSO_sSUJZtZaV9g5bxp_Ssl8DPTH7.5wPx%2FctolgQgRddaxwWWbIHQNeMoSen%2BIdjghPEpBPM; _gid=GA1.2.184347568.1508421537; _duckbase_guid=de562f7f711cc3ab4efd0de1; _hjIncludedInSample=1; _gat=1; _gat_Web=1; rememberme=S3u2eA9SX1tSw3ntkfwktGZGN0Ej0U26; loggedin=1; _gat_App=1
Connection: close

_csrf=ChZ8Uvl8-yz07Pxjz87VrMV4wMbMTi8JmELI

HTTP Response:-
HTTP/1.1 200 OK
Date: Thu, 19 Oct 2017 14:51:05 GMT
Content-Type: application/json; charset=utf-8
Connection: close
Server: nginx
Vary: Accept-Encoding
X-DNS-Prefetch-Control: off
Strict-Transport-Security: max-age=10886400
X-Download-Options: noopen
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Referrer-Policy: no-referrer
X-Frame-Options: SAMEORIGIN
ETag: W/"77-4sii1M9+uiHgSTjXmq/QmR+My5c"
X-Infogram-Server: b302
X-Infogram-Proxy: as
Content-Length: 119

{"status":"ok","msg":"We sent you an e-mail with the account deletion link.<br/>The link will be active for 24 hours."}

Note:-
Ofcourse, generating account deletion emails is possible if an attacker gets control over user's account (or) it may be possible if any other vulnerabilities are discovered in future.

Thank you

## Attachments
No attachments
