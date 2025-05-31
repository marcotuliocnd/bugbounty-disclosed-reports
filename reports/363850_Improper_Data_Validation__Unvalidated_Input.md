# Improper Data Validation / Unvalidated Input

## Report Details
- **Report ID**: 363850
- **URL**: https://hackerone.com/reports/363850
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-06-10T02:24:34.153Z
- **Disclosed**: 2018-07-05T07:54:38.554Z

## Reporter
- **Username**: g0dz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
Steps to reproduce:

1 - Be logged in a account
2 - Go to: https://liberapay.com/{user}/edit/statement
3 - Click on Visualize
4 - Submit (and edit POST parameters to fuzz infinitely)
5 - Wait the server proccess the request.

I send only 2.813.054 characters. 

Improper input size validation...

I'm sorry. The server gets a bit lagged.
My account in website is cardangi, if u guys want to check the characters that I got stored in DB... 

```
POST /cardangi/edit/statement HTTP/1.1
Host: liberapay.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://liberapay.com/cardangi/edit/statement
Cookie: __cfduid=dec7fa01079ce07bb54844ee12fafb51c1528593599; csrf_token=Y1wbnOu1ykM7eNq0DuCNs5fDoGInaDa5; session="647226:1:GER3tosCuKW0BtbQP2zgtOxn_VHaGn6-"
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 2813138

csrf_token=Y1wbnOu1ykM7eNq0DuCNs5fDoGInaDa5&lang=pt&summary=&statement={VULNERABLE}&preview=true
```

## Impact

An attacker can send UNLIMITATED data to the server.
He can do a unlimited fuzzing too.
Affects totally availability, server response...

Maybe null terminators? Who knows.

Basically, no captcha to register, real attack scenario:

1 - Create with a bot 100+ accounts
2 - Send packets of GB's and GB's of strings to the field
3 - Wait for the CHAOS! :]

## Attachments
No attachments
