# Subdomains takeover of  register.acronis.com, promo.acronis.com, info.acronis.com and promosandbox.acronis.com

## Report Details
- **Report ID**: 1018790
- **URL**: https://hackerone.com/reports/1018790
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-10-26T12:31:00.445Z
- **Disclosed**: 2022-02-08T09:12:37.155Z

## Reporter
- **Username**: ashmek
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary:
The Subdomains  https://register.acronis.com,  https://promo.acronis.com, https://info.acronis.com  and  https://promosandbox.acronis.com 
are vulnerable to takeover due to unclaimed marketo CNAME records.  Anyone is able to own these  subdomains at the moment.

This vulnerability is called subdomain takeover. You can read more about it here:

    https://blog.sweepatic.com/subdomain-takeover-principles/
    https://hackerone.com/reports/32825
    https://hackerone.com/reports/779442	
    https://hackerone.com/reports/175070

## Steps To Reproduce:

```
nslookup register.acronis.com
Non-authoritative answer:
Name: sjh.mktossl.com
Addresses:104.17.74.206
          104.17.72.206
          104.17.70.206
          104.17.73.206
          104.17.71.206
Aliases:  register.acronis.com
          acronis.mktoweb.com

nslookup promo.acronis.com
Non-authoritative answer:
Name:    sjh.mktossl.com
Addresses:  104.17.71.206
          104.17.70.206
          104.17.74.206
          104.17.72.206
          104.17.73.206
Aliases:  promo.acronis.com
          acronis.mktoweb.com

```

CNAMES entries to corresponding  domains are as:
```
promo.acronis.com                               acronis.mktoweb.com
promosandbox.acronis.com                   acronissandbox2.mktoweb.com
register.acronis.com                            acronis.mktoweb.com
info.acronis.com  	                             mkto-h0084.com
```

As  register.acronis.com and promo.acronis.com pointing to CNAME record as  acronis.mktoweb.com  and are aliases to acronis.mktoweb.com . http://acronis.mktoweb.com/ is giving 404, page not found  with message "The requested URL was not found on this server"  which can  be claimed by anyone now and would result in subdomain takeover.

The marketo document to Customize Your Landing Page URLs with a CNAME
https://docs.marketo.com/display/public/DOCS/Customize+Your+Landing+Page+URLs+with+a+CNAME

**As marketo is a paid service and offers account for marketing automation, I don't have a registered account. 
I wrote to Marketo technical support team and they claim the availability of listed domains as the listed domains are not in use or configured anymore.**

## Supporting Material/References:
Please refer to attached screenshots.

## Impact

With this, I can clearly see XSS impact in your case. Please have a look at your /v2/account request intercepted below:
Request:
```
PUT /v2/account HTTP/1.1
Host: account.acronis.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Content-Length: 702
Origin: https://register.acronis.com
Connection: close
Referer: https://account.acronis.com/
Cookie: _gcl_au=1.1.36144172.1601449011; _ga=GA1.2.1290766356.1601449012; _fbp=fb.1.1601449012432.633797135; _hjid=a7dd36be-ea53-40b1-b04e-c2a96f5ebc3c; optimizelyEndUserId=oeu1601449014822r0.42778295429069313; OptanonConsent=isIABGlobal=false&datestamp=Mon+Oct+26+2020+16%3A35%3A28+GMT%2B0530+(India+Standard+Time)&version=6.6.0&hosts=&consentId=07081eac-3ae3-443d-8451-79f5327d9351&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1%2CC0003%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=IN%3BHR; _mkto_trk=id:929-HVV-335&token:_mch-acronis.com-1601449020651-40834; OptanonAlertBoxClosed=2020-10-26T11:05:28.204Z; visid_incap_1638029=Bol4fqOiQTKxMXB55rfSHvSPlF8AAAAAQUIPAAAAAACe+MbhqMW1sJI4dpZBH6DI; _hjTLDTest=1; nlbi_1638029=ibxAVmtdEHzy/Y9u+BxnEAAAAAB308NLs7A3ARoQwyk4Cyrg; incap_ses_745_1638029=ddKxJtFthhy2IeNut8VWCvWPlF8AAAAACuwA/vpt+9dXQmj6hoxBWQ==; _gid=GA1.2.639811834.1603690260; _gac_UA-149943-47=1.1603691724.Cj0KCQjwxNT8BRD9ARIsAJ8S5xZC0_Hlxu0wgG7xA0-jU5eIi2BxoGFsRealW_kNcbHRyB_H8h3z-y0aAjFAEALw_wcB; AcronisSID.en=8a4d91ace2ecadca23dda91cdcb5abc5; AcronisUID.en=1438137573; _hjAbsoluteSessionInProgress=1; _uetsid=6d516b50174c11eb8ef2b18637bee740; _uetvid=b490e7509541648c67826dc18a0c7c46; _gat_UA-149943-47=1
```

Response:
```
HTTP/1.1 200 OK
Server: nginx
Date: Mon, 26 Oct 2020 11:59:18 GMT
Content-Type: application/json
Connection: close
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
pragma: no-cache
expires: -1
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 97
Access-Control-Allow-Origin: https://register.acronis.com
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Accept-Language, Authorization, Cache-Control, Connection, DNT, Keep-Alive, If-Modified-Since, Origin, Save-Data, User-Agent, X-Requested-With, Content-Type
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS
p3p: CP=IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT
X-Frame-Options: SAMEORIGIN
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-XSS-Protection: 1; mode=block
Content-Length: 714
```
See in response below,:
```
Access-Control-Allow-Origin: https://register.acronis.com
Access-Control-Allow-Credentials: true
```
Access-Control-Allow-Credentials are true for Access-Control-Allow-Origin as *.acronis.com which makes Credentials  true for all subdomains of acronis.com. Cross-Origin Resource Sharing (CORS) allows cross-domain access from all subdomains of acronis.com

Therefore, by taking over listed subdomains or finding any XSS vulnerability in any of the listed subdomains  can  steal user information  or read arbitrary data from the accounts of other users. 

The Subdomain takeover allows various attacks.

    Malware distribution
    Phishing / Spear phishing
    XSS
    Authentication bypass
    ...

List goes on and on. Since some certificate authorities (Let's Encrypt) require only domain verification, SSL certificate can be easily generated.
An attacker can utilize these domains for targeting the organization by fake login forms, or steal sensitive information of teams (credentials,  information, etc)

FIX & MITIGATION
**You should immediately remove the CNAME  entries for these domains or point it elsewhere if you don't use marketo services.**

Please let me know if more info needed or any help.

Best Regards,
Ashmek

## Attachments
- 404.PNG
- dns-1.PNG
- dns-2.PNG
- info-404.PNG
