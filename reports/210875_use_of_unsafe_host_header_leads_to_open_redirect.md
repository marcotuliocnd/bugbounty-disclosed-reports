# use of unsafe host header leads to open redirect

## Report Details
- **Report ID**: 210875
- **URL**: https://hackerone.com/reports/210875
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-03-05T15:05:05.461Z
- **Disclosed**: 2017-05-01T14:20:41.291Z

## Reporter
- **Username**: exception
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rockstargames

## Vulnerability Information
Hi guys

I noticed you are using unsafe host header in generating short links.

#Details 
First i navigated to my account 
`https://socialclub.rockstargames.com/member/xerojuzto`

Then i created a new message , and i clicked on share button which shortens the url for example 

From `https://socialclub.rockstargames.com/member/xerojuzto/feed/3073813190982488067` 
to `http://rsg.ms/517ae7c`

I fetched the http requests to find the end-point which is used to shorten urls.
`https://socialclub.rockstargames.com/some_dirs/share/Person/getcontent?_=1488723542848`

the end-point is taking all the url parts before `/Share/Person` and creates a short link corresponding to this cut url.

I Guess the code looks like 
```
<?php
$actual_link = "https://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
$trimed_link=explode($actual_link,"/Share");

$short=DB_Create_short_link($trimed_link);
echo $short;
?>
```
Did you notice the usage of `HTTP_HOST` which  is variable and could be changed by sending different host header values , this will result in creating malicious urls.

The following request 
```
GET /feed/102126489/activity/3073813190982488067/share/Person/getcontent?_=1488723542848 HTTP/1.1
Host: socialclub.rockstargames.com
```
Is meant to shorten `/feed/102126489/activity/3073813190982488067` to `http://rsg.ms/517ae7c`   but due to not sharing my wall , it will create another redirect to my profile `https://socialclub.rockstargames.com/member/xerojuzto`

#Exploiting
I tried to manipulate the host header to force it to redirect the client  to my domain

```
GET /feed/102126489/activity/2960911889698885091/share/Person/getcontent?_=1488725310707 HTTP/1.1
Host: socialclub.rockstargames.com.this.is.my.domain.evil.net
```

and it resulted in creating `http://rsg.ms/5350b75` if you visited it , you would be redirected to 

`https://socialclub.rockstargames.com.this.is.my.domain.evil.net/member/xerojuzto/feed/2960911889698885091` 
Which is not your domain.

#Consequences
1- Phishing attacks
2- Open redirects
3- Cache poisoning and password reset leakage (Limited)

#Steps to reproduce
1- Log into your account at socialclub
2- Navigate to your profile
3- Post a new message
4- Set up a proxy server (i used burp)
5- Configure your browser(firefox in my case) to work with the proxy server
6- Click on share button 
7- Intercept the request
8- Manipulate the host header and copy the generated shorten url (ex: rsg.ms/5350b75)
9- Visit it and you will see a redirect to the injected domain.

you can visit `http://rsg.ms/5350b75` , if you need a video just shout me .


#Fix
- If you are shortening urls from only `socialclub` , then you should correctly validate the host header 
-If you are using many domains 
   you should create a white list for them before constructing urls.


#Ref 
http://www.skeletonscribe.net/2013/05/practical-http-host-header-attacks.html



Best regards
Yasser












## Attachments
- RSG_Request.http
- RS_req_resp.png
