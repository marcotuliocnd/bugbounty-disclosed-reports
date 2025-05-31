# No Data Validation, No Captcha, No Filters...

## Report Details
- **Report ID**: 363863
- **URL**: https://hackerone.com/reports/363863
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-06-10T04:28:28.859Z
- **Disclosed**: 2018-06-11T13:55:24.844Z

## Reporter
- **Username**: g0dz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
```
POST /for/new HTTP/1.1
Host: liberapay.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://liberapay.com/for/new
Cookie: __cfduid=dec7fa01079ce07bb54844ee12fafb51c1528593599; csrf_token=Y1wbnOu1ykM7eNq0DuCNs5fDoGInaDa5; session="647226:1:GER3tosCuKW0BtbQP2zgtOxn_VHaGn6-"
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 138

csrf_token=Y1wbnOu1ykM7eNq0DuCNs5fDoGInaDa5&name=§%26%2347%26%2347%26%2347%26%2347%26%2347%26%2347%26%2347%26%2347%26%2347%26%2347§&lang=mul
```

No captcha, no communities limit.
Create communities with a bot forever. (just changing the name...)

## Impact

Can create infinites communities, flooding the server.
Impacts integrity.
Lags the webserver.

## Attachments
No attachments
