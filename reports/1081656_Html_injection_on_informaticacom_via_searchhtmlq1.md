# Html injection on ██████.informatica.com via search.html?q=1

## Report Details
- **Report ID**: 1081656
- **URL**: https://hackerone.com/reports/1081656
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-19T16:15:01.998Z
- **Disclosed**: 2021-02-12T12:51:34.616Z

## Reporter
- **Username**: lu3ky-13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
hello dear 

I have found HTML injection  on ██████.informatica.com

parameters injectable  search.html?q=1

URL :  https://████████.informatica.com/search.html?q=1%22%3E%3Cimg%20src=https://www.no-gods-no-masters.com/images_designs/anonymous-gandhi-d001001207265.png%3E%E2%80%9D@x.y%20%22

payload ; 1"><img src=https://www.no-gods-no-masters.com/images_designs/anonymous-gandhi-d001001207265.png>”@x.y "

https://█████.informatica.com/search.html?q=1%3Ca%20href=%22//bf.am%22%3EWelcome%3C/a%3E

payload : <a href="//bf.am">Welcome</a>

## Impact

Phising

    Abusing other user

    Defacing

## Attachments
No attachments
