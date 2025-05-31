# reflected XSS avito.ru

## Report Details
- **Report ID**: 344429
- **URL**: https://hackerone.com/reports/344429
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-04-29T17:35:44.327Z
- **Disclosed**: 2018-12-06T09:45:27.785Z

## Reporter
- **Username**: circuit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: avito

## Vulnerability Information
Привет, авито) 

Я нашел у вас хсс.

1. Переходим по этой ссылке https://www.avito.ru/sankt-peterburg?verifyUserLocation=1#login?next=javascript:alert();//
2. Логинимся через ОК, ВК и т.д.
3. XSS выполнена.

## Impact

XSS

## Attachments
No attachments
