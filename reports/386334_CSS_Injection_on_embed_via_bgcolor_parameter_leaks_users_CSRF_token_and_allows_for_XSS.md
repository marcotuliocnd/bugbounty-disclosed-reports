# CSS Injection on /embed/ via bgcolor parameter leaks user's CSRF token and allows for XSS 

## Report Details
- **Report ID**: 386334
- **URL**: https://hackerone.com/reports/386334
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-07-24T18:02:24.808Z
- **Disclosed**: 2018-09-19T23:37:20.507Z

## Reporter
- **Username**: nahamsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
Hi there,

There's a CSS injection here: https://chaturbate.com/embed/admin/?bgcolor=%7D*%7Bbackground:red&tour=nvfS&disable_sound=0&campaign=iNSGX 

```
  body, div#main, div.content, div.block, div.section {margin: 0px; padding: 0px;}
  body {min-width:800px;}
  div.content {width: 100%;}
  
  body {background: }*{background:red;}

```

This allows an attacker to enumerate the CSRF token. Once the CSRF token is enumerated, we can 

#POC 
1. Go to `http://d0nut.pythonanywhere.com/demo/token_stealing/7GTt5qD1LD273WYkJyaR/reset`
2. Now go to `http://d0nut.pythonanywhere.com/demo/token_stealing/7GTt5qD1LD273WYkJyaR` and let it do it's magic :) 

{F324052}

There are numerous endpoints like `POST /choose_broadcaster_chat_color` where it returns `Content-Type: text/html; charset=utf-8` that could potentially allow a hacker to combine the two for XSS (I haven't gotten that far yet)


 **Do you mind asking your HackerOne contact to allow collaboration on your program, so I can invite another researcher that helped me exploit this fully?**

Thanks,
Ben

## Impact

#

## Attachments
- cssi.gif
