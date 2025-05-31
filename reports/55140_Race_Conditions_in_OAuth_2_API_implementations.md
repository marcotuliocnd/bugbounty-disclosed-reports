# Race Conditions in OAuth 2 API implementations

## Report Details
- **Report ID**: 55140
- **URL**: https://hackerone.com/reports/55140
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2015-04-06T23:56:06.373Z
- **Disclosed**: 2017-09-19T17:40:28.080Z

## Reporter
- **Username**: dor1s
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Most of OAuth 2 API implementations seem to have multiple Race Condition vulnerabilities for processing requests for Access Token or Refresh Token.

Race Condition allows a malicious application to obtain several `access_token` and `refresh_token` pairs while only one pair should be generated. Further, it leads to authorization bypass when access would be revoked.

I've already tested for this vulnerability 11 different targets (web-services providing OAuth2 API), and 6 of them are vulnerable. Only one target seems to be certainly protected (or I just failed to catch into Race Condition time window). The rest 4 targets have Race Condition bug, but protected against further exploitation by one of the following reasons:
* only one of several tokens generated is valid (**1 target**)
* for any access revocation all tokens always are revoked (**1 target**)
* for all concurring requests finished successfully the same `access_token` values (or in pair with `refresh_token`) obtained (**2 targets**)

At this moment I cannot list vulnerable targets here because of responsible disclosure, but I think it would be possible to publish their names soon.

Initially, I thought the vulnerability is located in [Doorkeeper gem for Ruby](https://github.com/doorkeeper-gem/doorkeeper). It is very popular, and I know that some of the vulnerable targets use this gem. To be clear, I tested [OAuth 2 provider example based on it](https://github.com/doorkeeper-gem/doorkeeper-provider-app) and it was safe for me. *Honestly, I'm not ruby developer, so it is not easy for me to quickly inspect doorkeeper's code and distinguish is it vulnerable or not*.

However, I'm sure that 6 of vulnerable targets use different implementations (at least more than one). So the attack vector seems to be universal and possible by design.

Race Condition for Access Token
===============================
According to [OAuth 2.0 RFC](https://tools.ietf.org/html/rfc6749), `code` obtained via callback may be used only once to generate `access_token` (and corresponding `refresh_token`).

Race Condition vulnerability allows a malicious application to generate several `access_token` and `refresh_token` pairs. This leads to authentication issue when a user will revoke access for an application. One `access_token` and `refresh_token` pair would be revoked, but all the rest stay active.

Proof-Of-Concept
------------------------
 *PoC description is unified and may be used for any provider*

0) Register an application for using OAuth 2.0 API of the target provider. Obtain credentials for the application

1) Open link for the application authorization in browser. Usually it looks like:
```
https://OAUTH_PROVIDER_DOMAIN/oauth/authorize?client_id=APPLICATION_ID&redirect_uri=https://APPLICATION_REDIRECT_URI&response_type=code
```

2) Log into *a victim's* account (if it needed) and allow access for the application

3) Obtain `code` value from callback:
```
https://APPLICATION_REDIRECT_URI?code=AUTHORIZATION_CODE_VALUE
```

4) Try to exploit Race Condition for Access Token request. I used the following script for that:
```
#!/bin/bash
curl --data "grant_type=authorization_code&code=AUTHORIZATION_CODE_VALUE&client_id=APPLICATION_ID&client_secret=APPLICATION_SECRET&redirect_uri=APPLICATION_REDIRECT_URI" "https://OAUTH_PROVIDER_DOMAIN/oauth/token" &
< ... previous line repeated 20 times ... >
```

For different attempts result of its execution gives from 1 to 20 different `access_token` values (may be in pair with `refresh_token` values) for targets which has Race Condition bug (10 of 11 tested).

5) Check each `access_token`. Take the simplest request from the target API and try it for each value, like:
```
GET /api/me?access_token=ACCESS_TOKEN_VALUE HTTP/1.1
Host: OAUTH_PROVIDER_DOMAIN

```

Usually all `access_token` values are valid and working.

6) Please note that Race Condition is probabilistic vulnerability. It may be needed to do few attempts with PoC to reproduce it. Attackers usually can generate some additional load to the server (not DoS, but many requests to vulnerable script) to increase the chance of successful exploitation.

7) Here execution flow has two possible directions:
7A) Go to **settings** or **applications** page in the victim's account and revoke access for the application. Then repeat step 5 and see if all `access_token`s become invalid or not. If all `access_token`s are invalid, It is good behavior despite successful Race Condition exploitation. Actually, in some cases only one `access_token` is revoked, while all the rest stay valid.

7B) Use revocation request (like `/oauth/revoke`) for one of the `access_token`s. Then repeat step 5 and see that in this case only one token is revoked, while all the rest stay active (except one of the targets tested).


Race Condition for Refresh Token
--------------------------------
While `code` may be used only once to obtain `access_token`, `refresh_token` often may be used only once too. In such case, Race Condition vulnerability allows an attacker to generate huge number of `access_token` and `refresh_token` pairs. This will make it very hard for a victim to revoke access for the malicious application.

0) Register an application for using OAuth 2.0 API of the target provider. Obtain credentials for the application

1) Open link for the application authorization in browser. Usually it looks like:
```
https://OAUTH_PROVIDER_DOMAIN/oauth/authorize?client_id=APPLICATION_ID&redirect_uri=https://APPLICATION_REDIRECT_URI&response_type=code
```

2) Log into *a victim's* account (if it needed) and allow access for the application

3) Obtain `code` value from callback:
```
https://APPLICATION_REDIRECT_URI?code=AUTHORIZATION_CODE_VALUE
```

4) Legally obtain `access_token` and `refresh_token`. Usually it may be done by request like:
```
curl --data "grant_type=authorization_code&code=AUTHORIZATION_CODE_VALUE&client_id=APPLICATION_ID&client_secret=APPLICATION_SECRET&redirect_uri=APPLICATION_REDIRECT_URI" "https://OAUTH_PROVIDER_DOMAIN/oauth/token"
```

5) Try to exploit Race Condition for `refresh_token`. I used the following script for that:
```
#!/bin/bash
curl --data "grant_type=refresh_token&refresh_token=REFRESH_TOKEN_VALUE&client_id=APPLICATION_ID&client_secret=APPLICATION_SECRET" "https://OAUTH_PROVIDER_DOMAIN/oauth/token" &
< ... previous line repeated 20 times ... >

```

For different attempts result of its execution gives from 1 to 20 different `access_token` values (may be in pair with `refresh_token` values) for targets which has Race Condition bug.

6) Check obtained `access_token`s as in previous Proof-of-Concept. All of them are valid and working for API.

7) Please note that Race Condition is probabilistic vulnerability. It may be needed to do few attempts with PoC to reproduce it. Attackers usually can generate some additional load to the server (not DoS, but many requests to vulnerable script) to increase the chance of successful exploitation.

8) Here execution flow has two possible directions:
8A) Go to **settings** or **applications** page in the victim's account and revoke access for the application. Then repeat step 5 and see if all `access_token`s become invalid or not. If all `access_token`s are invalid, It is good behavior despite successful Race Condition exploitation. Actually, in some cases only one `access_token` is revoked, while all the rest stay valid.

8B) Use revocation request (like `/oauth/revoke`) for one of the `access_token`s. Then repeat step 5 and see that in this case only one token is revoked, while all the rest stay active (except one of the targets tested).


Exploitation for `refresh_token` is more dangerous than for `access_token`, because there is no way for an attacker to fail. Each exploitation gives at least one new `refresh_token` which may be used further. Thus, number of token pairs grows exponentially.

Impact
======
Generating huge number of tokens for access is serious issue which violates [OAuth framework RFC](https://tools.ietf.org/html/rfc6749) and best practices. This vulnerability deprives a victim of ability to deny access for malicious application (for most of implementations tested).

Because of target (e.g `/oauth/token`) script is vulnerable to Race Condition, there are more attack vectors than I demonstrated. For example, an application may infinitely refresh its access and user would not be able to revoke access too.

Put it simply
-----------------
OAuth API is widespread mechanism nowadays. Number of different services and applications increases so fast, that almost no one wants to have so many different accounts for all of them. This is why OAuth is popular and important. But, on the other hand, no one wants to grant access to yet another one service/application, if he knows that it is impossible for him to revoke deny access later. This is why such bypassing of access revocation should be prevented.



## Attachments
No attachments
